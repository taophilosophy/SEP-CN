# Bohmian Mechanics
**First published Fri Oct 26, 2001; substantive revision Sat Sep 20, 2025**

*Goldstein, Sheldon*

Bohmian mechanics, which is also called the de Broglie-Bohm theory, the pilot-wave model, and the causal interpretation of quantum mechanics, is a version of quantum theory discovered by Louis de Broglie in 1927 and rediscovered by David Bohm in 1952. It is the simplest example of what is often called a hidden variables interpretation of quantum mechanics. In Bohmian mechanics a system of particles is described in part by its wave function, evolving, as usual, according to Schrödinger’s equation. However, the wave function provides only a partial description of the system. This description is completed by the specification of the actual positions of the particles. The latter evolve according to the “guiding equation”, which expresses the velocities of the particles in terms of the wave function. Thus, in Bohmian mechanics the configuration of a system of particles evolves via a deterministic motion choreographed by the wave function. In particular, when a particle is sent into a two-slit apparatus, the slit through which it passes and its location upon arrival on the photographic plate are completely determined by its initial position and wave function.

Bohmian mechanics inherits and makes explicit the nonlocality implicit in the notion, common to just about all formulations and interpretations of quantum theory, of a wave function on the configuration space of a many-particle system. It accounts for all of the phenomena governed by nonrelativistic quantum mechanics, from spectral lines and scattering theory to superconductivity, the quantum Hall effect and quantum computing. In particular, the usual measurement postulates of quantum theory, including collapse of the wave function and probabilities given by the absolute square of probability amplitudes, emerge from an analysis of the two equations of motion: Schrödinger’s equation and the guiding equation. No invocation of a special, and somewhat obscure, status for observation is required.

## 1. The Completeness of the Quantum Mechanical Description

Conceptual difficulties have plagued quantum mechanics since its inception, despite its extraordinary predictive successes. The basic problem, plainly put, is this: It is not at all clear what quantum mechanics is about. What, in fact, does quantum mechanics describe?

It might seem, since it is widely agreed that any quantum mechanical system is completely described by its wave function, that quantum mechanics is fundamentally about the behavior of wave functions. Quite naturally, no physicist wanted this to be true more than did Erwin Schrödinger, the father of the wave function. Nonetheless, Schrödinger ultimately found this impossible to believe. His difficulty had little to do with the novelty of the wave function:

> That it is an abstract, unintuitive mathematical construct is a scruple that almost always surfaces against new aids to thought and that carries no great message. (Schrödinger [1935] 1980: 327)

Rather, it was that the “blurring” that the spread out character of the wave function suggests “affects macroscopically tangible and visible things, for which the term ‘blurring’ seems simply wrong”.

For example, in the same paper Schrödinger, echoing Einstein in the 1927 Solvay discussions (pp. 440–41 in Bacciagaluppi & Valentini 2009)[^bacciagaluppi-2009], noted that it may happen in radioactive decay that

> the emerging particle is described … as a spherical wave … that impinges continuously on a surrounding luminescent screen over its full expanse. The screen however does not show a more or less constant uniform surface glow, but rather lights up at *one* instant at *one* spot …. (Schrödinger [1935] 1980: 327–328)

And he observed that one can easily arrange, for example by including a cat in the system, “quite ridiculous cases” with

> the *ψ*-function of the entire system having in it the living and the dead cat (pardon the expression) mixed or smeared out in equal parts. (Schrödinger [1935] 1980: 328)

It is thus because of the “measurement problem”, of macroscopic superpositions, that Schrödinger found it difficult to regard the wave function as “representing reality”. But then what does? With evident disapproval, Schrödinger observes that

> the reigning doctrine rescues itself or us by having recourse to epistemology. We are told that no distinction is to be made between the state of a natural object and what I know about it, or perhaps better, what I can know about it if I go to some trouble. Actually—so they say—there is intrinsically only awareness, observation, measurement. (Schrödinger [1935] 1980: 328)

Many physicists pay lip service to the Copenhagen interpretation—that quantum mechanics is fundamentally about observation or results of measurement. But (with the exception of the proponents of QBism) it is becoming increasingly difficult to find any who, when pressed, will defend this interpretation. It seems clear that quantum mechanics is fundamentally about atoms and electrons, quarks and strings, not those particular macroscopic regularities associated with what we call *measurements* of the properties of these things. But if these entities are not somehow identified with the wave function itself—and if talk of them is not merely shorthand for elaborate statements about measurements—then where are they to be found in the quantum description?

There is, perhaps, a very simple reason why it is so difficult to discern in the quantum description the objects we believe quantum mechanics ought to describe. Perhaps the quantum mechanical description is not the whole story, a possibility most prominently associated with Albert Einstein. (For a general discussion of Einstein’s scientific philosophy, and in particular of his approach to the conflicting positions of realism and positivism, see the entry on Einstein’s philosophy of science.)

In 1935 Einstein, Boris Podolsky and Nathan Rosen defended this possibility in their famous EPR paper. They concluded with this observation:

> While we have thus shown that the wave function does not provide a complete description of the physical reality, we left open the question of whether or not such a description exists. We believe, however, that such a theory is possible. (Einstein et al. 1935: 780)[^einstein-1935]

The argument that the EPR paper advances to support this conclusion invokes quantum correlations and an assumption of locality. (See the entries on the Einstein-Podolsky-Rosen argument in quantum theory and on quantum entanglement and information.)

Later, on the basis of more or less the same considerations as those of Schrödinger quoted above, Einstein again concluded that the wave function does not provide a complete description of individual systems, an idea he called “this most nearly obvious interpretation” (Einstein 1949: 672)[^einstein-1949]. In relation to a theory incorporating a more complete description, Einstein remarked that

> the statistical quantum theory would … take an approximately analogous position to the statistical mechanics within the framework of classical mechanics. (Einstein 1949: 672)[^einstein-1949]

We note here, and show below, that Bohmian mechanics exactly fits this description.

## 2. The Impossibility of Hidden Variables … or the Inevitability of Nonlocality?

John von Neumann, one of the greatest mathematicians of the twentieth century, claimed that he had proven that Einstein’s dream of a deterministic completion or reinterpretation of quantum theory was mathematically impossible. He concluded that

> It is therefore not, as is often assumed, a question of a re-interpretation of quantum mechanics—the present system of quantum mechanics would have to be objectively false, in order that another description of the elementary processes than the statistical one be possible. (von Neumann [1932] 1955: 325)

Physicists and philosophers of science almost universally accepted von Neumann’s claim. (The philosopher [Grete Hermann](https://www.springer.com/gp/book/9789402409680/) was a notable exception.) For example, Max Born, who formulated the statistical interpretation of the wave function, assured us that

> No concealed parameters can be introduced with the help of which the indeterministic description could be transformed into a deterministic one. Hence if a future theory should be deterministic, it cannot be a modification of the present one but must be essentially different. (Born 1949: 109)[^born-1949]

Bohmian mechanics is a counterexample to the claims of von Neumann and Born. Thus von Neumann’s argument must be wrong. In fact, according to John Bell, von Neumann’s assumptions (about the relationships among the values of quantum observables that must be satisfied in a hidden-variables theory, see Bell 1966)[^bell-1966] are so unreasonable that “the proof of von Neumann is not merely false but *foolish*!” (Mermin 1993: 805, fn 8, quoting an interview in *Omni*, May, 1988: 88)[^mermin-1993]. Nonetheless, some physicists continue to rely on von Neumann’s proof.

Recently, however, physicists more commonly cite the Kochen-Specker Theorem and, even more frequently, Bell’s inequality in support of the contention that a deterministic completion of quantum theory is impossible. We still find, a quarter of a century after the rediscovery of Bohmian mechanics in 1952, statements such as these:

> The proof he [von Neumann] published …, though it was made much more convincing later on by Kochen and Specker (1967), still uses assumptions which, in my opinion, can quite reasonably be questioned. … In my opinion, the most convincing argument against the theory of hidden variables was presented by J.S. Bell (1964)[^bell-1964]. (Wigner [1976] 1983: 291)

Now there are many more statements of a similar character that we could cite. This quotation is significant because Wigner was one of the leading physicists of his generation. Unlike most of his contemporaries, moreover, he was also profoundly concerned about the conceptual foundations of quantum mechanics and wrote on the subject with great clarity and insight.

There was, however, one physicist who wrote on this subject with even greater clarity and insight than Wigner himself: the very J. S. Bell whom Wigner praises for demonstrating the impossibility of a deterministic completion of quantum theory such as Bohmian mechanics. Here’s how Bell himself reacted to Bohm’s discovery:

> But in 1952 I saw the impossible done. It was in papers by David Bohm. Bohm showed explicitly how parameters could indeed be introduced, into nonrelativistic wave mechanics, with the help of which the indeterministic description could be transformed into a deterministic one. More importantly, in my opinion, the subjectivity of the orthodox version, the necessary reference to the “observer”, could be eliminated. …
>
> But why then had Born not told me of this “pilot wave”? If only to point out what was wrong with it? Why did von Neumann not consider it? More extraordinarily, why did people go on producing “impossibility” proofs, after 1952, and as recently as 1978? … Why is the pilot wave picture ignored in text books? Should it not be taught, not as the only way, but as an antidote to the prevailing complacency? To show us that vagueness, subjectivity, and indeterminism, are not forced on us by experimental facts, but by deliberate theoretical choice? (Bell 1982, reprinted in 1987c: 160)[^bell-1982][^bell-1987c]

Wigner to the contrary notwithstanding, Bell did not establish the impossibility of a deterministic reformulation of quantum theory, nor did he ever claim to have done so. On the contrary, until his untimely death in 1990, Bell was the prime proponent, and for much of this period almost the sole proponent, of the very theory, Bohmian mechanics, that he supposedly demolished.

Bohmian mechanics is of course as much a counterexample to the Kochen-Specker argument for the impossibility of hidden variables as it is to the one of von Neumann. It is obviously a counterexample to any such argument. However reasonable the assumptions of such an argument may be, some of them must fail for Bohmian mechanics.

Wigner was quite right to suggest that the assumptions of Kochen and Specker are more convincing than those of von Neumann. They appear, in fact, to be quite reasonable indeed. However, they are not. The impression that they are arises from a pervasive error, an uncritical realism about operators, that we discuss below in the sections on quantum observables, spin, and contextuality.

John Bell replaced the “arbitrary axioms” (Bell 1966, reprinted 1987c: 11)[^bell-1966][^bell-1987c] of Kochen-Specker and others by an assumption of locality, of no action-at-a-distance. It would be hard to argue against the reasonableness of such an assumption, even if one were so bold as to doubt its inevitability. Bell showed that any hidden-variables formulation of quantum mechanics must be nonlocal, as, indeed, Bohmian mechanics is. But he showed much much more. (For more detail on Bell’s locality assumption, see Goldstein et al. 2011 and Norsen 2011.)[^goldstein-2011][^norsen-2011]

In a celebrated paper he published in 1964, Bell showed that quantum theory itself is irreducibly nonlocal. (More precisely, Bell’s analysis applies to any single-world version of quantum theory, i.e., any version for which measurements have outcomes that, while they may be random, are nonetheless unambiguous and definite, in contrast to the situation with Everett’s many-worlds version of quantum theory.) This fact about quantum mechanics, based as it is on a short and mathematically simple analysis, could have been recognized soon after the discovery of quantum theory in the 1920’s. That this did not happen is no doubt due in part to the obscurity of orthodox quantum theory and to the ambiguity of its commitments. (It almost did happen: Schrödinger 1935, in his famous cat paper, came remarkably close to discovering a Bell-type argument for quantum nonlocality. For details see Hemmick and Shakur 2012, chapter 4. For a more accessible presentation see Bricmont et al. 2020 and 2022.)[^bricmont-2020][^bricmont-2022][^hemmick-2012][^schrödinger-1935] It was, in fact, his examination of Bohmian mechanics that led Bell to his nonlocality analysis. In the course of investigating Bohmian mechanics, he observed that:

> in this theory an explicit causal mechanism exists whereby the disposition of one piece of apparatus affects the results obtained with a distant piece. …
>
> Bohm of course was well aware of these features of his scheme, and has given them much attention. However, it must be stressed that, to the present writer’s knowledge, there is no *proof* that *any* hidden variable account of quantum mechanics *must* have this extraordinary character. It would therefore be interesting, perhaps, to pursue some further “impossibility proofs”, replacing the arbitrary axioms objected to above by some condition of locality, or of separability of distant systems. (Bell 1966: 452; reprinted 1987c: 11)[^bell-1966]

In a footnote, Bell added that “Since the completion of this paper such a proof has been found” (1966: 452, fn. 19). He published it in his 1964 paper, “On the Einstein-Podolsky-Rosen Paradox”. In this paper he derives Bell’s inequality, the basis of his conclusion of quantum nonlocality. (See the entry on Bell’s Theorem. For a discussion of how nonlocality emerges in Bohmian mechanics, see Section 13.)

It is worth stressing that Bell’s analysis indeed shows that any (single-world) account of quantum phenomena must be nonlocal, not just any hidden variables account. Bell showed that the predictions of standard quantum theory itself imply nonlocality. Thus if these predictions govern nature, then nature is nonlocal. [That nature is so governed, even in the crucial EPR-correlation experiments, has by now been established by a great many experiments. The first rather conclusive such experiment was that of Aspect (Aspect, Dalibard, & Roger 1982)[^aspect-1982]. More conclusive still is the experiment of Weihs et al. 1998. Very recently there have been several “loop-hole free” tests of Bell’s inequality (Giustina et al. 2015; Hensen et al. 2015; and Shalm et al. 2015. See also the entry on Bell’s Theorem.)[^giustina-2015][^hensen-2015][^shalm-2015].]

Bell, too, stressed this point (by determinism Bell here means hidden variables):

> It is important to note that to the limited degree to which *determinism* plays a role in the EPR argument, it is not assumed but *inferred*. What is held sacred is the principle of “local causality”—or “no action at a distance”…
>
> It is remarkably difficult to get this point across, that determinism is not a *presupposition* of the analysis. (Bell 1981a, reprinted 1987c: 143)[^bell-1981a][^bell-1987c]
>
> Despite my insistence that the determinism was inferred rather than assumed, you might still suspect somehow that it is a preoccupation with determinism that creates the problem. Note well then that the following argument makes no mention whatever of determinism. … Finally you might suspect that the very notion of particle, and particle orbit … has somehow led us astray. … So the following argument will not mention particles, nor indeed fields, nor any other particular picture of what goes on at the microscopic level. Nor will it involve any use of the words “quantum mechanical system”, which can have an unfortunate effect on the discussion. The difficulty is not created by any such picture or any such terminology. It is created by the predictions about the correlations in the visible outputs of certain conceivable experimental set-ups. (Bell 1981a, reprinted 1987c: 150)[^bell-1981a][^bell-1987c]

The “problem” and “difficulty” to which Bell refers above is the conflict between the predictions of quantum theory and what can be inferred, call it $C$, from an assumption of locality in Bohm’s version of the EPR argument, a conflict established by Bell’s inequality. $C$ happens to concern the existence of a certain kind of hidden variables, what might be called local hidden variables, but this fact is of little substantive importance. What is important is not so much the identity of $C$ as the fact that $C$ is incompatible with the predictions of quantum theory. The identity of $C$ is, however, of great historical significance: it is responsible for the misconception that Bell proved that hidden variables are impossible, a belief that physicists until recently almost universally shared, as well as for the view, even now almost universally held, that what Bell’s result does is to rule out local hidden variables, a view that is misleading.

Here again is Bell, expressing the logic of his *two-part* demonstration of quantum nonlocality, the first part of which is Bohm’s version of the EPR argument, concerning EPRB correlations:

> Let me summarize once again the logic that leads to the impasse. The EPRB correlations are such that the result of the experiment on one side immediately foretells that on the other, whenever the analyzers happen to be parallel. If we do not accept the intervention on one side as a causal influence on the other, we seem obliged to admit that the results on both sides are determined in advance anyway, independently of the intervention on the other side, by signals from the source and by the local magnet setting. But this has implications for non-parallel settings which conflict with those of quantum mechanics. So we *cannot* dismiss intervention on one side as a causal influence on the other. (Bell 1981a, reprinted 1987c: 149)[^bell-1981a][^bell-1987c]

As with just about everything else in the foundations of quantum mechanics, there remains considerable controversy about what exactly Bell’s analysis demonstrates. (For further insight into the various controversies see Maudlin 2014 and Goldstein et al. 2011. See also the entry on Bell’s Theorem.)[^goldstein-2011][^maudlin-2014] Nonetheless, the opinion of Bell himself about what he showed is perfectly clear. See Norsen 2011 for a nice overview of Bell’s views on the matter.

## 3. History

The pilot-wave approach to quantum theory was initiated by Einstein, even before the discovery of quantum mechanics itself. Einstein hoped that interference phenomena involving particle-like photons could be explained if the motion of the photons was somehow guided by the electromagnetic field—which would thus play the role of what he called a *Führungsfeld* or guiding field (see Wigner [1976] 1983: 262 and Bacciagaluppi and Valentini 2009: Ch. 9)[^bacciagaluppi-2009]. While the notion of the electromagnetic field as guiding field turned out to be rather problematical, Max Born explored the possibility that the wave function could play this role, of guiding field or pilot wave, for a system of electrons in his early paper founding quantum scattering theory (Born 1926)[^born-1926]. Heisenberg was profoundly unsympathetic.

Not long after Schrödinger’s discovery of wave mechanics in 1926, i.e., of Schrödinger’s equation, a discovery inspired by Louis de Broglie’s 1924 Ph.D. thesis, de Broglie in effect discovered Bohmian mechanics: In 1927, de Broglie found an equation of particle motion equivalent to the guiding equation for a scalar wave function (de Broglie 1928: 119)[^broglie-1928], and he explained at the 1927 Solvay Congress how this motion could account for quantum interference phenomena. However, despite what is suggested by Bacciagaluppi and Valentini (2009), de Broglie responded very poorly to an objection of Wolfgang Pauli (Pauli 1928)[^pauli-1928] concerning inelastic scattering, no doubt making a rather bad impression on the illustrious audience at the congress.

Born and de Broglie very quickly abandoned the pilot-wave approach and became supporters of the rapidly developing consensus in favor of the Copenhagen interpretation. David Bohm (1952)[^bohm-1952] rediscovered de Broglie’s pilot-wave theory in 1952. He was the first person to genuinely understand its significance and implications. John Bell became its principal proponent during the sixties, seventies and eighties.

For a very good discussion of the history of quantum mechanics, the debates about its foundations, and about the reception of Bohmian mechanics in particular, see Bricmont 2016 and Becker 2018. See also Beller 1999.

## 4. The Defining Equations of Bohmian Mechanics

In Bohmian mechanics the wave function, obeying Schrödinger’s equation, does not provide a complete description or representation of a quantum system. Rather, it governs the motion of the fundamental variables, the positions of the particles: In the Bohmian mechanical version of nonrelativistic quantum theory, quantum mechanics is fundamentally about the behavior of particles; the particles are described by their positions, and Bohmian mechanics prescribes how these change with time. In this sense, for Bohmian mechanics the particles are primary, or primitive, while the wave function is secondary, or derivative. (Bohmian mechanics, like classical mechanics, is thus a theory grounded in a *primitive ontology*, for Bohmian mechanics one of particles described by their positions. This terminology was introduced in Dürr et al. 1992a. For more on the notion of primitive ontology, see Allori et al. 2008 and Allori 2015.)

Warning: It is the positions of the particles in Bohmian mechanics that are its “hidden variables”, an unfortunate bit of terminology. As Bell writes, referring to Bohmian mechanics and similar theories,

> Absurdly, such theories are known as “hidden variable” theories. Absurdly, for there it is not in the wavefunction that one finds an image of the visible world, and the results of experiments, but in the complementary “hidden”(!) variables. Of course the extra variables are not confined to the visible “macroscopic” scale. For no sharp definition of such a scale could be made. The “microscopic” aspect of the complementary variables is indeed hidden from us. But to admit things not visible to the gross creatures that we are is, in my opinion, to show a decent humility, and not just a lamentable addiction to metaphysics. In any case, the most hidden of all variables, in the pilot wave picture, is the wavefunction, which manifests itself to us only by its influence on the complementary variables. (1987a, reprinted 1987c: 201–202)

Bohmian mechanics is the minimal completion of Schrödinger’s equation, for a nonrelativistic system of particles, to a theory describing a genuine motion of particles. For Bohmian mechanics the state of a system of $N$ particles is described by its wave function $\psi = \psi(\boldsymbol{q}_1 ,\ldots ,\boldsymbol{q}_N) = \psi(q)$, a complex (or spinor-valued) function on the space of possible configurations $q$ of the system, together with its actual configuration $Q$ defined by the actual positions $\mathbf{Q}_1 ,\ldots ,\mathbf{Q}_N$ of its particles. (The word “spinor” refers to a suitable array of complex numbers in place of a single one. Spinor-valued wave functions are used in quantum mechanics to describe electrons and other quantum particles that “have spin”.) The theory is then defined by two evolution equations:

**Schrödinger’s equation** $$ i\hslash\frac{\partial \psi}{\partial t} = H\psi $$ for $\psi(t)$, where $H$ is the nonrelativistic (Schrödinger) Hamiltonian, containing the masses of the particles and a potential energy term, and (writing $\Im[z]$ for the imaginary part $b$ of a complex number $z = a +\di b)$ a first-order evolution equation,

**The guiding equation** $$ \frac{d\mathbf{Q}_k}{dt} = \frac{\hslash}{m_k} \Im {{\psi^*\partial_k\psi} \over{\psi^*\psi}} (\mathbf{Q}_1 ,\ldots ,\mathbf{Q}_N) $$ for $Q(t)$, the simplest first-order evolution equation for the positions of the particles that is compatible with the Galilean (and time-reversal) covariance of the Schrödinger evolution (Dürr, Goldstein, & Zanghì 1992a: 852–854)[^dürr-1992a]. Here $\hslash$ is Planck’s constant divided by $2\pi$, *m$_k$* is the mass of the $k$-th particle, and $\partial_k = (\partial /\partial x_k,\partial /\partial y_k,\partial /\partial z_k)$ is the gradient with respect to the generic coordinates $\boldsymbol{q}_k = (x_k,y_k,z_k)$ of the $k$-th particle. If *ψ* is spinor-valued, the two products involving *ψ* in the equation should be understood as scalar products (involving sums of products of spinor components). When external magnetic fields are present, the gradient should be understood as the covariant derivative, involving the vector potential. (Since the denominator on the right hand side of the guiding equation vanishes at the nodes of *ψ*, global existence and uniqueness for the Bohmian dynamics is a nontrivial matter. It is proven in Berndl, Dürr, et al. 1995 and in Teufel and Tumulka 2005.)[^berndl-1995][^berndl-1995-2][^dürr-2005][^teufel-2005]

For an $N$-particle system these two equations (together with the detailed specification of the Hamiltonian, including all interactions contributing to the potential energy) completely define Bohmian mechanics. This deterministic theory of particles in motion accounts for all the phenomena of nonrelativistic quantum mechanics, from interference effects to spectral lines (Bohm 1952: 175–178)[^bohm-1952] to spin (Bell 1964: 10)[^bell-1964]. And it does so in an entirely ordinary manner, as we explain in the following sections.

For a scalar wave function, describing particles without spin, the form of the guiding equation above is a little more complicated than necessary, since the complex conjugate of the wave function, which appears in the numerator and the denominator, cancels out. If one looks for an evolution equation for the configuration compatible with the space-time symmetries of Schrödinger’s equation, one almost immediately arrives at the guiding equation in this simpler form as the simplest possibility.

However, the form above has two advantages: First, it makes sense for particles with spin—and, in fact, Bohmian mechanics without further ado accounts for all the apparently paradoxical quantum phenomena associated with spin. Secondly, and this is crucial to the fact that Bohmian mechanics is empirically equivalent to orthodox quantum theory, the right hand side of the guiding equation is $J/\varrho$, the ratio of the quantum probability current $J$ to the quantum probability density $\varrho=\psi^*\psi=\lvert \psi \rvert^2$. This shows that it should require no imagination whatsoever to guess the guiding equation from Schrödinger’s equation, provided one is looking for one, since the classical formula for current is density times velocity, $J=\varrho v$. Moreover, it follows from the quantum continuity equation $\partial \varrho /\partial t + \textrm{div} J = 0$, an immediate consequence of Schrödinger’s equation, that if at some time (say the initial time) the configuration $Q$ of our system is random, with distribution given by $\lvert \psi \rvert^2 $, this will always be true (provided the system does not interact with its environment).

This demonstrates that it is wrong to claim that the predictions of quantum theory are incompatible with the existence of hidden variables—with an underlying deterministic model in which quantum randomness arises from averaging over ignorance. Bohmian mechanics provides us with just such a model: For any quantum experiment we merely take as the relevant Bohmian system the combined system, including the system upon which the experiment is performed as well as all the measuring instruments and other devices used to perform the experiment (together with all other systems with which these have significant interaction over the course of the experiment). We then obtain the “hidden variables” model by regarding the initial configuration of this big system as random in the usual quantum mechanical way, with distribution given by $\lvert \psi \rvert^2$. The guiding equation for the big system then transforms the initial configuration into the final configuration at the conclusion of the experiment. It then follows that this final configuration of the big system, including in particular the orientation of instrument pointers, will also be distributed in the quantum mechanical way. Thus our deterministic Bohmian model yields the usual quantum predictions for the results of the experiment.

As the preceding paragraph suggests, and as we discuss in more detail later, Bohmian mechanics does not need any “measurement postulates” or *axioms* governing the behavior of other “observables”. Any such axioms would be at best redundant and could be inconsistent.

Besides the guiding equation, there are other velocity formulas with nice properties, including Galilean symmetry, and yielding theories that are empirically equivalent to orthodox quantum theory—and to Bohmian mechanics (Deotto & Ghirardi 1998)[^deotto-1998]. The Bohmian choice is arguably the simplest. Moreover, Wiseman (2007)[^wiseman-2007] has shown that it is the Bohmian velocity formula, given by the guiding equation, that, according to orthodox quantum theory, would be found in a “weak measurement” of the velocity of a particle. (Marian, Zanghì, and Oriols 2016 have recently proposed an explicit procedure for performing such a measurement.)[^marian-2016] And, somewhat paradoxically, it can be shown (Dürr, Goldstein, & Zanghì 2009)[^dürr-2009][^dürr-2009-2] that according to Bohmian mechanics such a measurement is indeed a genuine measurement of the particle’s velocity—despite the existence of empirically equivalent velocity formulas!

Similarly, weak measurements could be used to measure trajectories. In fact, Kocsis et al. (2011) have used weak measurements to reconstruct the trajectories for single photons “as they undergo two-slit interference”, finding “those predicted in the Bohm-de Broglie interpretation of quantum mechanics”. And Mahler et al. 2016 have experimentally found, using weak measurements, “Bohmian trajectories” for entangled photons, illustrating quantum nonlocality and the phenomenon of “surreal Bohmian trajectories”.

For a single particle the guiding equation defines the motion of a particle guided by a wave in physical three-dimensional space. One might expect that similar motions might arise classically. Couder & Fort (2006) have shown, by investigating interference-like phenomena in the motion of bouncing oil droplets in a fluid, that this is indeed so. Bush (2015)[^bush-2015] has further explored this sort of possibility for the emergence of a Bohmian version of quantum mechanics from something like classical fluid dynamics. A formidable obstacle to the success of such a program is the quantum entanglement and nonlocality characteristic of many-particle quantum systems, whose guiding waves (unlike the waves in any pool of vibrating fluid) propagate not in three-dimensional physical space but in an abstract, higher-dimensional configuration space.

The “many interacting worlds” approach of Hall, Deckert, & Wiseman (2014), independently advanced by Sebens (2015)[^sebens-2015], retains particle trajectories but attempts to do away with a wave-function at the level of fundamental ontology. What takes its place is a large number of trajectories in configuration space, with each trajectory regarded as actual and as corresponding to the motions of a finite number of particles in physical space regarded as describing a world in its own right. These interact in such a way as to mimic trajectories guided by a wave function: a coarse-grained density of worlds takes the place of $\lvert \psi \rvert^2$. The velocities of the world-particles are required to at least approximately be related to their configurations via some smooth function on configuration space. This condition would be a rather surprising one for the sorts of large systems studied in statistical mechanics. Even more unmotivated from a classical perspective, the velocity function must be the gradient of a multivalued function that obeys a Bohr-Sommerfeld-like quantum condition.

We stress that Bohmian mechanics should be regarded as a theory in its own right. Its viability does not depend on its being derivable from some other theory, classical or otherwise.

## 5. The Quantum Potential

Bohmian mechanics as presented here is a first-order theory, in which it is the velocity, the rate of change of position, that is fundamental. It is this quantity, given by the guiding equation, that the theory specifies directly and simply. The second-order (Newtonian) concepts of acceleration and force, work and energy do not play any fundamental role.

Bohm, however, did not regard his theory in this way. He regarded it, fundamentally, as a second-order theory, describing particles moving under the influence of forces, among which, however, is a force stemming from a “quantum potential”.

In his 1952 hidden-variables paper, Bohm arrived at his theory by writing the wave function in the polar form $\psi = R$exp$(iS/\hslash)$, where $S$ and $R$ are real, with $R$ nonnegative. He then rewrote Schrödinger’s equation in terms of these new variables to obtain a pair of coupled evolution equations: the continuity equation for $\varrho = R^2$ and a modified Hamilton-Jacobi equation for $S$. The latter differs from the usual classical Hamilton-Jacobi equation only by the appearance of an extra term, the *quantum potential* $$ U = {-}\sum_k (\hslash^2 /2m_k) (\partial_{k}^2 R / R ), $$ alongside the classical potential energy term.

Bohm then used the modified Hamilton-Jacobi equation to define particle trajectories just as one does for the classical Hamilton-Jacobi equation, that is, by identifying $\partial_k S$ with $m_k\boldsymbol{v}_k$, i.e., by setting $$ d\mathbf{Q}_k /dt = \partial_k S / m_k. $$ This is equivalent to the guiding equation for particles without spin. [The (pre-Schrödinger equation) de Broglie relation $\boldsymbol{p} = \hslash \boldsymbol{k}$, as well as the eikonal equation of classical optics, already suggest the guiding equation in this form.] The resulting motion is precisely what would be obtained classically if the particles were acted upon by the force generated by the quantum potential, in addition to the usual forces.

The quantum potential formulation of the de Broglie-Bohm theory is still fairly widely used. For example, the monographs by Bohm and Hiley and by Holland present the theory in this way. And regardless of whether or not we regard the quantum potential as fundamental, it can in fact be quite useful. In order to see most clearly that Newtonian mechanics should be expected to emerge from Bohmian mechanics in the classical limit, it is convenient to transform the theory into Bohm’s Hamilton-Jacobi form. Then the (size of the) quantum potential provides a measure of the deviation of Bohmian mechanics from its classical approximation. Moreover, the quantum potential is also useful for developing approximation schemes for solutions to Schrödinger’s equation (Nerukh & Frederick 2000, Wyatt 2006)[^nerukh-2000][^wyatt-2006].

However, Bohm’s rewriting of Schrödinger’s equation in terms of variables that seem interpretable in classical terms is not without a cost. The most obvious is an increase in complexity: Schrödinger’s equation is rather simple, and it is linear, whereas the modified Hamilton-Jacobi equation is somewhat complicated, and highly nonlinear. Moreover the latter, since it involves $R$, requires the continuity equation for its closure. The quantum potential itself is neither simple nor natural. Even to Bohm it seemed “rather strange and arbitrary” (Bohm 1980: 80)[^bohm-1980]. And it is not very satisfying to think of the quantum revolution as amounting to the insight that nature is classical after all, except that there is in nature what appears to be a rather *ad hoc* additional force term, the one arising from the quantum potential. The artificiality that the quantum potential suggests is the price one pays for casting a highly nonclassical theory into a classical mold.

Moreover, the connection between classical mechanics and Bohmian mechanics that the quantum potential suggests is rather misleading. Bohmian mechanics is not simply classical mechanics with an additional force term. In Bohmian mechanics the velocities are not independent of positions, as they are classically, but are constrained by the guiding equation. (In classical Hamilton-Jacobi theory we also have this equation for the velocity, in the form displayed above, but there the Hamilton-Jacobi function $S$ can be entirely eliminated and the description in terms of $S$ simplified and reduced to a finite-dimensional description, with basic variables the positions and the (unconstrained) momenta of all the particles, given by Hamilton’s or Newton’s equations.)

Arguably, the most serious flaw in the quantum potential formulation of Bohmian mechanics is that it gives a completely false impression of the lengths to which we must go in order to convert orthodox quantum theory into something more rational. The quantum potential suggests, as has often been stated, that transforming Schrödinger’s equation into a theory that can account in “realistic” terms for quantum phenomena, many of which are dramatically nonlocal, requires adding to the theory a complicated quantum potential of a grossly nonlocal character. It should be clear that this view is inappropriate. After all, the quantum potential need not even be mentioned in the *formulation* of Bohmian mechanics, and it in any case merely reflects the wave function, which Bohmian mechanics shares with, rather than adds to, orthodox quantum theory. What it adds are the (actual positions of the) particles themselves.

## 6. The Two-Slit Experiment

According to Richard Feynman, the two-slit experiment for electrons is

> a phenomenon which is impossible, *absolutely* impossible, to explain in any classical way, and which has in it the heart of quantum mechanics. In reality it contains the *only* mystery. (Feynman, Leighton, & Sands 1963: 37–2)[^feynman-1963]

This experiment

> has been designed to contain all of the mystery of quantum mechanics, to put you up against the paradoxes and mysteries and peculiarities of nature one hundred per cent. (Feynman 1967: 130)[^feynman-1967]

As to the question,

> How does it really work? What machinery is actually producing this thing? Nobody knows any machinery. Nobody can give you a deeper explanation of this phenomenon than I have given; that is, a description of it. (Feynman 1967: 145)[^feynman-1967]

But Bohmian mechanics is just such a deeper explanation. It resolves in a rather straightforward manner the dilemma of the appearance of both particle and wave properties in one and the same phenomenon: Bohmian mechanics is a theory of motion describing a particle (or particles) guided by a wave.

Here we have a family of Bohmian trajectories for the two-slit experiment.

![[line drawing, a vertical bar on the left with two openings, multiple lines angle out to the right from each]](../assets/qm-bohm/figure1.gif)

\*Figure 1:\* An ensemble of trajectories for the two-slit experiment, uniform in the slits. (adapted by Gernot Bauer from Philippidis, Dewdney, & Hiley 1979: 23, fig. 3)[^philippidis-1979]

While each trajectory passes through only one slit, the wave passes through both; the interference profile that therefore develops in the wave generates a similar pattern in the trajectories guided by the wave.

Compare Feynman’s presentation with Bell’s:

> Is it not clear from the smallness of the scintillation on the screen that we have to do with a particle? And is it not clear, from the diffraction and interference patterns, that the motion of the particle is directed by a wave? De Broglie showed in detail how the motion of a particle, passing through just one of two holes in screen, could be influenced by waves propagating through both holes. And so influenced that the particle does not go where the waves cancel out, but is attracted to where they cooperate. This idea seems to me so natural and simple, to resolve the wave-particle dilemma in such a clear and ordinary way, that it is a great mystery to me that it was so generally ignored. (Bell [1989] 1987c: 191)

Perhaps the most puzzling aspect of the two-slit experiment is the following: If, by any means whatsoever, one determines the slit through which the particle passes, the interference pattern will then be destroyed. This dramatic effect of observation is, in fact, a simple consequence of Bohmian mechanics. To see this, one must consider the meaning of determining the slit through which the particle passes. This must involve interaction with another system, and this system, together with the particle, must be included in a Bohmian mechanical analysis of the experiment.

The destruction of interference is related, naturally enough, to the Bohmian mechanical analysis of quantum measurement (Bohm 1952)[^bohm-1952]. It occurs via the mechanism that in Bohmian mechanics leads to the “collapse of the wave function”.

For an accessible presentation of the behavior of Bohmian trajectories in scattering and tunneling phenomena, see Norsen 2013.

## 7. The Measurement Problem

The measurement problem is the most commonly cited of the conceptual difficulties that plague quantum mechanics. (It amounts, more or less, to the paradox of Schrödinger’s cat.) Indeed, for many physicists the measurement problem is not merely one conceptual difficulty of quantum mechanics; it is *the* conceptual difficulty.

The problem is as follows. Suppose that the wave function of any individual system provides a complete description of that system. When we analyze the process of measurement in quantum mechanical terms, we find that the after-measurement wave function for system and apparatus that arises from Schrödinger’s equation for the composite system typically involves a superposition over terms corresponding to what we would like to regard as the various possible results of the measurement—e.g., different pointer orientations. In this description of the after-measurement situation it is difficult to discern the actual result of the measurement—e.g., some specific pointer orientation. But the whole point of quantum theory, and the reason we should believe in it, is that it is supposed to provide a compelling, or at least an efficient, account of our observations, that is, of the outcomes of measurements. In short, the measurement problem is this: Quantum theory implies that measurements typically fail to have outcomes of the sort the theory was created to explain.

In contrast, if we, like Einstein, regard the description provided by the wave function as incomplete, the measurement problem vanishes: There is no measurement problem with a theory or interpretation in which, as in Bohmian mechanics, the description of the after-measurement situation includes, in addition to the wave function, at least the values of the variables that register the result. In Bohmian mechanics pointers always point.

Often, the measurement problem is expressed a little differently. Textbook quantum theory provides two rules for the evolution of the wave function of a quantum system: A deterministic dynamics given by Schrödinger’s equation when the system is not being “measured” or observed, and a random collapse of the wave function to an *eigenstate* of the “measured observable” when it is. However, the objection continues, textbook quantum theory does not explain how to reconcile these two apparently incompatible rules.

That this formulation of the measurement problem and the preceding one are more or less equivalent should be reasonably clear: If a wave function provides a complete description of the after-measurement situation, the outcome of the measurement must correspond to a wave function that describes the actual result, that is, a “collapsed” wave function. Hence the collapse rule. But it is difficult to take seriously the idea that different laws than those governing all other interactions should govern those interactions between system and apparatus that we happen to call measurements. Hence the apparent incompatibility of the two rules.

The second formulation of the measurement problem, though basically equivalent to the first, raises an important question: Can Bohmian mechanics itself reconcile these two dynamical rules? How does Bohmian mechanics justify the use of the “collapsed” wave function instead of the original one? This question was answered in Bohm’s first papers on Bohmian mechanics (Bohm 1952: Part I, Section 7 and Part II, Section 2)[^bohm-1952]. What would nowadays be called effects of decoherence, produced by interaction with the environment (air molecules, cosmic rays, internal microscopic degrees of freedom, etc.), make it very difficult for significant overlap to develop between the component of the after-measurement wave function corresponding to the actual result of the measurement and the other components of the after-measurement wave function. (This overlap refers to the configuration space of the very large system that includes all systems with which the original system and apparatus come into interaction.) But without such overlap that component all by itself generates to a high degree of accuracy the future evolution of the configuration of the system and apparatus. The replacement is thus justified as a practical matter (see also Dürr, Goldstein & Zanghì 1992a: Section 5)[^dürr-1992a].

Many proponents of orthodox quantum theory believe that decoherence somehow resolves the measurement problem itself. It is not easy to understand this belief. In the first formulation of the measurement problem, nothing prevents us from including in the apparatus all sources of decoherence. But then decoherence can no longer be in any way relevant to the argument. Be that as it may, Bohm (1952)[^bohm-1952] gave one of the best descriptions of the mechanisms of decoherence, though he did not use the word itself. He recognized its importance several decades before it became fashionable. (See also the encyclopedia entry on The Role of Decoherence in Quantum Mechanics.)

## 8. The Collapse of the Wave Function

In the previous section we indicated that collapse of the wave function can be regarded in Bohmian mechanics as a pragmatic affair, that the collapse of the wave function is an *effective* collapse. However, there is a sense in which the collapse of the wave function in Bohmian mechanics is more than a matter of convenience, a sense in which the collapse is actual and not merely effective. Indeed, if we focus on the appropriate notion of the wave function, not of the composite of system and apparatus—which strictly speaking remains a superposition if the composite is treated as closed during the measurement process—but of the system itself, we find that for Bohmian mechanics this wave function does in fact collapse, precisely as the quantum formalism demands. The key element here is the notion of the *conditional wave function* of a subsystem of a larger system, which we describe briefly in this section and that Dürr, Goldstein, & Zanghì 1992a: Section 5, discuss in some detail, together with the related notion of the effective wave function.

One of the defining equations of Bohmian mechanics is Schrödinger’s equation, governing the evolution of the wave function. Among the defining equations there is no additional evolution equation prescribing collapse of the wave function. Nonetheless the textbook collapse rule is a consequence of the Bohmian dynamics. To appreciate this, one should first note that, since observation implies interaction, a system under observation cannot be a closed system but rather must be a subsystem of a larger closed system. We may take this larger system to be the entire universe, or any smaller more or less closed system that contains the system to be observed, *the subsystem*. The configuration $Q$ of this larger system naturally splits into $X$, the configuration of the subsystem, and $Y$, the configuration of the *environment* of the subsystem.

Suppose the larger system has wave function $\Psi = \Psi(q) = \Psi(x, y)$. According to Bohmian mechanics, the larger system is then completely described by *Ψ*, evolving according to Schrödinger’s equation, together with $X$ and $Y$. The question then arises—and it is a critical question—as to what should be meant by the wave function of the subsystem.

There is a rather obvious answer for this, a natural function of $x$ that suitably incorporates the objective structure at hand, namely the *conditional wave function* $$\psi(x) = \Psi(x, Y)$$ obtained by plugging the actual configuration of the environment into the wave function of the larger system. (This definition is appropriate only for scalar wave functions; for particles with spin the situation would be a little more complicated.) It then follows immediately that the configuration of the subsystem obeys the guiding equation with the conditional wave function on its right-hand side.

Moreover, taking into account the way that the conditional wave function depends upon time $t$ $$\psi_t (x) = \Psi_t (x, Y_t)$$ via the time dependence of $Y$ as well as that of *Ψ*, it is not difficult to see (Dürr, Goldstein, & Zanghì 1992a)[^dürr-1992a] the following two things about the evolution of the conditional wave: First, that it obeys Schrödinger’s equation for the subsystem when that system is suitably decoupled from its environment. Part of what is meant by this decoupling is that *Ψ* has a special form, what might be called an effective product form (similar to but more general than the superposition produced in an “ideal quantum measurement”), in which case the conditional wave function of the subsystem is also called its *effective wave function*. Second, using the quantum equilibrium hypothesis, that it randomly collapses according to the usual quantum mechanical rules under precisely those conditions on the interaction between the subsystem and its environment that define an ideal quantum measurement.

It is perhaps worth noting that orthodox quantum theory lacks the resources that make it possible to define the conditional wave function, namely, the actual configuration $Y$ of the environment. Indeed, from an orthodox point of view what should be meant by the wave function of a subsystem is entirely obscure.

For a more accessible and pedagogical discussion of the conditional wave function and its behavior, see Norsen 2017, Norsen 2014, and Stefan Teufel's video about The Little Quantum System in the Other Internet Resources.

## 9. Quantum Randomness

According to the quantum formalism, for a system with wave function *ψ* the probability density for finding its configuration to be $q$ is $\lvert\psi(q)\rvert^2$. To the extent that the results of measurement are registered configurationally, at least potentially, it follows that the predictions of Bohmian mechanics for the results of measurement must agree with those of orthodox quantum theory (assuming the same Schrödinger equation for both) provided that it is somehow true for Bohmian mechanics that configurations are random, with distribution given by the *quantum equilibrium* distribution $\lvert\psi(q)\rvert^2$. Now the status and justification of this *quantum equilibrium hypothesis* is a rather delicate matter, one that has been explored in considerable detail (Dürr, Goldstein, & Zanghì 1992a)[^dürr-1992a]. Here are a few relevant points.

It is nowadays a rather familiar fact that dynamical systems quite generally give rise to behavior of a statistical character, with the statistics given by the (or a) stationary probability distribution for the dynamics. So it is with Bohmian mechanics, except that for the Bohmian system stationarity is not quite the right concept. Rather it is the notion of *equivariance* that is relevant. A probability distribution $\varrho^{\psi}$ on configuration space, depending upon the wave function *ψ*, is *equivariant* if $$(\varrho^{\psi})_t = \varrho^{\psi_t},$$ where the dependence on $t$ on the right arises from Schrödinger’s equation and on the left from the evolution of probability distributions arising from the flow that the guiding equation induces. Thus equivariance expresses the mutual compatibility, relative to $\varrho^{\psi}$, of the Schrödinger evolution of the wave function and the Bohmian motion of the configuration. It is an immediate consequence of the guiding equation and the quantum continuity equation that $\varrho^{\psi} = \lvert\psi(q)\rvert^2$ is equivariant. (It can be shown in fact that this is more or less the only equivariant possibility that is suitably local (Goldstein & Struyve 2007)[^goldstein-2007].)

In trying to understand the status in Bohmian mechanics of the quantum equilibrium distribution, it is perhaps helpful to think of

*quantum equilibrium*, $\varrho = \lvert\psi \rvert^2$

as roughly analogous to (classical)

*thermodynamic equilibrium*, $\varrho = \textrm{exp} (-H/kT) /Z$,

the probability distribution of the phase-space point of a system in equilibrium at temperature $T$. ($Z$ is a normalization constant called the partition function and $k$ is Boltzmann’s constant.) This analogy has several facets: In both cases the probability distributions are naturally associated with their respective dynamical systems. In particular, these distributions are stationary or, what amounts to the same thing within the framework of Bohmian mechanics, equivariant. In both cases it seems natural to try to justify these equilibrium distributions by means of mixing-type, convergence-to-equilibrium arguments (Bohm 1953; Valentini & Westman 2005)[^bohm-1953][^valentini-2005]. It has been argued, however, that in both cases the ultimate justification for these probability distributions must be in terms of statistical patterns exhibited by ensembles of actual subsystems within a *typical* individual universe (Bell 1981b, reprinted 1987c: 129; Dürr, Goldstein, & Zanghì 1992a)[^bell-1981b][^bell-1987c][^dürr-1992a]. And in both cases the status of, and justification for, equilibrium distributions remains controversial (Dürr & Struyve 2020; see also Goldstein 2012)[^dürr-2020][^dürr-2020-2][^goldstein-2012][^struyve-2020].

It can nonetheless be shown (Dürr, Goldstein, & Zanghì 1992a)[^dürr-1992a] that probabilities for positions given by the quantum equilibrium distribution emerge naturally from an analysis of “equilibrium” for the deterministic dynamical system that Bohmian mechanics defines—in much the same manner that the Maxwellian velocity distribution emerges from an analysis of classical thermodynamic equilibrium. (For more on the thermodynamic side of the analogy see Goldstein 2001.)[^goldstein-2001][^goldstein-2001-2] Thus with Bohmian mechanics the statistical description in quantum theory indeed takes, as Einstein anticipated, “an approximately analogous position to the statistical mechanics within the framework of classical mechanics”.

It is also perhaps worth noting that the typicality-grounded account of quantum randomness in Bohmian mechanics is extremely similar to Everett’s account (Everett 1957)[^everett-1957] of quantum randomness for “many worlds”, despite the huge metaphysical differences that exist between these two versions of quantum theory.

## 10. Quantum Observables

Orthodox quantum theory supplies us with probabilities not merely for positions but for a huge class of quantum observables. It might thus appear that it is a much richer theory than Bohmian mechanics, which seems exclusively concerned with positions. Appearances are, however, misleading. In this regard, as with so much else in the foundations of quantum mechanics, Bell made the crucial observation:

> [I]n physics the only observations we must consider are position observations, if only the positions of instrument pointers. It is a great merit of the de Broglie-Bohm picture to force us to consider this fact. If you make axioms, rather than definitions and theorems, about the “measurement” of anything else, then you commit redundancy and risk inconsistency. (Bell 1982, reprinted 1987c: 166)[^bell-1982][^bell-1987c]

Consider classical mechanics first. The observables are functions on phase space, functions of the positions and momenta of the particles. The axioms governing the behavior of the basic observables—Newton’s equations for the positions or Hamilton’s for positions and momenta—define the theory. What would be the point of making additional axioms, for other observables? After all, the behavior of the basic observables entirely determines the behavior of any observable. For example, for classical mechanics, the principle of the conservation of energy is a theorem, not an axiom.

The situation might seem to differ in quantum mechanics, as usually construed. Here there is no small set of basic observables having the property that all other observables are functions of them. Moreover, no observables at all are taken seriously as describing objective properties, as actually having values whether or not they are or have been measured. Rather, all talk of observables in quantum mechanics is supposed to be understood as talk about the measurement of the observables.

But if this is so, the situation with regard to other observables in quantum mechanics is not really that different from that in classical mechanics. Whatever quantum mechanics means by the measurement of (the values of) observables—that, we are urged to believe, don’t actually have values—must at least refer to some experiment involving interaction between the “measured” system and a “measuring” apparatus leading to a recognizable result, as given potentially by, say, a pointer orientation. But then if some axioms suffice for the behavior of pointer orientations (at least when they are observed), rules about the measurement of other observables must be theorems, following from those axioms, not additional axioms.

It should be clear from the discussion towards the end of Section 4 and at the beginning of Section 9 that, assuming the quantum equilibrium hypothesis, any analysis of the measurement of a quantum observable for orthodox quantum theory—whatever it is taken to mean and however the corresponding experiment is performed—provides ipso facto an account for Bohmian mechanics that is at least as adequate as the one for orthodox quantum theory. The only part of orthodox quantum theory relevant to the analysis is the Schrödinger evolution, and it *shares* this with Bohmian mechanics. The main difference between them is that orthodox quantum theory encounters the measurement problem before it reaches a satisfactory conclusion while Bohmian mechanics does not. This difference stems of course from what Bohmian mechanics *adds* to orthodox quantum theory: actual configurations.

The rest of this section will discuss the significance of quantum observables for Bohmian mechanics. (It follows from what has been said in the three preceding paragraphs that what we conclude here about quantum observables for Bohmian mechanics holds for orthodox quantum theory as well.)

Bohmian mechanics yields a natural association between experiments and so-called *generalized observables*, given by positive-operator-valued measures (Davies 1976)[^davies-1976], or POVMs, $O(dz)$, on the value spaces for the results of the experiments (Berndl, Daumer, et al. 1995)[^berndl-1995][^berndl-1995-2]. This association is such that the probability distribution of the result $Z$ of an experiment, when performed upon a system with wave function *ψ*, is given by $\langle \psi | O(dz)\psi \rangle$ (where $\langle\, \cdot\, |\, \cdot \, \rangle$ is the usual inner product between quantum state vectors).

Moreover, this conclusion follows immediately from the very meaning of an experiment from a Bohmian perspective: a coupling of system to apparatus leading to a result $Z$ that is a function of the final configuration of the total system, e.g., the orientation of a pointer. Analyzed in Bohmian mechanical terms, the experiment defines a map from the initial wave function of the system to the distribution of the result. It follows directly from the structure of Bohmian mechanics, and from the fact that the quantum equilibrium distribution is quadratic in the wave function, that this map is bilinear (or, more precisely, sesquilinear, in that its dependence on one factor of the wave function is antilinear, involving complex conjugation, rather than linear). Such a map is equivalent to a POVM.

The simplest example of a POVM is a standard quantum observable, corresponding to a self-adjoint operator $A$ on the Hilbert space of quantum state vectors (i.e., wave functions). For Bohmian mechanics, more or less every “measurement-like” experiment is associated with this special kind of POVM. The familiar quantum measurement axiom that the distribution of the result of the “measurement of the observable $A$” is given by the *spectral measure* for $A$ relative to the wave function (in the very simplest cases just the absolute squares of the so-called *probability amplitudes*) is thus obtained.

For various reasons, after the discovery of quantum mechanics it quickly became almost universal to speak of an experiment associated with an operator $A$ in the manner just sketched as a *measurement* of the *observable* $A$—as if the operator somehow corresponded to a property of the system that the experiment in some sense measures. It has been argued that this assumption, which has been called *naive realism about operators*, has been a source of considerable confusion about the meaning and implications of quantum theory (Daumer et al. 1997a)[^daumer-1997a]. Against this misuse of the word “measurement”, Bell wrote the following:

> A second charge is that the word comes loaded with meaning from everyday life, meaning which is entirely inappropriate in the quantum context. When it is said that something is “measured” it is difficult not to think of the result as referring to some preexisting property of the object in question. This is to disregard Bohr's insistence that in quantum phenomena the apparatus as well as the system is essentially involved. If it were not so, how could we understand, for example, that “measurement” of a component of “angular momentum”… in an arbitrarily chosen direction … yields one of a discrete set of values? When one forgets the role of the apparatus, as the word “measurement” makes all too likely, one despairs of ordinary logic … hence “quantum logic”. When one remembers the role of the apparatus, ordinary logic is just fine.
>
> In other contexts, physicists have been able to take words from ordinary language and use them as technical terms with no great harm done. Take for example the “strangeness”, “charm”, and “beauty” of elementary particle physics. No one is taken in by this “baby talk”. … Would that it were so with “measurement”. But in fact the word has had such a damaging effect on the discussion, that I think it should now be banned altogether in quantum mechanics. (Bell 1990, reprinted 1987c: 216)[^bell-1987c][^bell-1990]

## 11. Spin

The case of spin illustrates nicely both the way Bohmian mechanics treats non-configurational quantum observables, and some of the difficulties that the naive realism about operators mentioned above causes.

Spin is the canonical quantum observable that has no classical counterpart, reputedly impossible to grasp in a nonquantum way. The difficulty is not quite that spin is quantized in the sense that its allowable values form a discrete set (for a spin-1/2 particle, $\pm \hslash/2$). Energy too may be quantized in this sense. Nor is it precisely that the components of spin in the different directions fail to commute—and so cannot be simultaneously discussed, measured, imagined, or whatever it is that we are advised not to do with noncommuting observables. Rather the problem is that there is no ordinary (nonquantum) quantity which, like the spin observable, is a 3-vector and which also is such that its components in all possible directions belong to the same discrete set. The problem, in other words, is that the usual vector relationships among the various components of the spin vector are incompatible with the quantization conditions on the values of these components.

For a particle of spin-1 the problem is even more severe. The components of spin in different directions aren’t simultaneously measurable. Thus, the impossible vector relationships for the spin components of a quantum particle are not observable. But those of their squares are. Bell (1966)[^bell-1966], and, independently, Simon Kochen and Ernst Specker (1967) showed that for a spin-1 particle the squares of the spin components in the various directions satisfy, according to quantum theory, a collection of relationships, each individually observable, that taken together are impossible: the relationships are incompatible with the idea that measurements of these observables merely reveal their preexisting values rather than creating them, as quantum theory urges us to believe. Many physicists and philosophers of physics continue to regard the Kochen-Specker Theorem as precluding the possibility of hidden variables.

We thus might naturally wonder how Bohmian mechanics copes with spin. But we have already answered this question. Bohmian mechanics makes sense for particles with spin, i.e., for particles whose wave functions are spinor-valued. When such particles are suitably directed toward Stern-Gerlach magnets, they emerge moving in more or less a discrete set of directions—2 possible directions for a spin-1/2 particle, having 2 spin components, 3 for spin-1 with 3 spin components, and so on. This occurs because the Stern-Gerlach magnets are so designed and oriented that a wave packet (a localized wave function with reasonably well defined velocity) directed towards the magnet will, by virtue of the Schrödinger evolution, separate into distinct packets—corresponding to the spin components of the wave function and moving in the discrete set of directions. The particle itself, depending upon its initial position, ends up in one of the packets moving in one of the directions.

The probability distribution for the result of such a *Stern-Gerlach experiment* can be conveniently expressed in terms of the quantum mechanical spin operators—for a spin-1/2 particle given by certain 2 by 2 matrices called the Pauli spin matrices—in the manner alluded to above. From a Bohmian perspective there is no paradox in any of this—unless we assume that the spin operators correspond to genuine properties of the particles. As to what has often been called the Kochen-Specker paradox described above, this points to the issue of contextuality.

For further discussion and more detailed examples of the Bohmian perspective on spin, see Norsen 2014.

## 12. Contextuality

The Kochen-Specker Theorem, the earlier theorem of Gleason (Gleason 1957 and Bell 1966)[^bell-1966][^gleason-1957], and other no-hidden-variables results, including Bell’s inequality (Bell 1964)[^bell-1964], show that any hidden-variables formulation of quantum mechanics must be *contextual*. It must violate the noncontextuality assumption “that measurement of an observable must yield the same value independently of what other measurements may be made simultaneously” (1964, reprinted 1987c: 9). To many physicists and philosophers of science contextuality seems too great a price to pay for the rather modest benefits—largely psychological, so they would say—that hidden variables provide.

Even many Bohmians suggest that contextuality departs significantly from classical principles. For example, Bohm and Hiley write that

> The context dependence of results of measurements is a further indication of how our interpretation does not imply a simple return to the basic principles of classical physics. (1993: 100)

However, to understand contextuality in Bohmian mechanics almost nothing needs to be explained. Consider an operator $A$ that commutes with operators $B$ and $C$ (which however don’t commute with each other). What is often called the “result for $A$” in an experiment for “measuring $A$ together with $B$” usually disagrees with the “result for $A$” in an experiment for “measuring $A$ together with $C$”. This is because these experiments differ and different experiments usually have different results. The misleading reference to measurement, which suggests that a pre-existing value of $A$ is being revealed, makes contextuality seem more than it is.

Seen properly, contextuality amounts to little more than the rather unremarkable observation that results of experiments should depend upon how they are performed, even when the experiments are associated with the same operator in the manner alluded to above. David Albert (1992: 153)[^albert-1992] has given a particularly simple and striking example of this dependence for Stern-Gerlach experiments “measuring” the $z$-component of spin. Reversing the polarity in a magnet for “measuring” the $z$-component of spin while keeping the same geometry yields another magnet for “measuring” the $z$-component of spin. The use of one or the other of these two magnets will often lead to opposite conclusions about the “value of the $z$-component of spin” prior to the “measurement” (for the same initial value of the position of the particle).

As Bell insists:

> A final moral concerns terminology. Why did such serious people take so seriously axioms which now seem so arbitrary? I suspect that they were misled by the pernicious misuse of the word “measurement” in contemporary theory. This word very strongly suggests the ascertaining of some preexisting property of some thing, any instrument involved playing a purely passive role. Quantum experiments are just not like that, as we learned especially from Bohr. The results have to be regarded as the joint product of “system” and “apparatus”, the complete experimental set-up. But the misuse of the word “measurement” makes it easy to forget this and then to expect that the “results of measurements” should obey some simple logic in which the apparatus is not mentioned. The resulting difficulties soon show that any such logic is not ordinary logic. It is my impression that the whole vast subject of “Quantum Logic” has arisen in this way from the misuse of a word. I am convinced that the word “measurement” has now been so abused that the field would be significantly advanced by banning its use altogether, in favour for example of the word “experiment”. (Bell 1982, reprinted 1987c: 166)[^bell-1982][^bell-1987c]

## 13. Nonlocality

Bohmian mechanics is manifestly nonlocal. The velocity, as expressed in the guiding equation, of any particle of a many-particle system will typically depend upon the positions of the other, possibly distant, particles whenever the wave function of the system is entangled, i.e., not a product of single-particle wave functions. This is true, for example, for the EPR-Bohm wave function, describing a pair of spin-1/2 particles in the singlet state, that Bell and many others analyzed. Thus Bohmian mechanics makes explicit the most dramatic feature of quantum theory: quantum nonlocality, as discussed in Section 2.

It should be emphasized that the nonlocality of Bohmian mechanics derives solely from the nonlocality, discussed in Section 2, built into the structure of standard quantum theory. This nonlocality originates from a wave function on configuration space, an abstraction which, roughly speaking, combines—or binds—distant particles into a single irreducible reality. As Bell has stressed,

> That the guiding wave, in the general case, propagates not in ordinary three-space but in a multidimensional-configuration space is the origin of the notorious “nonlocality” of quantum mechanics. It is a merit of the de Broglie-Bohm version to bring this out so explicitly that it cannot be ignored. (Bell 1980, reprinted 1987c: 115)[^bell-1980][^bell-1987c]

Thus the nonlocal velocity relation in the guiding equation is but one aspect of the nonlocality of Bohmian mechanics. There is also the nonlocality, or nonseparability, implicit in the wave function itself, which is present even without the structure—actual configurations—that Bohmian mechanics adds to orthodox quantum theory. And, as Bell has shown, using the connection between the wave function and the predictions of quantum theory about experimental results, the elimination of this nonlocality, if possible at all, is extremely difficult—since eliminating the wave function does not eliminate those results (see Section 2).

The nonlocality of Bohmian mechanics can be appreciated perhaps most efficiently, in all its aspects, by focusing on the conditional wave function. Suppose, for example, that in an EPR-Bohm experiment particle 1 passes through its Stern-Gerlach magnet before particle 2 arrives at its magnet. Then the orientation of the Stern-Gerlach magnet for particle 1 will significantly affect the conditional wave function of particle 2: If the Stern-Gerlach magnet for particle 1 is oriented so as to “measure the $z$-component of spin”, then after particle 1 has passed through its magnet the conditional wave function of particle 2 will be an eigenvector (or eigenstate) of the $z$-component of spin (in fact, belonging to the eigenvalue that is the negative of the one “measured” for particle 1), and the same thing is true for any other component of spin. You can dictate the *kind* of spin eigenstate produced for particle 2 by appropriately choosing the orientation of an arbitrarily distant magnet. As to the future behavior of particle 2, in particular how its magnet affects it, this of course depends very much on the character of its conditional wave function; hence the choice of orientation of the distant magnet strongly influences that behavior.

This nonlocal effect upon the conditional wave function of particle 2 follows from combining the standard analysis of the evolution of the wave function in the EPR-Bohm experiment with the definition of the conditional wave function. (For simplicity, we ignore permutation symmetry.) Before reaching any magnets the EPR-Bohm wave function is a sum of two terms, corresponding to nonvanishing values for two of the four possible joint spin components for the two particles. Each term is a product of an eigenstate for a component of spin in a given direction for particle 1 with the opposite eigenstate (i.e., belonging to the eigenvalue that is the negative of the eigenvalue for particle 1) for the component of spin in the same direction for particle 2. Moreover, by virtue of its symmetry under rotations, the EPR-Bohm wave function has the property that any component of spin, i.e., any direction, can be used in this decomposition.

Decomposing the EPR-Bohm wave function using the component of spin in the direction associated with the magnet for particle 1, the evolution of the wave function as particle 1 passes its magnet is easily grasped: The evolution of the sum is determined (using the linearity of Schrödinger’s equation) by that of its individual terms, and the evolution of each term by that of each of its factors. The evolution of the particle-1 factor leads to a displacement along the magnetic axis in the direction determined by the (sign of the) spin component (i.e., the eigenvalue), as described in the fourth paragraph of Section 11. Once this displacement has occurred (and is large enough) the conditional wave function for particle 2 will correspond to the term in the sum selected by the actual position of particle 1. In particular, it will be an eigenstate of the component of spin “measured by” the magnet for particle 1. (For a more explicit and detailed discussion, see Norsen 2014.)[^norsen-2014]

The nonlocality of Bohmian mechanics has a remarkable feature: it is screened by quantum equilibrium. It is a consequence of the quantum equilibrium hypothesis that the nonlocal effects in Bohmian mechanics don’t yield observable consequences that can be controlled—we can’t use them to send instantaneous messages. This follows from the fact that, given the quantum equilibrium hypothesis, the observable consequences of Bohmian mechanics are the same as those of orthodox quantum theory, for which instantaneous communication based on quantum nonlocality is impossible (see Eberhard 1978)[^eberhard-1978]. Valentini (1991)[^valentini-1991] emphasizes the importance of quantum equilibrium for obscuring the nonlocality of Bohmian mechanics. (Valentini [2010a] has also suggested the possibility of searching for and exploiting quantum non-equilibrium. However, in contrast with thermodynamic non-equilibrium, we have at present no idea what quantum non-equilibrium, should it exist, would look like, despite claims and arguments to the contrary.)

## 14. Lorentz Invariance

Like nonrelativistic quantum theory, of which it is a version, Bohmian mechanics is not compatible with special relativity, a central principle of physics: Bohmian mechanics is not Lorentz invariant. Nor can it easily be modified to accommodate Lorentz invariance. Configurations, defined by the *simultaneous* positions of all particles, play too crucial a role in its formulation, with the guiding equation defining an evolution on *configuration* space. (Lorentz invariant extensions of Bohmian mechanics for a single particle, described by the Dirac equation (Bohm & Hiley 1993; Dürr et al. 1999)[^bohm-1993][^dürr-1999] or the Klein-Gordon equation (Berndl et al. 1996; Nikolic 2005)[^berndl-1996][^nikolic-2005], can easily be achieved, though for a Klein-Gordon particle there are some interesting subtleties, corresponding to what might seem to be a particle traveling backwards in time.)

This difficulty with Lorentz invariance and the nonlocality in Bohmian mechanics are closely related. Since quantum theory itself, by virtue merely of the character of its predictions concerning EPR-Bohm correlations, is irreducibly nonlocal (see Section 2), one might expect considerable difficulty with the Lorentz invariance of orthodox quantum theory as well with Bohmian mechanics. For example, the collapse rule of textbook quantum theory blatantly violates Lorentz invariance. As a matter of fact, the intrinsic nonlocality of quantum theory presents formidable difficulties for the development of any (many-particle) Lorentz invariant formulation that avoids the vagueness of orthodox quantum theory (see Maudlin 1994)[^maudlin-1994].

Bell made a somewhat surprising evaluation of the importance of the problem of Lorentz invariance. In an interview with the philosopher Renée Weber, not long before he died, he referred to the paradoxes of quantum mechanics and observed that

> Those paradoxes are simply disposed of by the 1952 theory of Bohm, leaving as *the* question, the question of Lorentz invariance. So one of my missions in life is to get people to see that if they want to talk about the problems of quantum mechanics—the real problems of quantum mechanics—they must be talking about Lorentz invariance. (Interview with John Bell, in Weber 1989 [Other Internet Resources])[^bell-1989]

The most common view on this issue is that a detailed description of microscopic quantum processes, such as would be provided by a putative extension of Bohmian mechanics to the relativistic domain, must violate Lorentz invariance. In this view Lorentz invariance in such a theory would be an emergent symmetry obeyed by our observations—for Bohmian mechanics a statistical consequence of quantum equilibrium that governs the results of quantum experiments. This is the opinion of Bohm and Hiley (1993), of Holland (1993)[^holland-1993], and of Valentini (1997)[^valentini-1997].

However—unlike nonlocality—violating Lorentz invariance is not inevitable. It should be possible, it seems, to construct a fully Lorentz invariant theory that provides a detailed description of microscopic quantum processes. One way to do this is by using an additional Lorentz invariant dynamical structure, for example a suitable time-like 4-vector field, that permits the definition of a foliation of space-time into space-like hypersurfaces providing a Lorentz invariant notion of “evolving configuration” and along which nonlocal effects are transmitted. See Dürr et al. 1999 for a toy model. Another possibility is that a fully Lorentz invariant account of quantum nonlocality can be achieved without the invocation of additional structure, exploiting only what is already at hand, for example, the wave function of the universe or light-cone structure. For more on the latter possibility, see Goldstein and Tumulka’s model (2003), in which they reconcile relativity and nonlocality through the interplay of opposite arrows of time. For a discussion of the former possibility, see Dürr et al. 2014. In the sort of theory discussed there, the wave function of the universe provides a covariant prescription for the desired foliation. Such a theory would be clearly Lorentz invariant. But, as suggested there, it is not so clear that it should be regarded as relativistic, a notion with connotations that arguably transcend Lorentz invariance.

Be that as it may, Lorentz invariant nonlocality involves extremely subtle issues and remains somewhat enigmatic. For example, Bell rightly would find

> disturbing … the impossibility of “messages” faster than light, which follows from ordinary relativistic quantum mechanics in so far as it is unambiguous and adequate for procedures $we$ [emphasis added] can actually perform. The exact elucidation of concepts like “message” and “we”, would be a formidable challenge. (1981a, reprinted 1987c: 155)

While quantum equilibrium and the absolute uncertainty that it entails (Dürr, Goldstein, & Zanghì 1992a)[^dürr-1992a] may be of some help here, the situation remains puzzling.

## 15. Identical Particles

Fundamental particles of the same kind, for example electrons, are treated in quantum mechanics as if they are somehow identical or indistinguishable. This treatment is reflected in the symmetry properties of the wave function of a many-particle system under permutations of the coordinates of those particles. For electrons, and for other *fermions*, the wave function must change its sign when the coordinates of a pair of particles are exchanged; it must be *antisymmetric*. For photons and other *bosons* it must be symmetric, with no change at all.

The justification usually given for this is that the only way to keep track of the individual particles and thereby retain their individuality is by following their trajectories, which of course one cannot and must not do, and in any case does not have, in standard quantum mechanics. (Like so many arguments used to justify various claims in quantum mechanics, this sort of argument, with its positivistic slant, is rather weak. Its conclusion, however, is quite solid.) On this basis one often hears it maintained that Bohmian mechanics, because its particles have trajectories (deterministic ones to boot), is unable to deal with identical particles.

There is, however, no problem whatsoever in incorporating bosons and fermions into Bohmian mechanics. One simply stipulates that the wave function in Bohmian mechanics has the same symmetry properties under permutations as in standard quantum mechanics. Once again, in Bohmian mechanics one does not change the wave function or its evolution equation; one merely adds to it the actual configuration of the particles and its guiding equation.

In fact, by taking the configuration seriously in Bohmian mechanics, one perhaps arrives even more naturally than in standard quantum mechanics at the classification of fundamental quantum particles as bosons and fermions, with wave functions of the appropriate symmetries. That’s because the natural configuration space for a system of $N$ particles, say electrons, all described by the same dynamical parameters such as charge, consists of $N$-point subsets of physical space, and not $N$-tuples of points in physical space. It is natural, in other words, to regard the labelling we assign to particles as an unphysical convenience, and to use on the fundamental level unlabelled configurations rather than labelled ones. Wave functions on this natural configuration space are in effect symmetric, trivially so.

Moreover the natural configuration space has a non-trivial topology. (To see this, consider a closed path in this space along which a pair of points in a configuration in the path is exchanged in proceeding along the path from the configuration back to itself.) When this is taken into account the possibility of antisymmetric wave functions, of fermions, naturally emerges. (Dürr et al. 2006, following Nelson 1985 for stochastic mechanics. For a similar early analysis that is more traditionally quantum, see Leinaas and Myrheim 1977.)[^dürr-2006][^nelson-1985]

## 16. Quantum Motion on Shape Space

A natural thought that one sometimes hears expressed is that Bohmian mechanics, for which particles with well-defined positions in space play a central role, cannot easily accommodate a relational framework, as most prominently advocated by Julian Barbour (1999)[^barbour-1999]. With such a framework, location in space is not a fundamental physical notion. Rather it is shapes formed by arrangements of particles, shapes determined by relative positions, that are physical.

Bohmian mechanics can naturally be extended to a relational framework, which also leads to a relational notion of time as well. Within this framework, the more familiar descriptions and laws, classical or quantum, in terms of absolute space and time emerge merely as corresponding to a choice of gauge (Dürr et al. 2020a)[^dürr-2020a]. Thus, rather than being a regression to outdated modes of physics, a Bohmian perspective suggests the possibility that much of what we regard as fundamental in physics might in fact be imposed by us, through our choice of gauge. (See also Goldstein and Zanghì 2022.)[^goldstein-2022]

## 17. Objections, Responses, and Comments

Bohmian mechanics has never been widely accepted by physicists. Since it is not part of the standard physics curriculum, many physicists—probably the majority—are simply unfamiliar with the theory and how it works. Sometimes the theory is rejected without explicit discussion of reasons for rejection. One also finds objections that are based on simple misunderstandings; among these are claims that some no-go theorem, such as von Neumann’s theorem, the Kochen-Specker theorem, or Bell’s theorem, shows that the theory cannot work. Such objections will not be dealt with here, as the reply to them will be obvious to those who understand the theory. In what follows only objections that are not based on elementary misunderstandings will be discussed.

A common objection is that Bohmian mechanics is too complicated or inelegant. To evaluate this objection one must compare the axioms of Bohmian mechanics with those of standard quantum mechanics. To Schrödinger’s equation, Bohmian mechanics adds the guiding equation; standard quantum mechanics adds instead postulates about experimental outcomes. These postulates can be formulated only in terms of a fundamental distinction between a quantum system and the experimental apparatus. And, as noted by Hilary Putnam,

> In Putnam ([1965]), I rejected Bohm’s interpretation for several reasons which no longer seem good to me. Even today, if you look at the Wikipedia encyclopedia on the Web, you will find it said that Bohm’s theory is mathematically inelegant. Happily, I did not give *that* reason in Putnam ([1965]), but in any case it is not true. The formula for the velocity field is extremely simple: you have the probability current in the theory anyway, and you take the velocity vector to be proportional to the current. There is nothing particularly inelegant about that; if anything, it is remarkably elegant! (2005: 262)

One frequent objection is that Bohmian mechanics, since it makes precisely the same predictions as standard quantum mechanics (insofar as the predictions of standard quantum mechanics are unambiguous), is not a distinct theory but merely a reformulation of standard quantum theory. In this vein, Heisenberg wrote,

> Bohm’s interpretation cannot be refuted by experiment, and this is true of all the counter-proposals in the first group. From the fundamentally “positivistic” (it would perhaps be better to say “purely physical”) standpoint, we are thus concerned not with counter-proposals to the Copenhagen interpretation, but with its exact repetition in a different language. (Heisenberg 1955: 18)[^heisenberg-1955]

More recently, Sir Anthony Leggett has echoed this charge. Referring to the measurement problem, he says that Bohmian mechanics provides “little more than verbal window dressing of the basic paradox” (Leggett 2005: 871)[^leggett-2005]. And in connection with the double-slit experiment, he writes,

> No experimental consequences are drawn from [the assumption of definite particle trajectories] other than the standard predictions of the QM formalism, so whether one regards it as a substantive resolution of the apparent paradox or as little more than a reformulation of it is no doubt a matter of personal taste (the present author inclines towards the latter point of view). (Leggett 2002: R419)[^leggett-2002]

Now Bohmian mechanics and standard quantum mechanics provide clearly different descriptions of what is happening on the microscopic level. So it is only with a purely instrumental attitude towards scientific theories that Bohmian mechanics and standard quantum mechanics can possibly be regarded as different formulations of exactly the same theory. But even if they were, why would this be an objection to Bohmian mechanics? Even if they were, we should still ask which of the two formulations is superior. Those impressed by the “not-a-distinct-theory” objection presumably give considerable weight to the fact that standard quantum mechanics came first. Supporters of Bohmian mechanics give more weight to its greater simplicity and clarity.

The position of Leggett, however, is very difficult to understand. There should be no measurement problem for a physicist with a purely instrumentalist understanding of quantum mechanics. But for more than thirty years Leggett has forcefully argued that quantum mechanics indeed suffers from the measurement problem. For Leggett the problem is so serious that it has led him to suggest that quantum mechanics might fail on the macroscopic level. So Leggett is no instrumentalist. Thus it is hard to understand why he so cavalierly dismisses a theory like Bohmian mechanics that obviously doesn’t suffer from the measurement problem, with which he has been so long concerned.

Sir Roger Penrose also seems to have doubts as to whether Bohmian mechanics indeed resolves the measurement problem. He writes that

> it seems to me that some measure of scale is indeed needed, for defining when classical-like behaviour begins to take over from small-scale quantum activity. In common with the other quantum ontologies in which no measurable deviations from standard quantum mechanics is expected, the point of view (e) [Bohmian mechanics] does not possess such a scale measure, so I do not see that it can adequately address the paradox of Schrödinger’s cat. (2005: 811)

But contrary to what he writes, his real concern seems to be with the emergence of classical behavior, and not with the measurement problem *per se*. With regard to this, we note that the Bohmian evolution of particles, which is always governed by the wave function and is always fundamentally quantum, turns out to be approximately classical when the relevant de Broglie wave length, determined in part by the wave function, is much smaller than the scale on which the potential energy term in Schrödinger’s equation varies (see Allori et al., 2002)[^allori-2002]. Under normal circumstances this condition will be satisfied for the motion of the center of mass of a macroscopic object.

It is perhaps worth mentioning that despite the empirical equivalence between Bohmian mechanics and orthodox quantum theory, there are a variety of experiments and experimental issues that don’t fit comfortably within the standard quantum formalism but are easily handled by Bohmian mechanics. Among these are dwell and tunneling times (Leavens 1996)[^leavens-1996], escape or arrival times and positions (Daumer et al. 1997b)[^daumer-1997b], scattering theory (Dürr et al., 2000)[^dürr-2000], and quantum chaos (Cushing 1994; Dürr, Goldstein, & Zanghì 1992b)[^cushing-1994][^dürr-1992b]. Moreover, the additional resources present in Bohmian mechanics, in particular the notion of the conditional wave function defined in Section 8, have been useful for the development of approximation schemes for dealing with practical quantum applications (Oriols & Mompart 2012, Struyve 2020)[^oriols-2012][^struyve-2020].

With regard to quantities, such as arrival times, that are problematical within orthodox quantum theory but are obviously well defined in Bohmian mechanics, a word of caution should be noted: the fact that a quantity is meaningful does not necessarily imply that a procedure widely regarded as measuring that quantity does so. There may in fact be no procedure that genuinely measures the quantity. A very nice example of this has recently been provided by Das & Dürr 2019. They compute the distribution of the time of arrival at a surface for a spin-1/2 particle moving in a wave guide. (For the motion of the particle they assume a guiding equation that differs from the usual one, given in Section 4, by the addition of an explicitly spin dependent term—see equations (5) and (6) of Goldstein et al. 2024b—that arises in the non-relativistic limit of the Dirac equation.) They find that the arrival time distribution depends on the spin state of the particle, and in a manner that, as shown in Goldstein et al. 2024a and 2024b, is incompatible with the distribution arising from a POVM, see Section 10. Thus no experiment can, for every spin state, measure the arrival time.

Especially problematical from an orthodox perspective is quantum cosmology, for which the relevant quantum system is the entire universe, so that there is no observer outside the system to cause collapse of the wave function upon measurement. This is not a problem from a Bohmian perspective since in Bohmian mechanics (conditional) wave functions collapse as appropiate—see Section 8. Moreover, in this setting Bohmian models have clarified the issue of the inevitability of the presence of singularities in theories of quantum gravity (Falciano, Pinto-Neto, & Struyve 2015)[^falciano-2015]. For a discussion of how a Bohmian perspective can eliminate some conceptual difficulties arising in quantum gravity, such as the problem of time and the problem of the absence of sufficiently many diffeomorphism-invariant observables, as discussed for example by Kuchař 1992, see Goldstein & Teufel 2001.

Another claim that has become popular in recent years is that Bohmian mechanics is an Everettian, or “many worlds”, interpretation in disguise (see entry on the many worlds interpretation of quantum mechanics for an overview of such interpretations). The idea is that Bohmians, like Everettians, must take the wave-function as physically real. Moreover, since Bohmian mechanics involves no wave-function collapse (for the wave function of the universe), all of the branches of the wave function, and not just the one that happens to be occupied by the actual particle configuration, persist. Everettians regard (at least some of) these branches as representing parallel worlds. As David Deutsch, referring to the branches, expresses the charge,

> the “unoccupied grooves” must be physically real. Moreover they obey the same laws of physics as the “occupied groove” that is supposed to be “the” universe. But that is just another way of saying that they are universes too. … In short, pilot-wave theories are parallel-universes theories in a state of chronic denial. (Deutsch 1996: 225)[^deutsch-1996]

See Brown and Wallace (2005) for an extended version of this argument. Not surprisingly, Bohmians do not agree that the branches of the wave function should be construed as representing worlds. For one Bohmian response, see Maudlin (2010)[^maudlin-2010]. Other Bohmian responses have been given by Lewis (2007)[^lewis-2007] and Valentini (2010b)[^valentini-2010b].

One's reaction to the claim of Deutsch, Brown, and Wallace depends in part on one's attitude towards the power of the kind of analysis employed for mind-body functionalism, of structure and patterns, as in the work of Daniel Dennett. On the one hand, for anyone who, like Wallace, accepts the viability of a functionalist many-worlds understanding of quantum mechanics—and in particular accepts that it follows as a matter of functional and structural analysis that when the wave function develops suitable complex patterns these ipso facto describe what we should regard as worlds—the claim should be compelling. On the other hand, for those who reject the functional analysis and regard many worlds as ontologically inadequate (see Maudlin 2010)[^maudlin-2010], or who, like Vaidman (see the SEP entry on the many-worlds interpretation of quantum mechanics), accepts many worlds on non-functionalist grounds, the claim should seem, not merely wrong, but silly.

Another interesting aspect of the claim is this: It seems that one could consider, at least as a logical possibility, a world consisting of particles moving according to some well-defined equations of motion, and in particular according to the equations of Bohmian mechanics. It seems entirely implausible that there should be a logical problem with doing so. Thus the claim of Deutsch, Brown, and Wallace, suggesting that there is, should perhaps be regarded, not as an argument in favor of many worlds, but as a reductio ad absurdum against it.

There is one striking feature of Bohmian mechanics that is often presented as an objection: in Bohmian mechanics the wave function acts upon (the positions of) the particles but the particles don't act back upon the wave function, since it autonomously evolves via Schrödinger’s equation. This is regarded by some Bohmians, not as an objection to the theory, but as an important clue to the meaning of the quantum-mechanical wave function. Discussing this point Dürr, Goldstein, & Zanghì (1997) and Goldstein & Teufel (2001) suggest that from a deeper perspective than afforded by standard Bohmian mechanics or quantum theory, the wave function of the universe should be regarded as nomological, as an object for conveniently expressing a law of motion somewhat analogous to the Hamiltonian in classical mechanics. A time-dependent Schrödinger-type equation, from this deeper (cosmological) perspective, is merely phenomenological.

Bohmian mechanics does not account for phenomena such as particle creation and annihilation characteristic of quantum field theory. This is not an objection to Bohmian mechanics but merely a recognition that quantum field theory explains a great deal more than does nonrelativistic quantum mechanics, whether in orthodox or Bohmian form. It does, however, underline the need to find an adequate, if not compelling, Bohmian version of quantum field theory, and of quantum gauge theories in particular. Some rather tentative steps in this direction can be found in Bohm & Hiley 1993, Holland 1993, Bell 1987b), and in some of the articles in Cushing, Fine, & Goldstein 1996.

A crucial issue is whether quantum field theory is fundamentally about fields or particles—or something else entirely. The choice of “fields” (see Struyve 2010 for an assessment of a variety of possibilities)[^struyve-2010] is of course suggested by the name. For most, including Bell, the preferred choice is particles. Bell’s proposal is in fact the basis of a canonical extension of Bohmian mechanics to general quantum field theories, and these “Bell-type quantum field theories” (Dürr et al. 2004 and 2005)[^dürr-2004][^dürr-2005] describe a stochastic evolution of particles that involves particle creation and annihilation. (Inspired by the structure of Bell-type quantum field theories, Tumulka has developed a novel approach to the problem of the ultraviolet divergences of quantum field theory based on what he calls *interior boundary conditions*. See D. Dürr et al. 2020b and the references therein.)[^dürr-2020b] For a general discussion of the possibility of a Bohmian quantum field theory—and of the point and value of Bohmian mechanics more generally—see the exchange of letters between Goldstein and Weinberg by following the link provided in the Other Internet Resources section below.

## 18. Summary and Comparisons

Bohmian mechanics is a version of quantum mechanics that describes the motion of particles. It is far simpler than the standard textbook version of the theory: it replaces the measurement postulates of the latter with a simple, and arguably rather obvious, guiding equation. For textbook quantum mechanics the role of the wave function is on the macroscopic level, of measurement and observation. For Bohmian mechanics it is on the fundamental microscopic level. For textbook quantum mechanics, rules governing measurement and observation play a fundamental role. For Bohmian mechanics those rules are derived. For textbook quantum mechanics, collapse is a postulate. For Bohmian mechanics it is a theorem.

For Bohmian mechanics the wave function is something but not everything. For Everett's many worlds theory it is everything. And for textbook quantum mechanics it also is often suggested that the wave function is everything, for example when the state of a quantum system is declared to be given by its wave function. It is also often suggested, with respect to textbook quantum mechanics, that the wave function is nothing, for example when it is said that it is merely a probability amplitude or that it just represents our information. But advocates of Bohmian mechanics hold that the most reasonable view in this regard is that, like for Bohmian mechanics, for textbook quantum mechanics the wave function is indeed something but not everything, since for that theory there must be macroscopic variables transcending the wave function, at least for describing measurement results.

Bohmian mechanics and Everett's many worlds theory both posit simple fundamental laws, but whereas for Everett explaining the real existence of familiar material objects in 3D remains an extraordinary challenge, Bohmian mechanics provides a trivially clear picture: tables, chairs, people, and planets are made of particles moving in ordinary physical space.

For a brief introduction to Bohmian mechanics see Tumulka 2021. For longer accessible presentations see Bricmont 2016, Norsen 2017, Bricmont 2018, Maudlin 2019, Dürr & Lazarovici 2020, and Tumulka 2022.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=qm-bohm). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/qm-bohm/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=qm-bohm&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/qm-bohm/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Weber, Renée, 1989, [Excerpts of an Interview with John Bell](http://www.math.rutgers.edu/~oldstein/bell-weber.html).
- [International Research Network on Bohmian Mechanics](http://www.mathematik.uni-muenchen.de/~bohmmech).
- [Exchange of letters between S. Goldstein and S. Weinberg](https://sites.math.rutgers.edu/~oldstein/papers/OnBohmianMechanics.pdf).
- [Videos of introductory lectures](http://www.mathematik.uni-muenchen.de/~bohmmech/videos.php).
- [Bohmian quantum mechanics in 4D](https://web.archive.org/web/20180427004106/http://astro-staff.uibk.ac.at/visworkshop2005/talks/sabinek.pdf) (in PDF), slides by Sabine Kreidl, from the 2nd High End Visualization Workshop, 2005.
- [The Mt. Rushmore of Quantum Foundations](https://sites.google.com/site/dlhquantum/educational/MtRush), at Foundations of Quantum (Douglas Hemmick).
- [Klaus von Bloh’s Bohmian mechanics demonstrations](http://demonstrations.wolfram.com/author.html?author=Klaus+von+Bloh).
- [Eric Dennis’ discussion e-group on Bell’s inequality and Bohmian mechanics](http://groups.yahoo.com/group/bell_bohm).
- [Exchange of letters on Quantum Theory Without Observers](http://www.math.rutgers.edu/~oldstein/papers/qtwoe/qtwoe.html), (reprinted from *Physics Today*, February 1999 [vol. 52, no. 2]).
- [The Little Quantum System, a video by Stefan Teufel dramatizing wave function collapse in Bohmian mechanics](https://tinyurl.com/3en2pym4).

## Related Entries

physics: holism and nonseparability | quantum mechanics | quantum mechanics: Copenhagen interpretation of | quantum mechanics: Kochen-Specker theorem | quantum mechanics: many-worlds interpretation of | quantum mechanics: modal interpretations of | quantum mechanics: the role of decoherence in | quantum theory: philosophical issues in | quantum theory: quantum entanglement and information | quantum theory: quantum gravity | quantum theory: quantum logic and probability theory | quantum theory: the Einstein-Podolsky-Rosen argument in | Uncertainty Principle

### Acknowledgments

I am grateful to Valia Allori, Jean Bricmont, Joanne Gowa, Dustin Lazarovici, Travis Norsen, Paul Oppenheimer, Ward Struyve, Stefan Teufel, Roderich Tumulka, Nino Zanghì and the subject editors, Guido Bacciagaluppi and Wayne Myrvold, for very careful readings and many valuable suggestions.

[^albert-1992]: Albert, David Z., 1992, *Quantum Mechanics and Experience*, Cambridge, MA: Harvard University Press.

[^allori-2015]: Allori, Valia, 2015, “Primitive Ontology in a Nutshell”, *International Journal of Quantum Foundations*, 1(3): 107–122.

[^allori-2002]: Allori, Valia, Detlef Dürr, Sheldon Goldstein, and Nino Zanghì, 2002, “Seven Steps Towards the Classical World”, *Journal of Optics B*, 4(4): 482–488. doi:10.1088/1464-4266/4/4/344 [[Allori et al. 2002 preprint available online](https://arxiv.org/abs/quant-ph/0112005)]

[^allori-2008]: Allori, Valia, Sheldon Goldstein, Roderich Tumulka, and Nino Zanghì, 2008, “On the Common Structure of Bohmian Mechanics and the Ghirardi-Rimini-Weber Theory”, *British Journal for the Philosophy of Science*, 59: 353–389. doi:10.1093/bjps/axn012 [[Allori et al. 2008 preprint available online](https://arxiv.org/abs/quant-ph/0603027)]

[^aspect-1982]: Aspect, Alain, Jean Dalibard, and Gérard Roger, 1982, “Experimental Test of Bell’s Inequalities Using Time-Varying Analyzers”, *Physical Review Letters*, 49(25): 1804–1807. doi:10.1103/PhysRevLett.49.1804

[^bacciagaluppi-2009]: Bacciagaluppi, Guido and Anthony Valentini, 2009, *Quantum Theory at the Crossroads: Reconsidering the 1927 Solvay Conference*, Cambridge: Cambridge University Press.

[^barbour-1999]: Barbour, Julian, 1999, *The End of Time*, Oxford: Oxford University Press.

[^becker-2018]: Becker, Adam, 2018, *What is Real?*, New York: Basic Books.

[^bell-1964]: Bell, John S., 1964, “On the Einstein-Podolsky-Rosen Paradox”, *Physics*, 1(3): 195–200. Reprinted in Bell 1987c: 14–21 and in Wheeler and Zurek 1983: 403–408.

[^bell-1966]: –––, 1966, “On the Problem of Hidden Variables in Quantum Theory”, *Reviews of Modern Physics*, 38(3): 447–452. doi:10.1103/RevModPhys.38.447 Reprinted in Bell 1987c: 1–13 and in Wheeler and Zurek 1983: 397–402.

[^bell-1980]: –––, 1980, “De Broglie-Bohm, Delayed-Choice Double-Slit Experiment, and Density Matrix”, *International Journal of Quantum Chemistry*, 18(S14): 155–159. 10.1002/qua.560180819 Reprinted in Bell 1987c: 111–116.

[^bell-1981a]: –––, 1981a, “Bertlmann’s Socks and the Nature of Reality”, *Journal de Physique Colloques*, 42(C2): 41–62. doi:10.1051/jphyscol:1981202 Reprinted in Bell 1987c: 139–158.

[^bell-1981b]: –––, 1981b, “Quantum Mechanics for Cosmologists”, in *Quantum Gravity 2: A Second Oxford Symposium*, C. Isham, Roger Penrose, D.W. Schiama (eds.), Oxford: Clarendon Press, pp. 611–637. Reprinted in Bell 1987c: 117–138.

[^bell-1982]: –––, 1982, “On the Impossible Pilot Wave”, *Foundations of Physics*, 12(10): 989–999. doi:10.1007/BF01889272 Reprinted in Bell 1987c: 159–168.

[^bell-1987a]: –––, 1987a, “Are There Quantum Jumps?”, *Schrödinger: Centenary of a Polymath*, Cambridge: Cambridge University Press, pp. 41–52. Reprinted in Bell 1987c: 201–212.

[^bell-1987b]: –––, 1987b, “Beables for Quantum Field Theory”, in *Quantum Implications: Essays in Honour of David Bohm*, Basil J. Hiley and F. David Peat, New York: Routledge & Kegan Paul in association with Methuen, pp. 227–234. Reprinted in Bell 1987c: 173–180.

[^bell-1987c]: –––, 1987c, *Speakable and Unspeakable in Quantum Mechanics,* SECOND EDITION, Cambridge: Cambridge University Press.

[^bell-1989]: –––, 1989, “Six Possible Worlds of Quantum Mechanics”, in *Possible Worlds in Humanities, Arts and Sciences: Proceedings of Noble Symposium 65*, Sture Allén (ed.), held August 11–15, 1986, Berlin: Walter de Gruyter, pp. 359–373. Reprinted in Bell 1987c: 181–195.

[^bell-1990]: –––, 1990, “Against ‘Measurement’”, in *Sixty-Two Years of Uncertainty: Historical, Philosophical, and Physical Inquiries into the Foundations of Quantum Mechanics (NATO Science Series B), Proceedings from the International School of History of Science*, Arthur I. Miller (ed.), convened at the Ettore Majorana Centre for Scientific Culture, Erice, Sicily, 5–15 August 1989, Cambridge: Cambridge University Press, pp. 17–32. Reprinted in Bell 1987c: 213–231.

[^beller-1999]: Beller, Mara, 1999, *Quantum Dialogue: The Making of a Revolution*, Chicago: University of Chicago Press.

[^berndl-1995]: Berndl, Karin, M. Daumer, Detlef Dürr, Sheldon Goldstein, and Nino Zanghì, 1995, “A Survey of Bohmian Mechanics”, *Il Nuovo Cimento B*, 110(5): 737–750. doi:10.1007/BF02741477 [[Berndl, Daumer et al. 1995 preprint available online](https://arxiv.org/abs/quant-ph/9504010)]

[^berndl-1995-2]: Berndl, Karin, Detlef Dürr, Sheldon Goldstein, G. Peruzzi, and Nino Zanghì, 1995, “On the Global Existence of Bohmian Mechanics”, *Communications in Mathematical Physics*, 173(3): 647–673. [[Berndl, Dürr et al. 1995 available online](http://projecteuclid.org/euclid.cmp/1104274916)]

[^berndl-1996]: Berndl, Karin, Detlef Dürr, Sheldon Goldstein, and Nino Zanghì, 1996, “Nonlocality, Lorentz Invariance, and Bohmian Quantum Theory”, *Physical Review A*, 53(4): 2062–2073. doi:10.1103/PhysRevA.53.2062 [[Berndl, Dürr et al. 1996 draft available online](https://arxiv.org/abs/quant-ph/9510027)]

[^bohm-1952]: Bohm, David, 1952, “A Suggested Interpretation of the Quantum Theory in Terms of ‘Hidden’ Variables, I and II”, *Physical Review*, 85(2): 166–193. doi:10.1103/PhysRev.85.166

[^bohm-1953]: –––, 1953, “Proof that Probability Density Approaches $\lvert\psi \rvert^2$ in Causal Interpretation of Quantum Theory”, *Physical Review*, 89(2): 458–466. doi:10.1103/PhysRev.89.458

[^bohm-1980]: –––, 1980, *Wholeness and the Implicate Order*, New York: Routledge.

[^bohm-1993]: Bohm, David and Basil J. Hiley, 1993, *The Undivided Universe: An Ontological Interpretation of Quantum Theory*, London: Routledge & Kegan Paul.

[^born-1926]: Born, Max, 1926, “Zur Quantenmechanik der Stoßvorgänge”, *Zeitschrift für Physik*, 37(12): 863–867. doi:10.1007/BF01397477 English translation “Quantum Mechanics of Collision Processes”, in Gunter Ludwig (ed.), 1968, *Wave Mechanics: Selected Readings in Physics*, Oxford: Pergamon Press: 206–225.

[^born-1949]: –––, 1949, *Natural Philosophy of Cause and Chance*, Oxford: Oxford University Press.

[^bricmont-2016]: Bricmont, Jean, 2016, *Making Sense of Quantum Mechanics*, Cham: Springer.

[^bricmont-2018]: –––, 2018, *Quantum Sense and Nonsense*, Cham: Springer.

[^bricmont-2020]: Bricmont, Jean, Sheldon Goldstein, and Doug Hemmick, 2020, “Schrödinger's Paradox and Proofs of Nonlocality Using Only Perfect Correlations”, *Journal of Statistical Physics*, 180: 74–91. [[Bricmont et al. 2020 available online](https://doi.org/10.1007/s10955-019-02361-w)]

[^bricmont-2022]: Bricmont, Jean, Sheldon Goldstein, and Doug Hemmick, 2022, “From EPR-Schrödinger Paradox to Nonlocality Based on Perfect Correlations”, *Foundations of Physics*, 52. [[Bricmont et al. 2022 preprint available online](http://arxiv.org/pdf/2005.00859)]

[^brown-2005]: Brown, Harvey R. and David Wallace, 2005, “Solving the Measurement Problem: De Broglie-Bohm loses out to Everett”, *Foundations of Physics*, 35(4): 517–540. doi:10.1007/s10701-004-2009-3

[^broglie-1928]: de Broglie, Louis, 1928, “La nouvelle dynamique des quanta”, in Solvay 1928, pp. 105–132.

[^bush-2015]: Bush, John W.M., 2015, “The New Wave of Pilot-wave Theory”, *Physics Today*, 68(8): 47–53. doi:10.1063/PT.3.2882

[^couder-2006]: Couder, Yves and Emmanuel Fort, 2006, “Single-Particle Diffraction and Interference at a Macroscopic Scale”, *Physical Review Letters*, 97: 154101. doi:10.1103/PhysRevLett.97.154101

[^cushing-1994]: Cushing, James T., 1994, *Quantum Mechanics: Historical Contingency and the Copenhagen Hegemony*, Chicago: University of Chicago Press.

[^cushing-1996]: Cushing, James T., Arthur Fine, and Sheldon Goldstein (eds), 1996, *Bohmian Mechanics and Quantum Theory: An Appraisal*, (Boston Studies in the Philosophy of Science, Volume 184), Boston: Kluwer Academic Publishers.

[^das-2019]: Das, Siddhant and Detlef Dürr, 2019, “Arrival Time Distributions of Spin-1/2 Particles”, *Scientific Reports*, 9: 2242. [[Das & Dürr 2019 available online](https://doi.org/10.1038/s41598-018-38261-4)]

[^daumer-1997a]: Daumer, Martin, Detlef Dürr, Sheldon Goldstein, and Nino Zanghì, 1997a, “Naive Realism About Operators”, *Erkenntnis*, 45(2): 379–397. doi:10.1007/BF00276801 [[Daumer et al. 1997a preprint available online](https://arxiv.org/abs/quant-ph/9601013)]

[^daumer-1997b]: –––, 1997b, “On the Quantum Probability Flux Through Surfaces”, *Journal of Statistical Physics*, 88(3): 967–977. doi:10.1023/B:JOSS.0000015181.86864.fb [[Daumer et al. 1997b preprint available online](https://arxiv.org/abs/quant-ph/9512016)]

[^davies-1976]: Davies, E.B., 1976, *Quantum Theory of Open Systems*, London: Academic Press.

[^deotto-1998]: Deotto, E. and G.C. Ghirardi, 1998, “Bohmian Mechanics Revisited”, *Foundations of Physics*, 28(1): 1–30. doi:10.1023/A:1018752202576

[^deutsch-1996]: Deutsch, David, 1996, “Comment on Lockwood”, *British Journal for the Philosophy of Science*, 47(2): 222–228. doi:10.1093/bjps/47.2.222

[^dürr-2009]: Dürr, Detlef and Stefan Teufel, 2009, *Bohmian Mechanics: The Physics and Mathematics of Quantum Theory*, Berlin: Springer-Verlag.

[^dürr-1992a]: Dürr, Detlef, Sheldon Goldstein, and Nino Zanghì, 1992a, “Quantum Equilibrium and the Origin of Absolute Uncertainty”, *Journal of Statistical Physics*, 67(5): 843–907. doi:10.1007/BF01049004 [[Dürr et al. 1992a preprint available online](https://arxiv.org/abs/quant-ph/0308039)]

[^dürr-1992b]: –––, 1992b, “Quantum Chaos, Classical Randomness, and Bohmian Mechanics”, *Journal of Statistical Physics*, 68(1): 259–270. doi:10.1007/BF01048845 [[Dürr et al. 1992b available (in Postscript) online](http://math.rutgers.edu/~oldstein/papers/qcbm.ps.gz)]

[^dürr-1997]: –––, 1997, “Bohmian Mechanics and the Meaning of the Wave Function”, in R.S. Cohen, M. Horne, and J. Stachel (eds), *Experimental Metaphysics—Quantum Mechanical Studies for Abner Shimony, Volume One*, (Boston Studies in the Philosophy of Science 193), Boston: Kluwer Academic Publishers. [[Dürr et al. 1997 preprint available online](https://arxiv.org/abs/quant-ph/9512031)]

[^dürr-2009-2]: –––, 2009, “On the Weak Measurement of Velocity in Bohmian Mechanics”, *Journal of Statistical Physics*, 134(5): 1023–1032. doi:10.1007/s10955-008-9674-0 [[Dürr et al. 2009 preprint available online](https://arxiv.org/abs/0808.3324)]

[^dürr-2020a]: –––, 2020a, “Quantum Motion on Shape Space and the Gauge Dependent Emergence of Dynamics and Probability in Absolute Space and Time”, *Journal of Statistical Physics*, 180: 92–134. doi:10.1007/s10955-019-02362-9 [[Dürr et al. 2020a preprint available online](https://arxiv.org/abs/1808.06844)]

[^dürr-1999]: Dürr, Detlef, Sheldon Goldstein, Karin Münch-Berndl, and Nino Zanghì, 1999, “Hypersurface Bohm-Dirac Models”, *Physical Review A*, 60(4): 2729–2736. doi:10.1103/PhysRevA.60.2729 [[Dürr et al. 1999 preprint available online](https://arxiv.org/abs/quant-ph/9801070)]

[^dürr-2014]: Dürr, Detlef, Sheldon Goldstein, Travis Norsen, Ward Struyve, and Nino Zanghì, 2014, “Can Bohmian Mechanics Be Made Relativistic?”, *Proceedings of The Royal Society A*, 470: 20130699. doi:10.1098/rspa.2013.0699 [[Dürr et al. 2014 preprint available online](https://arxiv.org/abs/1307.1714)]

[^dürr-2000]: Dürr, Detlef, Sheldon Goldstein, Stefan Teufel, and Nino Zanghì, 2000, “Scattering Theory from Microscopic First Principles”, *Physica A*, 279(1–4): 416–431. doi:10.1016/S0378-4371(99)00523-3

[^dürr-2004]: Dürr, Detlef, Sheldon Goldstein, Roderich Tumulka, and Nino Zanghì, 2004, “Bohmian Mechanics and Quantum Field Theory”, *Physical Review Letters*, 93(9): 1–4. doi:10.1103/PhysRevLett.93.090402 [[Dürr et al. 2004 preprint available online](https://arxiv.org/abs/quant-ph/0303156)]

[^dürr-2005]: –––, 2005, “Bell-Type Quantum Field Theories”, *Journal of Physics A: Mathematical and General*, 38(4): R1–R43. doi:10.1088/0305-4470/38/4/R01[[Dürr et al. 2005 preprint available online](https://arxiv.org/abs/quant-ph/0407116)]

[^dürr-2006]: Dürr, Detlef, Sheldon Goldstein, James Taylor, Roderich Tumulka, and Nino Zanghì, 2006, “Topological Factors Derived From Bohmian Mechanics”, *Annales Henri Poincaré*, 7: 791–807. [[Dürr et al. 2006 preprint available online](https://arxiv.org/abs/quant-ph/0601076)]

[^dürr-2020b]: Dürr, Detlef, Sheldon Goldstein, Stefan Teufel, Roderich Tumulka, and Nino Zanghì, 2020b, “Bohmian Trajectories for Hamiltonians with Interior-Boundary Conditions”, *Journal of Statistical Physics*, 180: 34–73. doi:10.1007/s10955-019-02335-y [[Dürr et al. 2020b preprint available online](https://arxiv.org/abs/1809.10235)]

[^dürr-2020]: Dürr, Detlef and Dustin Lazarovici, 2020, *Understanding Quantum Mechanics: The World According to Modern Quantum Foundations*, Cham: Springer. [[Dürr & Lazarovici 2020 available online](https://doi.org/10.1007/978-3-030-40068-2)]

[^dürr-2020-2]: Dürr, Detlef and Ward Struyve, 2020, “Typicality in the Foundations of Statistical Physics and Born’s rule”, in V.Allori, A. Bassi, D. Dürr and N. Zanghì (eds), *Do Wave Functions Jump? Perspectives of the Work of GianCarlo Ghirardi*, Cham: Springer, pp. 35–43. [[Dürr & Struyve 2020 preprint available online](https://arxiv.org/abs/1910.08049)]

[^eberhard-1978]: Eberhard, P.H., 1978, “Bell’s Theorem and the Different Concepts of Locality”, *Il Nuovo Cimento B*, 46(2): 392–419. doi:10.1007/BF02728628

[^einstein-1949]: Einstein, Albert, 1949, “Reply to Criticisms”, in *Albert Einstein, Philosopher-Scientist*, Paul Arthur Schilpp (ed.), Evanston, IL: Library of Living Philosophers, pp. 663–688.

[^einstein-1935]: Einstein, Albert, Boris Podolsky, and Nathan Rosen, 1935, “Can Quantum-Mechanical Description of Physical Reality be Considered Complete?”, *Physical Review*, 47(10): 777–780. doi:10.1103/PhysRev.47.777

[^everett-1957]: Everett, Hugh III, 1957, “‘Relative State’ Formulation of Quantum Mechanics”, *Reviews of Modern Physics*, 29(3): 454–462. doi:10.1103/RevModPhys.29.454

[^falciano-2015]: Falciano, F.T., N. Pinto-Neto, and W. Struyve, 2015, “Wheeler-DeWitt Quantization and Singularities”, *Physical Review D*, 91(4): 043524. doi:10.1103/PhysRevD.91.043524 [[Falciano et al. 2015 preprint available online](https://arxiv.org/abs/1501.04181)]

[^feynman-1967]: Feynman, Richard P., 1967, *The Character of Physical Law*, Cambridge, MA: MIT Press.

[^feynman-1963]: Feynman, Richard P., Robert B. Leighton, and Matthew Sands, 1963, *The Feynman Lectures on Physics, I*, New York: Addison-Wesley.

[^giustina-2015]: Giustina, Marissa et al., 2015, “Significant-Loophole-Free Test of Bell’s Theorem with Entangled Photons”, *Physical Review Letters*, 115: 250401. doi:10.1103/PhysRevLett.115.250401

[^gleason-1957]: Gleason, Andrew M., 1957, “Measures on the Closed Subspaces of a Hilbert Space”, *Indian University Mathematics Journal*, 6(4): 885–893. doi:10.1512/iumj.1957.6.56050

[^goldstein-2001]: Goldstein, Sheldon, 2001, “Boltzmann’s Approach to Statistical Mechanics”, in J. Bricmont, D. Dürr, M.C. Galavotti, G. Ghirardi, F. Petruccione, Nino Zanghì (eds), *Chance in Physics: Foundations and Perspectives*, (Lecture Notes in Physics 574), Berlin: Springer-Verlag, pp. 39–54. doi:10.1007/3-540-44966-3_3 [[Goldstein 2001 preprint available online](https://arxiv.org/abs/cond-mat/0105242)]

[^goldstein-2012]: Goldstein, Sheldon, 2012, “Typicality and Notions of Probability in Physics”, in Y. Ben-Menahem and M. Hemmo (eds), *Probability in Physics*, Berlin: Springer-Verlag, pp. 59–71. [[Goldstein 2012 preprint available online](https://sites.math.rutgers.edu/~oldstein/papers/typ.pdf)]

[^goldstein-2011]: Goldstein, Sheldon, Travis Norsen, Daniel Victor Tausk, and Nino Zanghì, 2011, “Bell’s Theorem”, *Scholarpedia* , 6(10): 8378, revision #91049. doi:10.4249/scholarpedia.8378 URL = <[http://www.scholarpedia.org/article/Bell%27s_theorem](http://www.scholarpedia.org/article/Bell%27s_theorem)>

[^goldstein-2007]: Goldstein, Sheldon and Ward Struyve, 2007, “On the Uniqueness of Quantum Equilibrium in Bohmian Mechanics”, *Journal of Statistical Physics*, 128(5): 1197–1209. doi:10.1007/s10955-007-9354-5 [[Goldstein & Struyve 2007 preprint available online](https://arxiv.org/abs/0704.3070)]

[^goldstein-2001-2]: Goldstein, Sheldon and Stefan Teufel, 2001, “Quantum Spacetime without Observers: Ontological Clarity and the Conceptual Foundations of Quantum Gravity”, in C. Callender and N. Huggett (eds), *Physics meets Philosophy at the Planck Scale*, Cambridge: Cambridge University Press. [[Goldstein & Teufel 2001 preprint available online](https://arxiv.org/abs/quant-ph/9902018)]

[^goldstein-2003]: Goldstein, Sheldon and Roderick Tumulka, 2003, “Opposite Arrows of Time Can Reconcile Relativity and Nonlocality”, *Classical and Quantum Gravity*, 20(3): 557–564. doi:10.1088/0264-9381/20/3/311 [[Goldstein & Tumulka 2003 preprint available online](https://arxiv.org/abs/quant-ph/0105040)]

[^goldstein-2022]: Goldstein, Sheldon and Nino Zanghì, 2022, “Remarks About the Relationship Between Relational Physics and a Large Kantian Component of the Laws of Nature”, in Yemima Ben-Menahem (ed.), *Rethinking the Concept of Law of Nature*, Springer, pp. 225–258. [[Goldstein & Zanghì 2022 preprint available online](https://arxiv.org/abs/2111.09609)]

[^goldstein-2024a]: Goldstein, Sheldon, Roderick Tumulka, and Nino Zanghì, 2024a, “On the Spin Dependence of Detection Times and the Non-Measurability of Arrival Times”, *Scientific Reports*, 14: 3775. [[Goldstein et al. 2024a available online](https://doi.org/10.1038/s41598-024-53777-8)]

[^goldstein-2024b]: Goldstein, Sheldon, Roderick Tumulka, and Nino Zanghì, 2024b, “Arrival Times Versus Detection Times”, *Foundations of Physics*, 54: 63. [[Goldstein et al. 2024b available online](https://doi.org/10.1007/s10701-024-00798-y)]

[^hall-2014]: Hall, Michael J.W., Dirk-André Deckert, and Howard M. Wiseman, 2014, “Quantum Phenomena Modeled by Interactions between Many Classical Worlds”, *Physical Review X*, 4(4): 041013. doi:10.1103/PhysRevX.4.041013

[^heisenberg-1955]: Heisenberg, Werner, 1955, “The Development of the Interpretation of the Quantum Theory”, in W. Pauli (ed.), *Niels Bohr and the Development of Physics: Essays Dedicated to Niels Bohr on the Occasion of his Seventieth Birthday*, New York: McGraw-Hill, pp. 12–29.

[^hemmick-2012]: Hemmick, Douglas L. and Asif M. Shakur, 2012, *Bell’s Theorem and Quantum Realism: Reassessment in Light of the Schrödinger Paradox*, New York: Springer.

[^hensen-2015]: Hensen, B. et al., 2015, “Loophole-free Bell Inequality Violation Using Electron Spins Separated by 1.3 Kilometers”, *Nature*, 526: 682–686. doi:10.1038/nature15759

[^holland-1993]: Holland, Peter R., 1993, *The Quantum Theory of Motion*, Cambridge: Cambridge University Press.

[^kochen-1967]: Kochen, Simon and E.P. Specker, 1967, “The Problem of Hidden Variables in Quantum Mechanics”, *Indiana University Journal of Mathematics*, 17(1): 59–87.

[^kocsis-2011]: Kocsis, Sacha, Boris Braverman, Sylvain Ravets, Martin J. Stevens, Richard P. Mirin, L. Krister Shalm, and Aephraim M. Steinberg, 2011, “Observing the Average Trajectories of Single Photons in a Two-Slit Interferometer”, *Science*, 332: 1170–1173. doi:10.1126/science.1202218

[^kuchař-1992]: Kuchař, Karel, 1992, “Time and Interpretations of Quantum Gravity”, in G. Kunstatter, D. E. Vincent , and J. G. Williams (eds.), *Proceedings of the 4th Canadian Conference on General Relativity and Relativistic Astrophysics (Winnipeg, MB, 1991)*, River Edge, NJ: World Scientific Publishing, pp. 211–314.

[^leavens-1996]: Leavens, C. Richard, 1996, “The ‘Tunneling-Time Problem’ for Electrons”, in Cushing et al. 1996: 111–129. doi:10.1007/978-94-015-8715-0_8

[^leggett-2002]: Leggett, A.J., 2002, “Testing the Limits of Quantum Mechanics: Motivation, State of Play, Prospects”, *Journal of Physics: Condensed Matter*, 14(15): R415–451. doi:10.1088/0953-8984/14/15/201

[^leggett-2005]: –––, 2005, “The Quantum Measurement Problem”, *Science*, 307(5711): 871–872. doi:10.1126/science.1109541

[^leinass-1977]: Leinass, J. and J. Myrheim, 1977, “On the Theory of Identical Particles”, *Il Nuovo Cimento*, 37B: 1–23.

[^lewis-2007]: Lewis, Peter J., 2007, “Empty Waves in Bohmian Quantum Mechanics”, *British Journal for the Philosophy of Science*, 58(4): 787–803. doi:10.1093/bjps/axm039

[^mahler-2016]: Mahler, Dylan H., Lee Rozema, Kent Fisher, Lydia Vermeyden, Kevin J. Resch, Howard M. Wiseman, and Aephraim Steinberg, 2016, “Experimental Nonlocal and Surreal Bohmian Trajectories”, *Science Advances*, 2(2), 1501466. doi:10.1126/sciadv.1501466

[^marian-2016]: Marian, D., Nino Zanghì, and Xavier Oriols, 2016, “Weak Values from Displacement Currents in Multiterminal Electron Devices”, *Physical Review Letters*, 116: 110404. doi:10.1103/PhysRevLett.116.110404 [[Marian et al. 2016 preprint available online](https://arxiv.org/abs/1508.00248)]

[^maudlin-1994]: Maudlin, Tim, 1994, *Quantum Non-Locality and Relativity: Metaphysical Intimations of Modern Physics*, Cambridge, MA: Blackwell.

[^maudlin-2010]: –––, 2010, “Can the World be Only Wavefunction?”, in Saunders et al. 2010: 121–143. doi:10.1093/acprof:oso/9780199560561.003.0005

[^maudlin-2014]: –––, 2014, “What Bell Did”, *Journal of Physics A: Mathematical and Theoretical*, 47: 424010. doi:10.1088/1751-8113/47/42/424010

[^maudlin-2019]: –––, 2019, *Philosophy of Physics: Quantum Theory*, Princeton: Princeton University Press.

[^mermin-1993]: Mermin, N. David, 1993, “Hidden Variables and the Two Theorems of John Bell”, *Reviews of Modern Physics*, 65(3): 803–815. doi:10.1103/RevModPhys.65.803

[^nelson-1985]: Nelson, Edward, 1985, *Quantum Fluctuations*, Princeton: Princeton University Press.

[^nerukh-2000]: Nerukh, Dmitry and John H. Frederick, 2000, “Multidimensional Quantum Dynamics with Trajectories: a Novel Numerical Implementation of Bohmian Mechanics”, *Chemical Physics Letters*, 332(1–2): 145–153. doi:10.1016/S0009-2614(00)01241-0

[^nikolic-2005]: Nikolic, H., 2005, “Relativistic Quantum Mechanics and the Bohmian Interpretation”, *Foundations of Physics Letters*, 18(6): 549–561. doi:10.1007/s10702-005-1128-1

[^norsen-2011]: Norsen, Travis, 2011, “John S. Bell’s Concept of Local Causality”, *American Journal of Physics*, 79: 1261–1275. doi:10.1119/1.3630940

[^norsen-2013]: –––, 2013, “The Pilot-wave Perspective on Quantum Scattering and Tunneling”, *American Journal of Physics*, 81: 258–266. doi:10.1119/1.4792375

[^norsen-2014]: –––, 2014, “The Pilot-wave Perspective on Spin”, *American Journal of Physics*, 82: 337–348. doi:10.1119/1.4848217

[^norsen-2017]: Norsen, Travis, 2017, *Foundations of Quantum Mechanics*, Cham: Springer.

[^oriols-2012]: Oriols, Xavier and Jordi Mompart (eds), 2012, *Applied Bohmian Mechanics: From Nanoscale Systems to Cosmology*, Singapore: Pan Stanford Publishing.

[^pauli-1928]: Pauli, W., 1928, “Discussion of Mr de Broglie’s report”, in Solvay 1928: 280–282.

[^penrose-2005]: Penrose, Roger, 2005, *The Road to Reality*, New York: Alfred A. Knopf.

[^philippidis-1979]: Philippidis, C., C. Dewdney, and B.J. Hiley, 1979, “Quantum Interference and the Quantum Potential”, *Il Nuovo Cimento B*, 52(1): 15–28. doi:10.1007/BF02743566

[^putnam-1965]: Putnam, Hilary, 1965, “A Philosopher Looks at Quantum Mechanics”, reprinted in his 1975, *Philosophical Papers*, vol. 1, *Mathematics, Matter and Method*, Cambridge: Cambridge University Press, pp. 130–58.

[^putnam-2005]: –––, 2005, “A Philosopher Looks at Quantum Mechanics (Again)”, *British Journal for the Philosophy of Science*, 56(4): 615–634. doi:10.1093/bjps/axi135

[^saunders-2010]: Saunders, Simon, Jonathan Barrett, Adrian Kent, and David Wallace (eds), 2010, *Many Worlds? Everett, Quantum Theory, & Reality*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780199560561.001.0001

[^schrödinger-1935]: Schrödinger, E., 1935, “Die gegenwärtige Situation in der Quantenmechanik”, *Die Naturwissenschaften*, 23: 807–812, 823–828, 844–849; English translation by John D. Trimmer, 1980, “The Present Situation in Quantum Mechanics: A Translation of Schrödinger’s ‘Cat Paradox’ Paper”, *Proceedings of the American Philosophical Society*, 124(5): 323–338, reprinted in Wheeler and Zurek 1983: 152–167.

[^sebens-2015]: Sebens, Charles, 2015, “Quantum Mechanics as Classical Physics”, *Philosophy of Science*, 82(2): 266–291. doi:10.1086/680190

[^shalm-2015]: Shalm, Lynden K. et al., 2015, “Strong Loophole-Free Test of Local Realism”, *Physical Review Letters*, 115: 250402. doi:10.1103/PhysRevLett.115.250402

[^solvay-1927]: Solvay Congress (1927), 1928, *Electrons et Photons: Rapports et Discussions du Cinquième Conseil de Physique tenu à Bruxelles du 24 au 29 Octobre 1927 sous les Auspices de l’Institut International de Physique Solvay*, Paris: Gauthier-Villars.

[^struyve-2010]: Struyve, Ward, 2010, “Pilot-Wave Theory and Quantum Fields”, *Reports on Progress in Physics*, 73(1): 106001. doi:10.1088/0034-4885/73/10/106001

[^struyve-2020]: –––, 2020, “Semi-classical Approximations Based on Bohmian Mechanics”, *International Journal of Modern Physics A*, 35: 2050070.

[^teufel-2005]: Teufel, Stefan and Roderich Tumulka, 2005, “Simple Proof for Global Existence of Bohmian Trajectories”, *Communications in Mathematical Physics*, 258(2): 349–365. doi:10.1007/s00220-005-1302-0 [[Teufel & Tumulka 2005 preprint available online](https://arxiv.org/abs/math-ph/0406030)]

[^tumulka-2021]: Tumulka, Roderich, 2021, “Bohmian Mechanics”, in Eleanor Knox and Alastair Wilson (eds), 2021, *The Routledge Companion to the Philosophy of Physics*, Routledge. [[Tumulka 2021 preprint available online](https://arxiv.org/abs/1704.08017)]

[^tumulka-2022]: Tumulka, Roderich, 2022, *Foundations of Quantum Mechanics (Lecture Notes in Physics)*, Cham: Springer.

[^valentini-1991]: Valentini, Antony, 1991, “Signal-Locality, Uncertainty and the Subquantum $H$-Theorem. II”, *Physics Letters A*, 158(1–2): 1–8. doi:10.1016/0375-9601(91)90330-B

[^valentini-1997]: –––, 1997, “On Galilean and Lorentz Invariance in Pilot-Wave Dynamics”, *Physics Letters A*, 228(4–5): 215–222. doi:10.1016/S0375-9601(97)00101-1

[^valentini-2010a]: –––, 2010a, “Inflationary Cosmology as a Probe of Primordial Quantum Mechanics”, *Physical Review D*, 82(6): 063513. doi:10.1103/PhysRevD.82.063513

[^valentini-2010b]: –––, 2010b, “De Broglie-Bohm Pilot-Wave Theory: Many Worlds in Denial?”, in Saunders et al. 2010: 476–509. doi:10.1093/acprof:oso/9780199560561.003.0019

[^valentini-2005]: Valentini, Antony and Hans Westman, 2005, “Dynamical Origin of Quantum Probabilities”, *Proceedings of the Royal Society A*, 461(2053): 253–272. doi:10.1098/rspa.2004.1394

[^neumann-1932]: von Neumann, J., 1932, *Mathematische Grundlagen der Quantenmechanik*, Berlin: Springer Verlag; English translation by R.T. Beyer, 1955, *Mathematical Foundations of Quantum Mechanics*, Princeton: Princeton University Press.

[^weihs-1998]: Weihs, Gregor, Thomas Jennewein, Christoph Simon, Harald Weinfurter, and Anton Zeilinger, 1998, “Violation of Bell’s Inequality under Strict Einstein Locality Conditions”, *Physical Review Letters*, 81: 5039. doi:10.1103/PhysRevLett.81.5039

[^wheeler-1983]: Wheeler, John Archibald and Wojciech Hubert Zurek (eds), 1983, *Quantum Theory and Measurement* (Princeton Series in Physics), Princeton: Princeton University Press.

[^wigner-1976]: Wigner, Eugene P., 1976, “Interpretation of Quantum Mechanics”, lecture notes; revised and printed in Wheeler and Zurek 1983: 260–314.

[^wigner-1983]: –––, 1983, “Review of Quantum Mechanical Measurement Problem”, in Pierre Meystre, and Marian O. Scully (eds), *Quantum Optics, Experimental Gravity and Measurement Theory*, New York: Plenum Press. doi:10.1007/978-1-4613-3712-6_3

[^wiseman-2007]: Wiseman, H.M., 2007, “Grounding Bohmian Mechanics in Weak Values and Bayesianism”, *New Journal of Physics*, 9: 165. doi:10.1088/1367-2630/9/6/165

[^wyatt-2006]: Wyatt, Robert E., 2006, *Quantum Dynamics with Trajectories*, New York: Springer.
