# Retrocausality in Quantum Mechanics
**First published Mon Jun 3, 2019; substantive revision Mon Nov 13, 2023**

*Friederich, Simon, Evans, Peter W.*

Quantum theory provides a framework for modern theoretical physics that enjoys enormous predictive and explanatory success. Yet, in view of the so-called “measurement problem”, there is no consensus on how physical reality can possibly be such that this framework has this success. The theory is thus an extremely well-functioning algorithm to predict and explain the results of observations, but no consensus on which kind of objective reality might plausibly underlie these observations.

Amongst the many attempts to provide an “interpretation” of quantum theory to account for this predictive and explanatory success, one class of interpretations hypothesizes backward-in-time causal influences—retrocausality—as the basis for constructing a convincing foundational account of quantum theory. This entry presents an overview of retrocausal approaches to the interpretation of quantum theory, the main motivations for adopting this approach, a selection of concrete suggested retrocausal models, and a review of the objections brought forward against such approaches.

## 1. History

From the birth of the theory of quantum mechanics in 1925/6 to the outbreak of war in Europe, a clear orthodoxy emerged in the conceptual and ontological framework for understanding quantum theory. Now known as the Copenhagen interpretation, this framework embodied the positivistic tendencies of Heisenberg and Bohr, and was set opposed to the more realist tendencies of de Broglie, Einstein, and Schrödinger. It was not until Bell’s theorem in the 1960s, and its experimental tests in the 1970s and 1980s, that new energy was breathed into this interpretational debate. However, beginning in the mid-1940s, the first suggestions of retrocausality as part of the conceptual and ontological framework in quantum theory had already materialized.

There are two key ideas that punctuate the historical development of the notion of retrocausality in quantum mechanics. The first proposal of retroactive influence in quantum mechanics comes from a suggestion made by Wheeler and Feynman (1945, 1949). They were led to this idea while considering the potentially classical origins of some of the difficulties of quantum theory. Consider the following problem from classical electrodynamics: an accelerating electron emits electromagnetic radiation and, through this process, the acceleration of the electron is damped. Various attempts to account for this phenomenon in terms of the classical theory of electrodynamics lacked either empirical adequacy or a coherent physical interpretation. Wheeler and Feynman attempted to remedy this situation by reinterpreting Dirac’s (1938) theory of radiating electrons.

The core of Wheeler and Feynman’s proposed “absorber theory of radiation” is a suggestion that the process of electromagnetic radiation emission and absorption should be thought of as an interaction between a source and an absorber rather than as an independent elementary process. (This idea has its roots as far back as Tetrode 1922 and G. Lewis 1926.)[^lewis-1926][^tetrode-1922] Wheeler and Feynman imagine an accelerated point charge located within an absorbing system and consider the nature of the electromagnetic field associated with the acceleration. An electromagnetic disturbance can be imagined “initially” to travel outwards from the source to perturb each particle of the absorber. The particles of the absorber then generate together a subsequent field. According to the Wheeler-Feynman view, this new field is comprised of half the sum of the retarded (forward-in-time) and advanced (backward-in-time) solutions to Maxwell’s equations. The sum of the advanced effects of all the particles of the absorber then yields an advanced incoming field that is present at the source simultaneous with the moment of emission (although see §5 for more on how one should understand this “process”). The claim is that this advanced field exerts a finite force on the source which has exactly the required magnitude and direction to account for the observed energy transferred from source to absorber; this is Dirac’s radiative damping field. In addition, when this advanced field is combined with the equivalent half-retarded, half-advanced field of the source, the total observed disturbance is the full retarded field known empirically to be emitted by accelerated point charges.

The crucial point to note about the Wheeler-Feynman schema is that due to the *advanced* field of the absorber, the radiative damping field is present at the source at exactly the time of the initial acceleration. This schema of advanced and retarded waves now forms the basis for the most fully-formed retrocausal model of quantum mechanics, the transactional interpretation (see §5).

The second key idea in the historical development of retrocausality in quantum mechanics occurs around the same time as Wheeler and Feynman’s absorber theory. French physicist Costa de Beauregard, a student of de Broglie, noticed a potential objection to the reasoning found in Einstein, Podolsky, and Rosen’s famous paper (1935) on the completeness of quantum mechanics (see the entry on the Einstein-Podolsky-Rosen argument in quantum theory), now widely known as the EPR argument. Einstein et al. argue that quantum mechanics must be incomplete on the basis of the following assumption: no reasonable definition of reality could be expected to permit the reality of some system being dependent upon the process of measurement carried out on some other distant system which does not in any way disturb the first system. The key condition that Einstein et al. suggest any reasonable definition of reality should satisfy is that “there is no longer any interaction between the two parts”. (Later, Einstein 1948 accounted for this feature with an explicit assumption of “locality”, see §2.2)[^einstein-1948]. Costa de Beauregard, however, was alert to a particular kind of unorthodox alternative to this condition which upended its role in the EPR argument. His proposal was that two distant systems could “remain correlated by means of a successively advanced and retarded wave” (Costa de Beauregard 1953: 1634)[^costa-1953]; that is, one system could influence, via an advanced wave, the state of the combined systems in their common past, which then, via a retarded wave, could influence the state of the distant system in a kind of “zigzag” through spacetime. This way, there could be a dependence between the two distant systems without any “spooky action-at-a-distance”. Thus, as Costa de Beauregard (1987b: 252) puts it,

> Einstein of course is right in seeing an incompatibility between his special relativity theory and the distant quantal correlations, but *only under the assumption that advanced actions are excluded*.

When Costa de Beauregard in 1947 suggested this response to the EPR argument to his then supervisor de Broglie, de Broglie was “far from willing to accept” the proposal (1987b: 252) and forbade Costa de Beauregard to publish his unorthodox idea (Price & Wharton 2015)[^price-2015]. However, in 1948 Feynman had developed his eponymous diagrams in which antiparticles were to be interpreted as particles moving backward-in-time along the particle trajectories, and so by 1953 de Broglie had endorsed the publication of Costa de Beauregard’s response. On the seeming craziness of the proposal, Costa de Beauregard claims, “[t]oday, as the phenomenon of the EPR correlations is very well validated experimentally, and is in itself a ‘crazy phenomenon’, any explanation of it must be ‘crazy’” (1987b: 252; see also Costa de Beauregard 1976, 1977b, 1987a)[^costa-1976][^costa-1977b][^costa-1987a].

## 2. Metaphysical Preliminaries

Before addressing two of the main motivations for adopting the hypothesis of retrocausality in the foundations of quantum theory, it will be worthwhile to provide a few comments on two key notions that play a significant role in the following discussion: causality and locality. This will help to pin down what exactly is meant, and not meant, by retrocausality.

### 2.1 Causality

There is a tradition that stretches back at least as far as Russell (1913) that denies that there is any place for causal notions in the fundamental sciences, including physics: the notion serves no purpose, and simply does not appear, in the fundamental sciences. The argument goes that, since at least the nineteenth century, the laws that govern physical behavior in fundamental sciences such as physics are almost always differential equations. Such equations are notable for specifying, given some initial conditions, exact properties of systems for all time. And thus if everything is specified for all time, there is no place left for causality. Thus Russell advocates that “causality” should be eliminated from the philosophers lexicon, because it is certainly not a part of the scientific lexicon.

In contrast to Russell’s position, Cartwright (1979: 420) claims that we do have a need and use for a causal vocabulary in science: “causal laws cannot be done away with, for they are needed to ground the distinction between effective strategies and ineffective ones”. One of the main contemporary accounts of causation, the interventionist account of causation (Woodward 2003; see also the entry on causation and manipulability)[^woodward-2003], is an embodiment of Cartwright’s dictum. In a nutshell, the interventionist account claims that *A* is a cause of *B* if and only if manipulating *A* is an effective means of (indirectly) manipulating *B*. Causality in the present entry, unless specified otherwise, should be understood along broadly interventionist lines. According to accounts of quantum theory that hypothesize retrocausality, manipulating the setting of a measurement apparatus can be an effective means of manipulating aspects of the past. A broadly interventionist view of causality indeed underlies most contemporary attempts to harness the tool kit of causal modeling (see the entry on causal models; Spirtes, Glymour, & Scheines 2000; Pearl 2009)[^pearl-2009][^spirtes-2000] in the foundations of quantum theory (Leifer & Spekkens 2013; Cavalcanti & Lal 2014; Costa & Shrapnel 2016; Allen et al. 2017)[^allen-2017][^cavalcanti-2014][^costa-2016][^leifer-2013].

Using the notion of causality along broadly interventionist lines in the foundations of quantum theory does not commit one to realism (or anti-realism) about the causal relations at issue. Woodward combines interventionism with realism about causality while acknowledging

> important differences between, on the one hand, the way in which causal notions figure in common sense and the special sciences and the empirical assumptions that underlie their application and, on the other hand, the ways in which these notions figure in physics. (Woodward 2007: 67; although see Frisch 2014: chs. 4 and 5 for a response)[^frisch-2014][^woodward-2007]

Another suggested strategy to take into account Russell’s worry while continuing to apply causal notions in physics in a consistent manner is to understand interventionism in “perspectival” terms (Price 2007; Price & Corry 2007; Price & Weslake 2010; Ismael 2016)[^ismael-2016][^price-2007][^price-2007-2][^price-2010]. Perspectivalism is usually staged, as seems natural in the setting of modern physics (although more will be said on this below), in the framework of a block universe view where the past, present, and future are equally real. In this framework, causality cannot have anything to do with *changing* the future or the past because both are—from an “external” perspective—completely “fixed”. But one can understand causation in the block universe from an “internal” perspective, according to which causal correlations are precisely those that are stable under interventions on those variables that we refer to as the “causes”.

The important difference between the two viewpoints—internal and external to the block—is that there is a discrepancy between the parts of the spacetime block that are epistemically accessible from each perspective. The spatiotemporally constrained perspective by which we are bound permits us only limited epistemic accessibility to other spatiotemporal regions. This is the perspective in which, according to causal perspectivalism, causal notions are perfectly serviceable. Once, on the other hand, we imagine ourselves to be omniscient beings that have epistemic access to the whole spatiotemporal block, it should not come as a surprise that our causal intuitions get confused when we attempt to consider how a spatiotemporally bound agent can deliberate about whether or not to affect a particular event that is already determined from our imagined omniscient perspective. It is because we do not *know* which events are determined to occur and are ignorant about many others that we can be deliberative agents at all. Again, these considerations are relevant just as much to ordinary forward-in-time causation as they are to backward-in-time causation.

Many of the retrocausal approaches to quantum theory considered in §6 are best understood with some type of perspectival interventionist account of causality in mind. A notable exception is the transactional interpretation (§5), in which causality might be best understood in terms of processes underscored by conserved quantities. The possibilist extension of the transactional interpretation, defended by Kastner (2006, 2013), moreover eschews the block universe picture.

### 2.2 Locality

According to Bell’s theorem (Bell 1964; Clauser et al. 1969; see also the entry on Bell’s theorem)[^bell-1964][^clauser-1969] and its descendants (e.g., Greenberger, Horne, & Zeilinger 1989; see also the entry on Bell’s theorem, §6; Goldstein et al. 2011; Brunner et al. 2014 for overviews)[^brunner-2014][^goldstein-2011][^greenberger-1989], any theory that reproduces all the correlations of measurement outcomes predicted by quantum theory must violate a principle that Bell calls *local causality* (Bell 1976, 1990; see also Norsen 2011; Wiseman & Cavalcanti 2017)[^bell-1976][^bell-1990][^norsen-2011][^wiseman-2017]. In a locally causal theory, probabilities of spatiotemporally localized events occurring in some region 1 are independent of what occurs in a region 2 that is spacelike separated from region 1, given a complete specification of what occurs in a spacetime region 3 in region 1’s backward light cone that completely shields off region 1 from the backward light cone of region 2. (See, for instance, Figs. 4 and 6 in Bell 1990 or Fig. 2 in the entry on Bell’s theorem.)[^bell-1990]

In a relativistic setting, then, the notion of locality involves prohibiting conditional dependences between spacelike separated events, provided that the region upon which these spacelike separated events are conditioned constitutes their common causal (Minkowski) past. This characterization of locality explicitly assumes causal asymmetry. Thus locality is the idea that there are no causal relations between spacelike separated events.

There is another sense of “local” that is worth explicitly noting for the purposes of avoiding ambiguity. This is the idea that causal influences are mediated continuously along timelike trajectories. Thus, given Costa de Beauregard’s suggestion of “zigzag” causal influences, it is perfectly possible for a retrocausal model of quantum phenomena to be nonlocal in the sense that causal relations exist between spacelike separated events, but “local” in the sense that these causal influences are constrained to timelike trajectories. For clarity, this latter notion is best understood as set opposed to action-at-a-distance, and is variously delineated as “action-by-contact” (Evans, Price, & Wharton 2013)[^evans-2013][^wharton-2013] or “continuous action” (Wharton & Argaman 2020; Adlam 2022)[^adlam-2022][^wharton-2020].

## 3. Motivation I: Exploiting Loopholes in the “No-Go Theorems”

The first of two main motivating considerations for invoking retrocausality in the foundations of quantum mechanics derives from the exploitation of what is essentially the same loophole in a range of theorems collectively known as “no-go theorems”. According to these theorems, any theory or model that is able to account for the empirically confirmed consequences of quantum theory must be unavoidably *nonlocal*, *contextual*, and *$\psi$-ontic* (i.e., ascribe reality to the quantum states $\psi$).

One way to understand the role that retrocausality plays in circumventing the results of the no-go theorems is to consider each theorem to be underpinned by what is known as the ontological models framework (Harrigan & Spekkens 2010; Leifer 2014; Ringbauer 2017)[^harrigan-2010][^leifer-2014][^ringbauer-2017]. This is a general framework that can be applied to a wide variety of “realist” models, including theories of classical physics as well as local hidden variable approaches to quantum mechanics. The framework consists of an operational description of a “process” which describes observed statistics for outcomes of measurements given both preparations and transformations, along with an ontological model (or “ontic extension”) accounting for the observed statistics. In the quantum context, when a preparation procedures corresponds to a quantum state $\psi$, a quantum system subjected to this procedure actually ends up in an “ontic” state $\lambda$, chosen from a set of states $\Lambda$, which completely specifies the system’s properties. The framework leaves open (and is ultimately used to define) whether the quantum state $\psi$ is itself an ontic or epistemic state (if $\psi$ is ontic, $\lambda$ either includes additional ontic degrees of freedom, or is in one-to-one correspondence with $\psi$; see §3.3). Each preparation is assumed to result in some $\lambda$ via a classical probability density over $\Lambda$, and a set of measurement procedures that determine conditional probabilities for outcomes dependent upon $\lambda$ (which thus screens off the preparation procedure $\psi$); explicitly, $\lambda$ does not causally depend on any future measurement setting $\alpha$. Finally, the operational statistics must reproduce the quantum statistics.

Important for our purposes here is the qualification that, in the ontological models framework, $\lambda$ is assumed to be “conditionally independent” of $\alpha$ (“measurement independence”). This assumption effectively rules out, among other things, that the future measurement setting $\alpha$ causally influences the earlier state $\lambda$. Thus, in so far as the no-go theorems are underpinned by the ontological models framework, the no-go theorems are not applicable to models that do allow retrocausality from $\alpha$ to $\lambda$. And in so far as there is motivation to avoid the consequences of the no-go theorems for quantum theory, retrocausality is well placed to provide such a model (or so the argument goes). Notably, it has been argued that admitting retrocausality (i) makes it possible to account for the correlations entailed by quantum theory using action-by-contact causal influences (and so ensures Lorentz invariance); (ii) undermines as implausible the assumption of (certain types of) noncontextuality from the outset; and (iii) may enable an independently attractive $\psi$-epistemic interpretation of the wavefunction underpinned by local hidden variables. These arguments are addressed in turn.

### 3.1 Nonlocality Theorems

The principle of local causality, according to Bell, is meant to spell out the idea that

> [t]he direct causes (and effects) of events are near by, and even the indirect causes (and effects) are no further away than permitted by the velocity of light. (1990: 105)

Violation of this principle, according to some researchers in the foundations of quantum theory, indicates a fundamental incompatibility between quantum theory and the spirit, perhaps even the letter, of relativity theory (Maudlin 2011)[^maudlin-2011]. That the correlations entailed by quantum theory which violate local causality actually occur in nature has been experimentally documented many times (for example, by Freedman & Clauser 1972; Aspect, Dalibard, & Roger 1982; and Aspect, Grangier, & Roger 1982; see the entry on Bell’s theorem, §4 for an overview on early experiments)[^aspect-1982][^aspect-1982-2][^freedman-1972].

Bell’s result crucially depends not only on the assumption of local causality, but also on the assumption that whatever variables $\lambda$ describes in some spacetime region, which Bell calls “local beables”, do not depend probabilistically on which measurement setting $\alpha$ some experimenters choose in the future of that region:

$$\tag{1} P(\lambda \mid \alpha) = P(\lambda)\,. \label{eq:independence} $$

This is the aforementioned assumption of measurement independence. It is also sometimes referred to as “no superdeterminism” because it is incompatible with a particularly strong form of determinism (“superdeterminism”) according to which the joint past of the measurement setting $\alpha$ and the measured system state $\lambda$ determines them both completely and induces a correlation between them. But, as pointed out in the first instance by Costa de Beauregard (1977a) and then by Price (1994, 1996), superdeterminism is not the only way in which Eq. (\ref{eq:independence}) can be violated: if there is retrocausality (understood along interventionist lines as outlined in §2.1), the choice of measurement setting $\alpha$ may causally influence the physical state $\lambda$ at an earlier time and thereby also render Eq. (\ref{eq:independence}) incorrect. In this picture, as pointed out by Price and Wharton (2021), it might be possible to interpret the local causality-violating correlations between distant events as reflecting a type of retrocausality-induced “collider bias”.

Without Eq. (\ref{eq:independence}), in turn, Bell’s theorem can no longer be derived. Thus, admitting the possibility of retrocausality in principle reopens the possibility of giving a causal account of the nonlocal correlations entailed by quantum theory as mediated by purely action-by-contact, spatiotemporally contiguous, Lorentz invariant causal influences (of the type envisaged by Costa de Beauregard) acting between systems described by local beables. Concrete steps towards a model that might fulfill this promise will be reviewed in §6.

Contrary to this narrative, Adlam (2022) argues that the attempt to rescue *continuous-action*-type locality (of the sort discussed in §2.2) is not a good motivation for retrocausality. According to Adlam, to the extent that the independently most attractive picture of causality is an interventionist one in combination with a block universe view, there is no principled reason for assuming that causal influences are confined to continuous action. Adlam provides her own motivation for retrocausality, based on an argument that “accepting the existence of genuine, unmediated nonlocality in and of itself leads us to accept retrocausality” (2022: 422).

### 3.2 Contextuality Theorems

A wealth of theoretical results establish that models and theories which reproduce the predictions of quantum theory must be in some sense “contextual”. A model or theory is *noncontextual* when the properties attributed to the system (e.g., the value of some dynamical variable that the system is found to have) are independent of the *manner* in which those properties are measured or observed (the context), beyond the actual observation itself (for instance, the other properties that are measured in conjunction with the measurement). In classical mechanics, the properties that systems are found to have and that are attributed to them as a consequence of measurement do not in principle depend on the measurement context, so classical mechanics is noncontextual. The first contextuality theorems for quantum theory go back to Bell (1966) and Kochen and Specker (1967). They demonstrate that if one were to consider quantum measurements as deterministically uncovering the values of arbitrary pre-existing dynamical variables of quantum systems, then such a model would have to be contextual (that is, measured values would have to depend upon the context of measurement). Thus, no noncontextual deterministic local hidden variable model can reproduce the observed statistics of quantum theory.

A new way of understanding contextuality operationally was pioneered by Spekkens (2005). Employing the ontological models framework, an ontological model of an operational theory is *noncontextual* when operationally equivalent experimental procedures have equivalent representations in the ontological model. This understanding of noncontextuality is then a principle of parsimony akin to Leibniz’ law of Identity of Indiscernibles: no ontological difference without operational difference. Using this operational understanding, Spekkens expands the class of ontological models to which contextuality applies beyond deterministic local hidden variable models. But the story is essentially the same: hypothesizing underlying ontic properties for quantum systems that are distinct only if there are corresponding operational differences cannot account for the correlations entailed by quantum theory. Thus, no noncontextual ontological model can reproduce the observed statistics of quantum theory. (For an extended criticism of Spekkens’ operational understanding of contextuality see Hermens 2011.)[^hermens-2011]

Hypothesizing retrocausal influences alleviates both of these worries. Retrocausality renders Kochen-Specker-type contextuality potentially explainable as a form of “causal contextuality” (see the entry on the Kochen-Specker theorem, §5.3). If there is a backward-directed influence of the chosen measurement setting (and context) on the pre-measurement ontic state, it is no longer to be expected that the measurement process is simply uncovering an independently existing definite value for some property of the system, rather the measurement process can play a causal role in *bringing about* such values (the measurement process is retro*causal* rather than retro*dictive*). Indeed, one might argue contextuality of measured values is just what one might expect when admitting retrocausal influences. As Wharton (2014: 203) puts it, “Kochen-Specker contextuality *is* the failure of the Independence Assumption”, i.e., the failure of measurement independence.

With respect to Spekkens’ more general understanding of contextuality, recall that it is an explicit assumption of the ontological models framework that the ontic state is independent of the measurement procedure. Thus, hypothesizing retrocausality is an unequivocal rejection of the ontological models framework. But one might wonder whether Spekkens’ principle of parsimony might be recast to apply more generally to retrocausal models. §7.4 considers a result due to Shrapnel and Costa (2018) that indicates that retrocausal accounts must indeed accept Spekkens-type contextuality.

### 3.3 Psi-ontology Theorems

In some models staged in the ontological models framework, an ontic state $\lambda$ is only compatible with preparation procedures associated with one specific quantum state $\psi$. In that case, $\psi$ can be seen as part of $\lambda$ and, therefore, as an element of reality itself. Models of this type are referred to as “$\psi$-ontic”. In other models, an ontic state $\lambda$ can be the result of preparation procedures associated with different quantum states $\psi$. In these models, $\psi$ is not an aspect of reality and is often more naturally seen as reflecting an agent’s incomplete knowledge about the underlying ontic state $\lambda$. Models of this type are referred to as “$\psi$-epistemic”. Spekkens (2007) motivates the search for attractive $\psi$-epistemic models by pointing out various parallels between quantum mechanics and a toy model in which the analogue of the quantum state is epistemic in that it reflects incomplete information about an underlying ontic state.

However, so-called “$\psi$-ontology theorems” (Pusey, Barrett, & Rudolph 2012; Hardy 2013; Colbeck & Renner 2012; see Leifer 2014 for an overview)[^colbeck-2012][^hardy-2013][^leifer-2014][^pusey-2012], establish that, given certain plausible assumptions, only $\psi$-ontic models can reproduce the empirical consequences of quantum theory. The specific assumptions used to derive this conclusion differ for the various theorems. All of them, however, rely on the ontological models framework which, as noted a number of times already, explicitly incorporates an assumption of measurement independence (Eq. (\ref{eq:independence})). Since, as shown above, measurement independence implicitly rules out retrocausality, these theorems apply only inasmuch as retrocausality is assumed to be absent.

Moreover, the theorem due to Pusey, Barrett, and Rudolph (2012)—which according to Leifer (2014) uses the least contestable assumptions of all—relies on an additional independence assumption according to which the ontic states of two or more distinct, randomly prepared, systems are uncorrelated before undergoing joint measurement. Wharton (2014: 203) points out that in a framework that is open to retrocausality this is a problematic assumption because one would then expect “past correlations [to] arise […] for exactly the same reason that future correlations arise in entanglement experiments”. Exploring the prospects for retrocausal accounts is therefore one—perhaps *the*—important open route for developing an attractive $\psi$-epistemic model that may be able to explain the quantum correlations.

### 3.4 Classical Ontology?

It is worth pausing at this point to consider the metaphysical motivation for taking a retrocausal approach to quantum theory, especially in light of circumventing these no-go theorems. The orthodox reading of the no-go theorems is that, whatever is said about the ultimate conceptual and ontological framework for understanding quantum theory, it cannot be completely classical: it must be nonlocal and/or contextual and/or ascribe reality to indeterminate states. In short, quantum theory cannot be about local hidden variables. Part of the appeal of hypothesizing retrocausality in the face of these no-go theorems is to regain (either partial or complete) classicality in these senses (albeit, with—perhaps nonclassical—symmetric causal influences). That is, retrocausality holds the potential to allow a metaphysical framework for quantum mechanics that contains causally action-by-contact, noncontextual (or where any contextuality is underpinned by noncontextual epistemic constraints), counterfactually definite, determinate (although possibly indeterministic), spatiotemporally located properties for physical systems—in other words, a classical ontology.

A nice to way to consider this is in terms of Quine’s (1951) distinction between the “ontology” and the “ideology” of a scientific theory, where the ideology of a theory consists of the ideas that can be expressed in that theory. Ideological economy is then a measure of the economy of primitive undefined statements employed to reproduce this ideology. The claim here would then be that the ideology of symmetric causal influences is more economical than rejecting a classical ontology. Thus in so far as quantum mechanics is telling us something profound about the fundamental nature of reality, the hypothesis of retrocausality shows that the lesson of quantum mechanics is not necessarily that the quantum ontology can no longer be classical. Some might see this as a virtue of retrocausal approaches. (Although the Shrapnel-Costa no-go theorem reviewed in §7.4 significantly jeopardizes this view.)

## 4. Motivation II: Time-Symmetry

### 4.1 Deriving Retrocausality from Time-Symmetry

The laws of nature at the most fundamental level at which they are currently known are combined in the Standard Model of elementary particle physics. These laws are CPT-invariant, i.e., they remain the same under the combined operations of charge-reversal *C* (replacing all particles by their anti-particles), parity *P* (flipping the signs of all spatial coordinates), and time-reversal *T*. The asymmetries in time which are pervasive in our everyday lives are a consequence not of any temporal asymmetry in these laws but, instead, of the boundary conditions of the universe, notably in its very early stages. It seems natural to assume that the time-symmetry of the laws (modulo the combined operation of *C* and *P*) extends to causal dependences at the fundamental “ontic” level that underlies the empirical success of quantum theory. If so, there may be backward-in-time no less than forward-in-time causal influences at that ontic level.

Price (2012) turns these sketchy considerations into a rigorous argument. He shows that, when combined with two assumptions concerning quantum ontology, time-symmetry implies retrocausality (understood along broadly interventionist lines). The ontological assumptions are (i) that at least some aspects of the quantum state $\psi$ are real (notably, in Price’s example, there is a “beable” encoding photon polarization angle), and (ii) that inputs and outputs of quantum experiments are *discrete* emission and detection events. Moreover, it is important to Price’s argument that dynamical time-symmetry (that the dynamical laws of the theory are time-symmetric) be understood as implying that operational time-symmetry (that the set of all possible combinations of preparation and measurement procedures in a theory, with associated probabilities for outputs given inputs, is closed under interchange of preparation and measurement) translates into ontic time-symmetry (operational time-symmetry plus a suitable map between the ontic state spaces of the symmetric combinations). Given these conditions, any foundational account that reproduces the empirical verdicts of quantum theory must be retrocausal.

Leifer and Pusey (2017) (see also Leifer 2017 in Other Internet Resources)[^leifer-2017] strengthen Price’s argument by showing that his assumption about the reality of (aspects of) the quantum state $\psi$ can be relaxed. As they demonstrate, if measurement outcomes depend only on a system’s ontic state $\lambda$, i.e., if that state completely mediates any correlations between preparation procedures and measurement outcomes (“$\lambda$-mediation”), this suffices for operational time-symmetry to entail the existence of retrocausality. Foundational accounts which like Bohmian mechanics (Bohm 1952a,b)[^bohm-1952a] or GRW-theory (Ghirardi, Rimini, & Weber 1986)[^ghirardi-1986] avoid postulating retrocausality do so by violating time-symmetry in some way. The GRW-theory does so by introducing explicitly time-asymmetric dynamics. In Bohmian mechanics the dynamics is time-symmetric, but the theory is applied in a time-asymmetric manner when assessing which quantum states are actually realized. Notably, one assumes that the quantum states of a measured system and a measurement device connected to it are uncorrelated prior to measurement, whereas they are in general correlated after measurement (Leifer & Pusey 2017: §X.)[^leifer-2017].

### 4.2 The Action Duality Principle

The more advanced relativistic quantum theories that underlie modern particle physics are typically formulated in the Lagrangian, path integral-based, formalism, where information about the symmetries and interactions of the theory are encoded in the action, *S*. Wharton, Miller, and Price (2011) use this formalism as a foundation to suggest that action symmetries must be reflected as ontological symmetries. In particular, Wharton et al. claim that for any two experimental arrangements related by a spacetime transformation (say, reflection in time) that leaves the action unchanged, the ontologies must also remain unchanged across the same spacetime transformation. This principle, referred to by Wharton et al. as *action duality*, imposes non-trivial constraints on realist accounts.

Notably, Evans, Price, & Wharton (2013) argue that there is such an action symmetry between a pair of entangled photons passing through separate polarizers and a single photon passing sequentially through two polarizers. Thus, if action duality is well-founded, the action symmetry should be reflected in identical ontologies for the action-dual experiments. Short of rejecting action duality, this implies one of two things: either the usual causal explanation for the behavior of the single photon must be reflected in a causal explanation for the typically-quantum behavior of the pair of entangled photons, and so there must be retrocausality at the level of the ontic state $\lambda$, or the nonlocality ascribed to the typically-quantum behavior of the pair of entangled photons must be similarly ascribed to the behavior of the single photon, and so nonlocality is even more dramatically widespread than usually assumed, and indeed is not unique to entangled bipartite quantum systems. In so far as there is a strong case for the behavior of a single photon passing sequentially through two polarizers having a perfectly good causal explanation based on spatiotemporally localized properties, the argument of Evans et al. is that this amounts to an equally strong case for retrocausality in quantum theory.

## 5. The Transactional Interpretation

This entry so far has considered the two most significant motivating arguments in favor of adopting retrocausality as a hypothesis for dealing with the interpretational challenges of quantum theory. But these motivations do not by themselves amount to an interpretation or model of quantum theory. §6 consists of a survey of a range of retrocausal models, but this section first considers perhaps the most prominent retrocausal model, the transactional interpretation. Developed by Cramer in the 1980s (Cramer 1980, 1986, 1988)[^cramer-1980][^cramer-1986][^cramer-1988], the transactional interpretation is heavily influenced by the framework of the Wheeler-Feynman absorber approach to electrodynamics (see §1); the Wheeler-Feynman schema can be adopted to describe the microscopic exchange of a single quantum of energy, momentum, *etc.*, between and within quantum systems.

At the heart of the transactional interpretation is the “transaction”: real physical events are identified with so-called “handshakes” between forward-evolving quantum states $\psi$ and backward-evolving complex-conjugates $\psi^*$. When a quantum emitter (such as a vibrating electron or atom in an excited state) is to emit a single quantum (a photon, in these cases), the source produces a radiative field—the “offer” wave. Analogously to the Wheeler-Feynman description, this field propagates outwards both forward and backward in time (as well as across space). When this field encounters an absorber, a new field is generated—the “confirmation” wave—that likewise propagates both forward and backward in time, and so is present as an advanced incident wave at the emitter at the instant of emission. Both the retarded field produced by the absorber and the advanced field produced by the emitter exactly cancel with the retarded field produced by the emitter and advanced field produced by the absorber for all times before the emission and after the absorption of the photon; only between the emitter and the absorber is there a radiative field. Thus the transaction is completed with this “handshake”: a cycle of offer and confirmation waves

> repeats until the response of the emitter and absorber is sufficient to satisfy all of the quantum boundary conditions…at which point the transaction is completed. (Cramer 1986: 662)[^cramer-1986]

Many confirmation waves from potential absorbers may converge on the emitter at the time of emission but the quantum boundary conditions can usually only permit a single transaction to form. Any observer who witnesses this process would perceive only the completed transaction, which would be interpreted as the passage of a particle (e.g., a photon) between emitter and absorber.

The transactional interpretation takes the wave function to be a real physical wave with spatial extent. The wave function of the quantum mechanical formalism is identical with the initial offer wave of the transaction mechanism and the collapsed wave function is identical with the completed transaction. Quantum particles are thus not to be thought of as represented by the wave function but rather by the completed transaction, of which the wave function is only the initial phase. As Cramer explains:

> The transaction may involve a single emitter and absorber or multiple emitters and absorbers, but it is only complete when appropriate boundary conditions are satisfied at all loci of emission and absorption. Particles transferred have no separate identity independent from the satisfaction of these boundary conditions. (1986: 666)

The amplitude of the confirmation wave which is produced by the absorber is proportional to the local amplitude of the incident wave that stimulated it and this, in turn, is dependent on the attenuation it received as it propagated from the source. Thus, the total amplitude of the confirmation wave is just the absolute square of the initial offer wave (evaluated at the absorber), which yields the Born rule. Since the Born rule arises as a product of the transaction mechanism, there is no special significance attached to the role of the observer in the act of measurement. The “collapse of the wave function” is interpreted as the completion of the transaction.

The transactional interpretation explicitly interprets the quantum state $\psi$ as real, and so does not constitute an attempt to exploit the retrocausality loopholes to the theorems that rule out $\psi$-epistemic accounts. Additionally, the transactional interpretation subverts the dilemma at the core of the EPR argument (Einstein, et al. 1935)[^einstein-1935] by permitting incompatible observables to take on definite values simultaneously: the wavefunction, according to the transactional interpretation,

> brings to each potential absorber the full range of possible outcomes, and all have “simultaneous reality” in the EPR sense. The absorber interacts so as to cause one of these outcomes to emerge in the transaction, so that the collapsed [wavefunction] manifests only one of these outcomes. (Cramer 1986: 668)[^cramer-1986].

Most importantly, however, the transactional interpretation employs both retarded and advanced waves, and in doing so admits the possibility of providing a “zigzag” explanation of the nonlocality associated with entangled quantum systems.

Before turning to one of the more significant objections to the transactional interpretation, and to retrocausality in general, it is instructive to tease apart here two complementary descriptions of this transaction process. On the one hand there is a description of the real physical process, consisting of the passage of a particle between emitter and absorber, that a temporally bound experimenter would observe; and on the other hand there is a description of a dynamical process of offer and confirmation waves that is instrumental in establishing the transaction. This latter process simply cannot occur in an ordinary time sequence, not least because any temporally bound observer by construction cannot detect any offer or confirmation waves. Cramer suggests that the “dynamical process” be understood as occurring in a “pseudotime” sequence:

> The account of an emitter-absorber transaction presented here employs the semantic device of describing a process extending across a lightlike or a timelike interval of space-time as if it occurred in a time sequence external to the process. The reader is reminded that this is only a pedagogical convention for the purposes of description. The process is atemporal and the only observables come from the superposition of all “steps” to form the final transaction. (Cramer 1986: 661, fn.14)[^cramer-1986]

These steps are of course the cyclically repeated exchange of offer and confirmation waves which continue “until the net exchange of energy and other conserved quantities satisfies the quantum boundary conditions of the system” (1986: 662). There is a strong sense here that any process described as occurring in pseudotime is *not a process at all* but, as Cramer reminds, merely a “pedagogical convention for the purposes of description”. Whether it is best to understand causality according to the transactional interpretation in terms of processes underscored by conserved quantities is closely tied to how one should best understand this pseudotemporal process.

Maudlin (2011) outlines a selection of problems that arise in Cramer’s theory as a result of the pseudotemporal account of the transaction mechanism: processes important to the completion of a transaction take place in pseudotime only (rather than in real time) and thus cannot be said to have taken place at all. Since a temporally bound observer can only ever perceive a completed transaction, i.e., a collapsed wavefunction, the uncollapsed wavefunction never actually exists. Since the initial offer wave is identical to the wavefunction of the quantum formalism, any ensuing exchange of advanced and retarded waves required to provide the quantum mechanical probabilities, according to Maudlin, also do not exist. Moreover, Cramer’s exposition of the transaction mechanism seems to suggest that the stimulation of sequential offer and confirmation waves occurs deterministically, leaving a gaping hole in any explanation the transactional interpretation might provide of the stochastic nature of quantum mechanics. Although these problems are significant, Maudlin admits that they may indeed be peculiar to Cramer’s theory. Maudlin also sets out a more general objection to retrocausal models of quantum mechanics which he claims to pose a problem for “any theory in which both backwards and forwards influences conspire to shape events” (2011: 184).

Maudlin’s main objection to the transactional interpretation hinges upon the fact that the transaction process depends crucially on the fixity of the absorbers “just sitting out there in the future, waiting to absorb” (2011: 182); one cannot presume that present events are unable to influence the future disposition of the absorbers. Maudlin offers a thought experiment to illustrate this objection. A radioactive source is constrained to emit a $\beta$-particle either to the left or to the right. To the right sits absorber *A* at a distance of 1 unit. Absorber *B* is also located to the right but at a distance of 2 units and is built on pivots so that it can be swung around to the left on command. A $\beta$-particle emitted at time $t_{0}$ to the right will be absorbed by absorber *A* at time $t_{1}$. If after time $t_{1}$ the $\beta$-particle is not detected at absorber *A*, absorber *B* is quickly swung around to the left to detect the $\beta$-particle after time $2t_{1}$.

According to the transactional interpretation, since there are two possible outcomes (detection at absorber *A* or detection at absorber *B*), there will be two confirmation waves sent back from the future, one for each absorber. Furthermore, since it is equally probable that the $\beta$-particle be detected at either absorber, the amplitudes of these confirmation waves should be equal. However, a confirmation wave from absorber *B* can only be sent back to the emitter if absorber *B* is located on the left. For this to be the case, absorber *A* must not have detected the $\beta$-particle and thus the outcome of the experiment must already have been decided. The incidence of a confirmation wave from absorber *B* at the emitter *ensures* that the $\beta$-particle is to be sent to the left, even though the amplitude of this wave implies a probability of a half of this being the case. As Maudlin (2011: 184) states so succinctly, “Cramer’s theory collapses”.

The key challenge from Maudlin is that any retrocausal mechanism must ensure that the future behavior of the system transpires consistently with the spatiotemporal structure dictated by any potential future causes: “stochastic outcomes at a particular point in time may influence the future, but that future itself is supposed to play a role in producing the outcomes” (2011: 181). In the transactional interpretation the existence of the confirmation wave itself presupposes some determined future state of the system with retrocausal influence. However, with standard (i.e., forward-in-time) stochastic causal influences affecting the future from the present, a determined future *may not necessarily be guaranteed* in every such case, as shown by Maudlin’s experiment.

Maudlin’s challenge to the transactional interpretation has been met with a range of responses. The responses generally fall into two types (P. Lewis 2013)[^lewis-2013]. The first type of response attempts to accommodate Maudlin’s example within the transactional interpretation. Berkovitz (2002) defends the transactional interpretation by showing that causal loops of the type found in Maudlin’s experiment need not obey the assumptions about probabilities that are common in linear causal situations. Marchildon (2006) proposes considering the absorption properties of the long distance boundary conditions: if the universe is a perfect absorber of all radiation then a confirmation wave from the left will always be received by the radioactive source at the time of emission and it will encode the correct probabilistic information. Kastner (2006) proposes differentiating between competing initial states of the radioactive source, corresponding to the two emission possibilities, that together characterize an unstable bifurcation point between distinct worlds, where the seemingly problematic probabilities reflect a probabilistic structure across both possible worlds.

The second type of response is to modify the transactional interpretation. For instance, Cramer (2016) introduces the idea of a hierarchy of advanced-wave echoes dependent upon the magnitude of the spatiotemporal interval from which they originate. Kastner (2013) surmises that the source of the problem that Maudlin has exposed, however, is the idea that quantum processes take place in the “block world”, and rejects this conception of processes in her own development of the transactional interpretation. According to her “possibilist” transactional interpretation, all the potential transactions exist in a real space of possibilities, which amounts at once to a kind of modal realism and an indeterminacy regarding future states of the system (hence Kastner’s rejection of the block universe view). The possibilist transactional interpretation arguably handles multi-particle scenarios more naturally, and presents the most modern sustained development of the transactional interpretation (although see P. Lewis 2013 for criticisms of the possibilist transactional interpretation specific to Maudlin’s challenge)[^lewis-2013].

## 6. Developments Towards a Retrocausal Model

The transactional interpretation might be seen as the most prominent—and historically significant—retrocausal model on the market, but it is not the only one. While retrocausality in quantum mechanics has been the subject of considerable analysis and critique over the years (Rietdijk 1978; Sutherland 1983, 1985, 1989; Price 1984, 2001; Hokkyo 1988, 2008; Miller 1996, 1997; Atkinson 2000; Argaman 2010; Evans 2015)[^argaman-2010][^atkinson-2000][^evans-2015][^hokkyo-1988][^miller-1996][^miller-1997][^price-1984][^price-2001][^rietdijk-1978][^sutherland-1983][^sutherland-1985][^sutherland-1989], the focus of this section is a review of some of the more concrete proposals for retrocausal models.

### 6.1 The Two-State Vector Formalism

What is now known as the two-state vector formalism was first proposed by Watanabe (1955), and then rediscovered by Aharonov, Bergmann, and Lebowitz (1964). The proposal is that the usual forward evolving quantum state contains insufficient information to completely specify a quantum system; rather the forward evolving state must be supplemented by a backward evolving state to provide a complete specification. Thus, according to the two-state vector formalism, the complete quantum description contains a state vector that evolves forward in time from the initial boundary condition towards the future, and a state vector that evolves backward in time from the future boundary condition towards the past. It is only a combination of complete measurements at both initial and final boundaries that can provide a complete specification of a quantum system. The two-state vector formalism is empirically equivalent to standard quantum mechanics (Aharonov & Vaidman 1991, 2008)[^aharonov-1991].

The emphasis of the two-state vector formalism is on the operational elements of the theory, and there are very few ontological prescriptions, including how best to understand causality. It is in principle compatible with a variety of supplemented retrocausal ontologies, e.g., the causally symmetric Bohm model (§6.3).

### 6.2 Toy Models

Toy models have been employed to illustrate how retrocausality could be possibly realized. Price (2008) suggests a simple toy model featuring linked nodes that can assume different values, which he dubs the “Helsinki model”. If one interprets the nodes as partially ordered in time and the values of the exogenous boundary nodes as controllable, the dynamics specified by Price entails causal bi-directionality, i.e., both ordinary forward causality and retrocausality, understood in an interventionist sense. Although the model does indeed display particular behavior that can be naturally interpreted as retrocausal, a full-blown analogy with standard quantum mechanics is limited.

The Helsinki model consists of three primitive endogenous nodes, each node comprising a meeting point of three edges, with two “internal” edges linking the three nodes and five “external” edges. Each edge has one of three “flavors”, *A*, *B*, or *C*. The system is temporally oriented with three exogenous nodes, each joined to a single edge, representing system “inputs” (preparations/interventions), and two system “outputs” (measurement outcomes/observations) joined to the remaining two edges. The two internal edges represent hidden flavors that cannot be directly controlled or observed. There are two basic rules that govern the dynamics of this toy system: (i) each node must be strictly inhomogeneous—i.e., comprising three edges of different flavors—or strictly homogeneous—i.e., three edges of the same flavor, and (ii) successive homogeneous nodes are prohibited.

The retrocausal behavior of the model arises as a result of the heavy constraints that the two basic rules place on the possible flavors of the hidden edges, which establishes correlations between the input states and the hidden states. Thus interventions on the left or right exogenous variables influence the complete set of possible hidden states of the system. Assuming that the hidden states are in the past of these variable choices, the hidden state depends “retrocausally” on the left and right input settings. Moreover, under specific node variables, some interventions on the left or right exogenous variables amount to interventions on the distant output variable, displaying a kind of nonlocality (but violating no-signaling).

More ambitiously, Corry (2015) proposes three toy models, also using nodes and links, which exhibit Bell-type correlations and account for them in a purely local manner in that the constraints governing nodes make reference only to information available at the respective nodes. The models do not in general specify values for unobserved nodes, however. As a way out, Corry suggests, one may either postulate such values at the price of accepting “retrofinkish dispositions” (dispositions which, if they were triggered, would not have been there in the first place) or simply deny the existence of such values outright.

### 6.3 The Causally Symmetric Bohm Model

A model that hypothesizes retrocausality and reproduces the consequences of standard quantum theory without violating Lorentz invariance is Sutherland’s (2008, 2015, 2017) causally symmetric version of Bohmian mechanics. This model adds to the standard quantum state $\psi_i$ of ordinary Bohmian mechanics, which is fixed by an initial boundary condition, an additional quantum state $\psi_f$, which is fixed by some final boundary condition. An analogue to the “guiding equation” for particle motion in ordinary Bohmian mechanics is derived by Sutherland that is symmetric with respect to these states. The zero-component of the probability current, which is directly related to the probability density, is computed as

$$\tag{2} \rho(\mathbf x, t)={\rm Re}\left(\psi\frac{\psi^*_f\psi_i}{a}\right)\,\label{eq:probdens} $$

where

$$\tag{3} a=\int\psi_f^*(\mathbf x,t)\psi_i(\mathbf x,t)d^3x\,. $$

Finally, for consistency, the model also requires that the conditional probability of the final state being $\psi_f$, given the initial state $\psi_i$, is

$$\tag{4} \rho(\psi_f\mid \psi_i)=\lvert a\rvert^2\,\label{eq:addass}\,. $$

Berkovitz (2008) criticizes the use of the additional assumption Eq. (\ref{eq:addass}) and the need for it in Sutherland’s model, arguing that it leads to an undesirable form of causal loops and has an *ad hoc* character because there is no independent reason to think that $\psi_i$ and $\psi_f$ should be correlated in this way.

Sutherland’s model is explicitly retrocausal in that particle dynamics are influenced by $\psi_f$, which in turn depends on the future measurement setting. It also contains action-by-contact causal influences in that Bell-type correlations are accounted for in the “zigzag” manner envisaged by Costa de Beauregard, as outlined in §1.

### 6.4 The Relational Blockworld Interpretation

Silberstein, Stuckey, and McDevitt (2018), based on earlier work together with Cifone (Stuckey, Silberstein, & Cifone 2008; Silberstein, Cifone, & Stuckey. 2008)[^silberstein-2008][^stuckey-2008], suggest a realist interpretation that they call the “relational blockworld view”. The ontology of this interpretation consists of so-called “spacetimesource elements”, which are characterized as “amalgams of space, time, and sources” (Silberstein, Stuckey, & McDevitt 2018: 153)[^silberstein-2018].

Technically, the relational blockworld approach is set up as a modification of lattice gauge theory, with the Feynman path integral functioning as an “adynamical global constraint”. While adynamical and acausal rather than retrocausal in spirit, on the authors’ view this interpretation exploits the retrocausality loopholes of the no-go theorems. They conceive of the relational blockworld view as $\psi$-epistemic. In more recent work (2018: Ch. 6), Silberstein, Stuckey and McDevitt have developed this approach into an ambitious overarching programme in fundamental physics, aiming at field-theoretic unification as well as a novel account of quantum gravity.

### 6.5 The Two-Time Boundary Value Model

Schulman (1997, 2012) proposes a solution to the quantum measurement problem based on the possibility of future conditioning, which originates from his analysis of the thermodynamic arrow of time. Beginning with Loschmidt’s challenge to Boltzmann—that it should not be possible to derive irreversible dynamical behavior from time-symmetric dynamics (see the entry on thermodynamic asymmetry in time)—Schulman notes that successful “retrodiction” of past macroscopic states of some thermodynamic system is indeed asymmetric to successful “prediction” of future macroscopic states. For successful retrodiction, rather than evolving each of the microscopic states of some macroscopic state according to the dynamical laws (which is identical to the process of prediction, and is the basis of Loschmidt’s challenge), one instead hypothesizes a prior macroscopic state to which the prediction process can be applied such that the current macroscopic state of the system obtains with high likelihood given the dynamical evolution of the prior microscopic states. With respect to the set of possible microscopic states for the current macroscopic state, since the evolution of the vast majority (on Liouville measure) of these states according to the dynamical laws result in trajectories that conflict with the retrodiction hypothesis, these states are effectively rejected in the process of retrodiction in favor of those special few microscopic states that correspond to the dynamical evolution of acceptable hypothetical initial conditions.

Schulman’s proposal in response to this asymmetry is that, just as the set of possible final microscopic states must be restricted for successful retrodiction, so should the permissible initial microscopic states be restricted for the purposes of prediction. Thus, since final microscopic states are subject to conditioning from the past state of the system, the initial microscopic states will be subject to conditioning from the future state of the system—a conditioning that is hidden in thermodynamic processes where the microscopic states of the system are indistinguishable macroscopically. This future conditioning is a central feature of Schulman’s two-time boundary condition proposal and the hidden nature of this conditioning Schulman calls “cryptic constraints”.

Regarding quantum theory, Schulman claims that quantum superpositions of macroscopically distinct states generated by quantum evolution, which are at the heart of many of the nonclassical elements of quantum theory, are what he calls “grotesque” states, and proposes that these states are avoided in quantum systems due to future conditioning and cryptic constraints. Just like there are special microscopic states of thermodynamical systems that evolve “against” the second law of thermodynamics (which are identified in the process of retrodiction), so too must there be “special” microscopic states of a quantum system which do not lead to grotesque states when evolved according to the quantum dynamical laws, rather these states will lead to one particular definite state of the superposition. Schulman’s solution to the quantum measurement problem is that, in every performed experiment, the initial conditions of the quantum system are among these special states which, through pure unitary quantum evolution, yield a single outcome to the experiment (Schulman 1997: 214)[^schulman-1997]. Grotesque states, the problematic states of the quantum measurement problem, are thus avoided.

Schulman’s proposal implicitly assumes that, in the preparation of an experiment, it is only the macroscopic state of the system which is under the control of the experimenter; it is impossible to control the precise microscopic state. It is this initial microscopic state that Schulman suggests is always a special state. Schulman envisages the special-state constraint as correlated with future conditions and, since these constraints are not apparent to the experimenter until the future conditions are “measured” at the end of the experiment, these constraints are cryptic. As a result of the future conditioning of initial states, Schulman’s proposal is a kind of retrocausal mechanism, understood in an interventionist sense. (For an extension of Schulman’s model into the Lagrangian schema (§6.6) see Almada et al. 2016 and Wharton 2014, 2018.)

### 6.6 “All-at-once” Lagrangian Models

Wharton (2010a; see also Wharton 2007, 2010b, 2013, 2016, 2018; Wharton, Miller, & Price 2011; Evans, Price, & Wharton 2013)[^evans-2013][^wharton-2007][^wharton-2010b][^wharton-2013][^wharton-2016][^wharton-2018][^wharton-2011] proposes a “novel interpretation of the Klein-Gordon equation” for a neutral, spinless relativistic particle. The account is a retrocausal picture based on Hamilton’s principle and the symmetric constraint of both initial and final boundary conditions to construct equations of motion from a Lagrangian, and is a natural setting for a perspectival interventionist account of causality. Wharton treats external measurements as physical constraints imposed on a system in the same way that boundary constraints are imposed on the action integral of Hamilton’s principle; the final measurement does not simply reveal preexisting values of the parameters, but constrains those values (just as the initial boundary condition would). Wharton’s model has been described as an “all-at-once” approach, since the dynamics of physical systems between an initial and final boundary emerges *en bloc* as the solution to a two-time boundary value problem.

On this interpretation, one considers reality exclusively between two temporal boundaries as being described by a classical field $\phi$ that is a solution to the Klein-Gordon equation: specification of field values at both an initial and final boundary (as opposed to field values and their rate of change at only the initial boundary) constrains the field solutions between the boundaries. Wharton argues that constraining such fields at both an initial and a final boundary (or a closed hypersurface in spacetime) generates two strikingly quantum features: quantization of certain field properties and contextuality of the unknown parameters characterizing the field between the boundaries. (That there are unknown parameters before the imposition of the final condition is ensured due to the underdetermination of the classical field by specifying only the field values, and not their rate of change, in the initial data.)

From within Wharton’s picture, an invariant joint probability distribution associated with each possible pair of initial and final conditions can be constructed, and the usual conditional probabilities can be formed by conditioning on any chosen portion of the boundary (Wharton 2010a,b)[^wharton-2010a]. Probability is then a manifestation of our ignorance: if one knew only the initial boundary, one would only be able to describe the subsequent field probabilistically (due to the future constraint); given the final boundary as well, one would then be able to retrodict the field values between the two boundaries. (See Evans, Gryb, and Thébault 2016 for a proposed extension of this schema to the cosmological context.)[^evans-2016]

In more recent work (Wharton 2016)[^wharton-2016], Wharton explores the prospects for a realist retrocausal interpretation of quantum theory based on the Feynman path integral formalism (Feynman 1942)[^feynman-1942]. In that formalism as applied to a single particle undergoing position measurements at spacetime points $(\mathbf{x_0},t_0)$ and $(\mathbf{x_1},t_1)$, the joint probability distribution for all pairs of points and given times $t_0$ and $t_1$ is given by

$$\tag{5} P(\mathbf{x_0},\mathbf{x_1})=\left|\sum_{\mathbf{x_0}\mapsto\mathbf{x_1}}\exp(iS/\hbar)\right|^2\,.\label{eq:feynman} $$

The sum in this formula is to be understood as the infinitesimal limit of a discretized set of spacetime trajectories connecting $(\mathbf{x_0},t_0)$ and $(\mathbf{x_1},t_1)$. *S* is the classical action of the particle along the respective trajectory.

A straightforward but naive interpretation of this equation according to which the probability reflects ignorance concerning the path taken does not work because the right hand side of Eq. (\ref{eq:feynman}) is not a sum of positive numbers (interpretable as probabilities of trajectories) but rather a positive number obtained by taking the modulus squared of a sum of complex numbers. Wharton explores the prospects for giving an ignorance interpretation of the path integral along less straightforward lines, noting that Eq. (\ref{eq:feynman}) can be brought into the form

$$\tag{6} P(\mathbf{x_0},\mathbf{x_1})=\sum_{c_i}\left|\sum_{A\in c_i}\exp(iS_A/\hbar)\right|^2\,,\label{eq:wharton} $$

where the $\left|c_i\right|$ are distinct *groups of trajectories* *A*. The form Eq. (\ref{eq:wharton}), according to Wharton, invites an interpretation of the probability in terms of ignorance concerning the actual group of trajectories $c_i$, and he tentatively proposes a field interpretation of the $c_i$. The interpretation is retrocausal because the probabilities over groups of trajectories are influenced by the future measurement time and setting. Open questions for this approach concern the grouping of trajectories, which is so far inherently ambiguous, the details of the suggested field interpretation, as well as generalizations to many-particle and other more general settings.

### 6.7 The Q-based interpretation

The Husimi Q-function (Husimi 1940)[^husimi-1940] is a non-negative distribution function on phase space with a wide applicability, e.g. in quantum optics. It is obtained from the better known Wigner function (Wigner 1932)[^wigner-1932][^wigner-1932-2] by smoothening with a Gaussian filter. The Q-based interpretation (Drumond and Reid 2020; Friederich 2021)[^friederich-2021] assumes that any quantum system has a precise phase space location, and that phase space locations are distributed according to the Q-function. As a consequence, all dynamical variables of all quantum systems have definite values in this interpretation, and the measurement problem is avoided.

Drummond and Reid (2020) argue that this interpretation avoids the no-go theorems discussed in §3 via the retrocausality loophole. In support of this claim, they point to a result by Drummond (2021), according to which, for a wide class of quantum field theories, the Q-function evolves via diffusion backward in time for half of all degrees of freedom (and forward for the other half). Friederich (2021) suggests that failure of temporal locality, independently motivated by Adlam (2018, 2022), could also make those theorems inapplicable to the Q-based interpretation.

It is not immediately obvious that the Q-based interpretation is empirically adequate since it does not exactly reproduce the quantum probabilities derived from the Born rule. However, as argued by Drummond and Reid (2020), for various measurement setups and at the level of macroscopic measurement devices, the discrepancy with standard quantum mechanics based on the Born rule may not be detectable. Friederich (2021) provides a general argument that the Q-based interpretation is practically indistinguishable from standard quantum mechanics at the level of measurement devices, parallelling the standard argument for the empirical adequacy of Bohmian mechanics, as sketched in the entry on Bohmian mechanics, §10. Interestingly, a version of Bohmian mechanics that also treats the Husimi function as the actual phase space probability distribution was earlier suggested by de Polavieja (1996).

## 7. Objections Against Retrocausality in Quantum Mechanics

This final section reviews some of the most common, and then two of the most significant, objections against the proposal of retrocausality in quantum mechanics.

### 7.1 General Arguments Against Retrocausality

There is a tradition in philosophy for regarding the very idea of retrocausality as incoherent. The most prominent worry (Flew 1954, Black 1956)[^black-1956][^flew-1954], is the so-called “bilking argument” (see the entry on time travel). Imagine a pair of events, a cause, *C*, and an effect, *E*, which we believe to be retrocausally connected (*E* occurs earlier in time than *C*). It seems possible to devise an experiment which could confirm whether our belief in the retrocausal connection is correct or not. Namely, once we had observed that *E* had occurred, we could then set about ensuring that *C* does not occur, thereby breaking any retrocausal connection that could have existed between them. If we were successful in doing this, then the effect would have been “bilked” of its cause.

The bilking argument drives one towards the claim that any belief an agent might hold in the positive retrocausal correlation between event *C* and event *E* is simply false. However, Dummett (1964) disputes that giving up this belief is the only solution to the bilking argument. Rather, according to Dummett, what the bilking argument actually shows is that a set of three conditions concerning the two events, and the agent’s relationship to them, is incoherent:

1. There exists a positive correlation between an event *C* and an event *E*.
2. Event *C* is within the power of an agent to perform.
3. The agent has epistemic access to the occurrence of event *E* independently of any intention to bring it about.

It is interesting to note that these conditions do not specify in which order events *C* and *E* occur. On simple reflection, there is a perfectly natural reason why it is not possible to bilk *future* effects of their causes, since condition (iii) fails to hold for future events: we simply have no access to which future events occur independently of the role we play as causal agents to bring the events about. When we lack that epistemic access to past events, the same route out of the bilking argument becomes available.

Dummett’s defense against the bilking argument is especially relevant to quantum mechanics. In fact, once a suitable specification is made of how condition (iii) can be violated, we find that there exists a strong parallel between the conditions which need to hold to justify a belief in bringing about the past and the structure of quantum mechanics. Price (1996: 174) points out that bilking is impossible in the following circumstances: rather than suppose that a violation of condition (iii) entails that the relevant agent has *no* epistemic access to the relevant past events independently of any intention to bring them about, suppose that the means by which knowledge of these past events is gathered breaks the claimed correlation between the agent’s action and those past events. Such a condition can be stated as follows:

1. The agent can gain epistemic access to the occurrence of event *E* independently of any intention to bring it about and without altering event *E* from what it would have been had no epistemic access been gained.

The significance of this weakened violation of condition (iii) is that it is just the sort of condition one would expect to hold if the system in question were a quantum system. The very nature of quantum mechanics ensures that any claimed positive correlation between the future measurement settings and the hidden variables characterizing a quantum system cannot possibly be bilked of their causes because condition (iv) is perennially violated. Moreover, so long as we subscribe to the epistemic interpretation of the wavefunction, we lack epistemic access to the “hidden” variables of the system and we lack this access *in principle* as a result of the structure of quantum theory.

Another prominent challenge against the very idea of retrocausality is that it inevitably would give rise to vicious causal loops (Mellor 1998)[^mellor-1998]. (See Faye 1994 for a response and the entry on backward causation for a more detailed review of the objections raised against the idea of retrocausality.)[^faye-1994]

### 7.2 Retrocausality Just Is Superdeterminism

Recall (§3.1) that retrocausality can be motivated as an explicit violation of the assumption of measurement independence (Eq. (\ref{eq:independence})) as a means of circumventing Bell’s theorem. But there is another possible mechanism that might underpin violations of measurement independence, namely, superdeterminism. This is the idea that, in the terminology of §3, the joint past of (i) the measurement setting $\alpha$ and (ii) the hidden state of the measured system $\lambda$ determines both of them completely and induces the relevant quantum correlations between them (see the entry on Bell’s Theorem, §8.1.1, and references therein). Hossenfelder (2020) argues against referring to violations of measurement independence as ‘retrocausality’, preferring to consider such violations as exclusively instances of ‘superdeterminism’, since “the idea of a cause propagating back in time is meaningless” (2020:10; see also Hossenfelder and Palmer (2020)). The essential point of contention here, and Hossenfelder points this out explicitly, is that each of retrocausality and superdeterminism invokes a different understanding of the nature of causality.

The characterisation of causality that Hossenfelder (2020: 10) takes to undermine the proposal of retrocausality is that *A* is a cause of *B* if and only if *A* and *B* are correlated and *B* is in the forward lightcone of *A*: “If you think you have a situation where B ”retrocauses“ *A*, then this merely means *A* causes *B*”. In this way, such correlations between events should never be understood as retrocausal, and should always be understood as superdeterministic. This characterization of causality is reminiscent of Hume’s conventionalism about cause and effect, according to which it is simply a matter of terminology that causes must precede their effects (see the entry on Backward Causation, §2.3). As noted in the metaphysical preliminaries set out in §2.1, the conception of causality that most naturally coheres with the proposal of retrocausality is an interventionist one. Hossenfelder acknowledges this, and argues that the reason the interventionist account of causation is inappropriate as a proposal in the quantum context “is that ”agents“ and their ”interventions“ are macroscopic terms that do not appear in quantum mechanics”.

What Hossenfelder’s critique emphasizes is that retrocausality requires a certain package of metaphysical views to be a viable proposal. Hossenfelder’s analysis relies on a conception of causality that is at odds with the interventionist account, especially as understood along perspectival lines, as outlined in §2.1. As a result, a defence of retrocausality against Hossenfelder’s objection would need to defend the fruitfulness of this account of causality.

### 7.3 Retrocausality Requires Fine Tuning

Causal modeling (Spirtes, Glymour, & Scheines 2000; Pearl 2009)[^pearl-2009][^spirtes-2000] is a practice that has arisen from the field of machine learning that consists in the development of algorithms that can automate the discovery of causes from correlations in large data sets. The causal discovery algorithms permit an inference from given statistical dependences and independences between distinct measurable elements of some system to a causal model for that system. As part of the algorithms, a series of constraints must be placed on the resulting models that capture general features that we take to be characteristic of causality. Two of the more significant assumptions are (i) the causal Markov condition, which ensures that every statistical dependence in the data results in a causal dependence in the model—essentially a formalization of Reichenbach’s common cause principle—and (ii) faithfulness, which ensures that every statistical independence implies a causal independence, or no causal independence is the result of a fine-tuning of the model.

It has long been recognized (Butterfield 1992; Hausman 1999; Hausman & Woodward 1999)[^butterfield-1992][^hausman-1999][^hausman-1999-2] that quantum correlations force one to give up at least one of the assumptions usually made in the causal modeling framework. Wood and Spekkens (2015) argue that any causal model purporting to causally *explain* the observed quantum correlations must be fine-tuned (i.e., must violate the faithfulness assumption). More precisely, according to them, since the observed statistical independences in an entangled bipartite quantum system imply no signaling between the parties, when it is then assumed that every statistical independence implies a causal independence (which is what faithfulness dictates), it must be inferred that there can be no (direct or mediated) causal link between the parties. Since there is an observed statistical dependence between the *outcomes* of measurements on the bipartite system, we can no longer account for this dependence with a causal link unless this link is fine tuned to ensure that the no-signaling independences still hold. There is thus a fundamental tension between the observed quantum correlations and the no-signaling requirement, the faithfulness assumption and the possibility of a causal explanation.

Formally, Wood and Spekkens argue that the following three assumptions form an inconsistent set: (i) the predictions of quantum theory concerning the observed statistical dependences and independences are correct; (ii) the observed statistical dependences and independences can be given a causal explanation; (iii) the faithfulness assumption holds. Wood and Spekkens conclude that, since the faithfulness assumption is an indispensable element of causal discovery, the second assumption must yield. The contrapositive of this is that *any* purported causal explanation of the observed correlations in an entangled bipartite quantum system falls afoul of the tension between the no-signaling constraint and no fine tuning and, thus, must violate the assumption of faithfulness. Such causal explanations, so the argument goes, including retrocausal explanations, should therefore be ruled out as viable explanations.

As a brief aside, this fine-tuning worry for retrocausality in the quantum context arises in a more straightforward way. There is no good evidence to suggest that signaling towards the past is possible; that is, there is no retrocausality at the operational level. (Pegg 2006, 2008 argues that this can be explained formally as a result of the completeness condition on the measurement operators, introducing an asymmetry in normalization conditions for preparation and measurement.)[^pegg-2006][^pegg-2008] Yet, despite there being no signaling towards the past, retrocausal accounts assume causal influences towards past. That these causal influences do not show up as statistical dependences exploitable for signaling purposes raises exactly the same fine-tuning worry as Wood and Spekkens raise.

An obvious response to the challenge set by Wood and Spekkens is to simply reject the assumption of faithfulness. But this should not be taken lightly; the intuition behind the faithfulness assumption is basic and compelling. When no statistical correlation exists between the occurrences of a pair of events, there is no reason for supposing there to be a causal connection between them. Conversely, if we were to allow the possibility of a causal connection between statistically uncorrelated events, we would have a particularly hard task determining which of these uncorrelated sets could be harboring a conspiratorial causal connection that hides the correlation. The faithfulness assumption is thus a principle of parsimony—the simplest explanation for a pair of statistically uncorrelated events is that they are causally independent—much the same way that Spekkens’ (2005) definition of contextuality is, too (see §3.2); indeed, Cavalcanti (2018) argues that contextuality can be construed as a form of fine-tuning.

There are, however, well-known examples of systems that potentially show a misapplication of the faithfulness assumption. One such example, originating in Hesslow (1976), involves a contraceptive pill that can cause thrombosis while simultaneously lowering the chance of pregnancy, which can also cause thrombosis. As Cartwright (2001: 246) points out, given the right weight for these process, it is conceivable that the net effect of the pills on the frequency of thrombosis be zero. This is a case of “cancelling paths”, where the effect of two or more causal routes between a pair of variables cancels to achieve statistical independence. In a case such as this, since we can have independent knowledge of the separate causal mechanisms involved here, there are grounds for arguing that there really is a causal connection between the variables despite their statistical independence. Thus, it is certainly possible to imagine a scenario in which the faithfulness assumption could lead us astray. However, in defense of the general principle, an example such as this clearly contains what Wood and Spekkens refer to as fine tuning; the specific weights for these processes would need to match precisely to erase the statistical dependence, and such a balance would generally be thought as unstable (any change in background conditions, etc. would reveal the causal connection in the form of a statistical dependence).

Näger (2016) raises the possibility that unfaithfulness can occur without conspiratorial fine tuning if the unfaithfulness arises in a stable way. In the quantum context, Näger suggests that the fine-tuning mechanism is what he calls “internal cancelling paths”. This mechanism is analogous to the usual cancelling paths scenario, but the path-cancelling mechanism does not manifest at the level of variables, but at the level of values. On this view, such fine tuning would occur as a result of the particular causal and/or nomological process that governs the system, and it is in this sense that the cancelling paths mechanism is internal, and it is the fact that the mechanism is internal that renders the associated fine tuning stable to external disturbances. Thus

> if the laws of nature are such that disturbances always alter the different paths in a balanced way, then it is physically impossible to unbalance the paths. (Näger 2016: 26)[^näger-2016]

The possibility raised by Näger would circumvent the problem that violations of faithfulness ultimately undermine our ability to make suitable inferences of causal independence based on statistical independence by allowing only a specific kind of unfaithfulness—a principled or law-based unfaithfulness that is “internal” and is thus stable to background conditions—which is much less conspiratorial, as the fine-tuning is a function of the specific process involved. Evans (2018) argues that a basic retrocausal model of the sort envisaged by Costa de Beauregard (see §1) employs just such an internal cancelling paths explanation to account for the unfaithful (no signaling) causal channels. See also Almada et al. (2016) for an argument that fine tuning in the quantum context is robust and arises as a result of symmetry considerations. Furthermore, Evans (2021) argues that, to the letter of Wood and Spekkens’ analysis, cases of fine tuning may be more ubiquitous than we suspect, and so we should not be so worried about such quantum cases.

### 7.4 Contextuality for Exotic Causal Structures

Recall (§3.2) that Spekkens’ (2005) claim that no noncontextual ontological model can reproduce the observed statistics of quantum theory based on his principle of parsimony (that there can be no ontological difference without operational difference) was sidestepped by retrocausal approaches due to the explicit assumption of the ontological models framework that the ontic state is independent of the measurement procedure (i.e., that there is no retrocausality). It was noted there the possibility that Spekkens’ principle of parsimony might be recast to apply more generally to retrocausal models. Shrapnel and Costa (2018) achieve just this in a no-go theorem that applies to any exotic causal structure used to sidestep the ontological models framework, including retrocausal accounts, rendering such models contextual after all.

Shrapnel and Costa’s result is based on a generalization of the ontological models framework which replaces the operational preparation, transformation, and measurement procedures with the temporally and causally neutral notions of local controllables and environmental processes that mediate correlations between different local systems, and generate the joint statistics for a set of events. “These include any global properties, initial states, connecting mechanisms, causal influence, or global dynamics” (2018: 5). Furthermore, they replace the ontic state $\lambda$ with the ontic “process” $\omega$:

> our ontic process captures the physical properties of the world that remain invariant under our local operations. That is, although we allow local properties to *change* under specific operations, we wish our *ontic process* to capture those aspects of reality that are independent of this probing. (2018: 8)

As a result, the notion of $\lambda$-mediation (encountered in §4.1) is replaced by the notion of $\omega$-mediation, in which the ontic process $\omega$ completely specifies the properties of the environment that mediate correlations between regions, and screens off outcomes produced by local controllables from the rest of the environment. Shrapnel and Costa (2018: 9) define the notion of “instrument noncontextuality” as a law of parsimony (along the lines of Spekkens’ own definition of noncontextuality): “Operationally indistinguishable pairs of outcomes and local controllables should remain indistinguishable at the ontological level”. They then show that no instrument noncontextual model can reproduce the quantum statistical predictions.

> Crucially, what is contextual is not just the traditional notion of “state”, but any supposedly objective feature of the theory, such as a dynamical law or boundary condition. (2018: 2)

Since preparations, transformations, and measurements have been replaced by local controllables, there is no extra assumption in Shrapnel and Costa’s framework that $\omega$ is correlated with some controllables but independent of others. Thus the usual route out of the ontological models framework, and so the no-go theorems of §3, open to retrocausal approaches—that the framework assumes no retrocausality—is closed off in the Shrapnel-Costa theorem, rendering retrocausal approaches contextual along with the rest of the models captured by the ontological models framework.

This presents a significant worry for retrocausal approaches to quantum theory. If the main motivation for pursing the hypothesis of retrocausality is to recapture in some sense a classical ontology for quantum theory (see §3.4), then the Shrapnel-Costa theorem has made this task either impossible, or beholden to the possibility of some further story explaining how the contextual features of the model arise from some noncontextual footing. On this latter point, it is difficult to see how this story might be told without significantly reducing the ideological economy of the conceptual framework of retrocausality, again jeopardizing a potential virtue of retrocausality (see Evans 2020 for further discussion of this point)[^evans-2020].

As mentioned above (§7.3), contextuality can be construed as a form of fine tuning (Cavalcanti 2018; Adlam 2021)[^adlam-2021][^cavalcanti-2018], especially when the demand for noncontextuality is understood as a requirement of parsimony, as above. The worries raised in this section and the last underline the fact that the challenge to account for various types of fine tuning is the most serious principled obstacle that retrocausal accounts continue to face.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=qm-retrocausality). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/qm-retrocausality/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=qm-retrocausality&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/qm-retrocausality/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- Hossenfelder, Sabine, 2020, “Superdeterminism: A Guide for the Perplexed”, [arXiv:2010.01324](https://arxiv.org/abs/2010.01324) [quant-ph].
- Leifer, Matthew S., 2017, “Time Symmetric Quantum Theory Without Retrocausality? A Reply to Tim Maudlin”, [arXiv:1708.04364](https://arxiv.org/abs/1708.04364) [quant-ph].
- [Retrocausality: A Toy Model](http://demonstrations.wolfram.com/RetrocausalityAToyModel/), contributed by Peter W. Evans after work by Huw Price, Wolfram Demonstrations Project, 7 March 2011. [Requires Wolfram CDF Player]

## Related Entries

Bell’s Theorem | causal models | causation: and manipulability | causation: backward | causation: the metaphysics of | compatibilism | determinism: causal | quantum mechanics | quantum mechanics: Bohmian mechanics | quantum mechanics: Copenhagen interpretation of | quantum mechanics: Kochen-Specker theorem | quantum theory: philosophical issues in | quantum theory: the Einstein-Podolsky-Rosen argument in | time | time: thermodynamic asymmetry in | time travel | time travel: and modern physics

### Acknowledgments

We are grateful to David Miller, Sally Shrapnel, Rod Sutherland, and Ken Wharton for helpful discussion and comments on earlier versions. P.W.E. acknowledges the support of the University of Queensland and the Australian Government through the Australian Research Council’s Discovery Early Career Award scheme (DE170100808). S.F. acknowledges the support of the Netherlands Organization for Scientific Research (NWO), Veni grant 275-20-065.

[^adlam-2018]: Adlam, Emily, 2018, “Spooky Action at a Temporal Distance”, *Entropy*, 20: 41. doi:10.3390/e20010041

[^adlam-2021]: –––, 2021, “Contextuality, Fine-Tuning and Teleological Explanation”, *Foundations of Physics*, 51: 106. doi:10.1007/s10701-021-00516-y

[^adlam-2022]: –––, 2022, “Two roads to retrocausality”, *Synthese*, 200: 422. doi:10.1007/s11229-022-03919-0

[^aharonov-1964]: Aharonov, Yakir, Peter G. Bergmann, and Joel L. Lebowitz, 1964, “Time Symmetry in the Quantum Process of Measurement”, *Physical Review*, 134(6B): B1410–B1416. doi:10.1103/PhysRev.134.B1410

[^aharonov-1991]: Aharonov, Yakir and Lev Vaidman, 1991, “Complete Description of a Quantum System at a given Time”, *Journal of Physics A: Mathematical and General*, 24(10): 2315–2328. doi:10.1088/0305-4470/24/10/018

[^aharonov-2007]: –––, 2007, “The Two-State Vector Formalism: An Updated Review”, in *Time in Quantum Mechanics*, J.G. Muga, R. Sala Mayato, and Í.L. Egusquiza (eds.), (Lecture Notes in Physics 734), Berlin, Heidelberg: Springer Berlin Heidelberg, 399–447. doi:10.1007/978-3-540-73473-4_13

[^allen-2017]: Allen, John-Mark A., Jonathan Barrett, Dominic C. Horsman, Ciarán M. Lee, and Robert W. Spekkens, 2017, “Quantum Common Causes and Quantum Causal Models”, *Physical Review X*, 7(3): 031021. doi:10.1103/PhysRevX.7.031021

[^almada-2016]: Almada, D., K. Ch’ng, S. Kintner, S., B. Morrison, and Ken B. Wharton, 2016, “Are Retrocausal Accounts of Entanglement Unnaturally Fine-tuned?”, *International Journal of Quantum Foundations*, 2(1): 1–16. [[Almada et al. 2016 available online](http://www.ijqf.org/archives/3218)]

[^argaman-2010]: Argaman, Nathan, 2010, “Bell’s Theorem and the Causal Arrow of Time”, *American Journal of Physics*, 78(10): 1007–1013. doi:10.1119/1.3456564

[^aspect-1982]: Aspect, Alain, Jean Dalibard, and Gérard Roger, 1982, “Experimental Test of Bell’s Inequalities Using Time- Varying Analyzers”, *Physical Review Letters*, 49(25): 1804–1807. doi:10.1103/PhysRevLett.49.1804

[^aspect-1982-2]: Aspect, Alain, Philippe Grangier, and Gérard Roger, 1982, “Experimental Realization of Einstein-Podolsky-Rosen-Bohm Gedankenexperiment : A New Violation of Bell’s Inequalities”, *Physical Review Letters*, 49(2): 91–94. doi:10.1103/PhysRevLett.49.91

[^atkinson-2000]: Atkinson, D., 2000, “Quantum Mechanics and Retrocausality”, in Naresh Dadhich, and Ajit Kembhavi (eds.), *The Universe, Visions and Perspectives*, Dordrecht: Kluwer Academic Publishers, pp. 35–50.

[^becker-2018]: Becker, Adam, 2018, “Quantum Time Machine: How the Future Can Change What Happens Now”, *New Scientist*, 14 February 2018.

[^bell-1964]: Bell, John S., 1964, “On the Einstein Podolsky Rosen Paradox”, *Physics Physique Fizika*, 1(3): 195–200. Reprinted in Bell 2004 14–21. doi:10.1103/PhysicsPhysiqueFizika.1.195

[^bell-1966]: –––, 1966, “On the Problem of Hidden Variables in Quantum Mechanics”, *Reviews of Modern Physics*, 38(3): 447–452. Reprinted in Bell 2004, pp. 1–13. doi:10.1103/RevModPhys.38.447

[^bell-1976]: –––, 1976, “The Theory of Local Beables”, *Epistemological Letters*, 9: 11–24. Reprinted in Bell 2004: 52–62. [[Bell 1976available online](https://cds.cern.ch/record/980036/files/197508125.pdf)]

[^bell-1990]: –––, 1990, “La Nouvelle Cuisine”, in A. Sarlemijn, and P. Kroes (eds.), *Between Science and Technology*, Amsterdam: Elsevier, pp. 97–115. Reprinted in Bell 2004: 232–248.

[^bell-2004]: –––, 2004, *Speakable and Unspeakable in Quantum Mechanics: Collected Papers on Quantum Philosophy*, second edition, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511815676

[^berkovitz-2002]: Berkovitz, Joseph, 2002, “On Causal Loops in the Quantum Realm”, in *Non-Locality and Modality*, Tomasz Placek and Jeremy Butterfield (eds.), Dordrecht: Springer Netherlands, 235–257. doi:10.1007/978-94-010-0385-8_16

[^berkovitz-2008]: –––, 2008, “On Predictions in Retro-Causal Interpretations of Quantum Mechanics”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 39(4): 709–735. doi:10.1016/j.shpsb.2008.08.002

[^black-1956]: Black, M., 1956, “Why Cannot an Effect Precede Its Cause?”, *Analysis*, 16(3): 49–58. doi:10.1093/analys/16.3.49

[^bohm-1952a]: Bohm, David, 1952a, “A Suggested Interpretation of the Quantum Theory in Terms of ‘Hidden’ Variables. I”, *Physical Review*, 85(2): 166–179. doi:10.1103/PhysRev.85.166

[^bohm-1952b]: –––, 1952b, “A Suggested Interpretation of the Quantum Theory in Terms of ‘Hidden’ Variables. II”, *Physical Review*, 85(2): 180–193. doi:10.1103/PhysRev.85.180

[^brunner-2014]: Brunner, Nicolas, Daniel Cavalcanti, Stefano Pironio, Valerio Scarani, and Stephanie Wehner, 2014, “Bell Nonlocality”, *Reviews of Modern Physics*, 86(2): 419–478. doi:10.1103/RevModPhys.86.419

[^butterfield-1992]: Butterfield, Jeremy, 1992, “Bell’s Theorem: What It Takes”, *The British Journal for the Philosophy of Science*, 43(1): 41–83. doi:10.1093/bjps/43.1.41

[^cartwright-1979]: Cartwright, Nancy, 1979, “Causal Laws and Effective Strategies”, *Noûs*, 13(4): 419. doi:10.2307/2215337

[^cartwright-2001]: –––, 2001, “What Is Wrong With Bayes Nets?”:, *Monist*, 84(2): 242–264. doi:10.5840/monist20018429

[^cavalcanti-2018]: Cavalcanti, Eric G., 2018, “Classical Causal Models for Bell and Kochen-Specker Inequality Violations Require Fine-Tuning”, *Physical Review X*, 8(2): 021018. doi:10.1103/PhysRevX.8.021018

[^cavalcanti-2014]: Cavalcanti, Eric G and Raymond Lal, 2014, “On Modifications of Reichenbachʼs Principle of Common Cause in Light of Bellʼs Theorem”, *Journal of Physics A: Mathematical and Theoretical*, 47(42): 424018. doi:10.1088/1751-8113/47/42/424018

[^clauser-1969]: Clauser, John F., Michael A. Horne, Abner Shimony, and Richard A. Holt, 1969, “Proposed Experiment to Test Local Hidden-Variable Theories”, *Physical Review Letters*, 23(15): 880–884. doi:10.1103/PhysRevLett.23.880

[^colbeck-2012]: Colbeck, Roger and Renato Renner, 2012, “Is a System’s Wave Function in One-to-One Correspondence with Its Elements of Reality?”, *Physical Review Letters*, 108(15): 150402. doi:10.1103/PhysRevLett.108.150402

[^corry-2015]: Corry, Richard, 2015, “Retrocausal Models for EPR”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 49: 1–9. doi:10.1016/j.shpsb.2014.11.001

[^costa-2016]: Costa, Fabio, and Shrapnel, Sally, 2016, “Quantum Causal Modelling”, *New Journal of Physics*, 18: 063032. doi:10.1088/1367-2630/18/6/063032

[^costa-1953]: Costa de Beauregard, Olivier, 1953, “Mécanique Quantique”, *Comptes Rendus Académie des Sciences*, 236: 1632–1634. [[Costa de Beauregard 1953 available online](https://gallica.bnf.fr/ark:/12148/bpt6k3188h/f1632.item)]

[^costa-1976]: –––, 1976, “Time Symmetry and Interpretation of Quantum Mechanics”, *Foundations of Physics*, 6(5): 539–559. doi:10.1007/BF00715107

[^costa-1977a]: –––, 1977a, “Les duellistes Bell et Clauser-Horne-Shimony (<<C.H.S.>>) s’aveuglent en refusant la <<causalité rétrograde>> inscrite en clair dans le formalisme”, *Epistemological Letters*, 16: 1–8.

[^costa-1977b]: –––, 1977b, “Time Symmetry and the Einstein Paradox”, *Il Nuovo Cimento B*, 42(1): 41–64. doi:10.1007/BF02906749

[^costa-1987a]: –––, 1987a, “On the Zigzagging Causality EPR Model: Answer to Vigier and Coworkers and to Sutherland”, *Foundations of Physics*, 17(8): 775–785. doi:10.1007/BF00733266

[^costa-1987b]: –––, 1987b, *Time, The Physical Magnitude*, Dordrecht: D. Reidel.

[^cramer-1980]: Cramer, John G., 1980, “Generalized Absorber Theory and the Einstein-Podolsky-Rosen Paradox”, *Physical Review D*, 22(2): 362–376. doi:10.1103/PhysRevD.22.362

[^cramer-1986]: –––, 1986, “The Transactional Interpretation of Quantum Mechanics”, *Reviews of Modern Physics*, 58(3): 647–687. doi:10.1103/RevModPhys.58.647

[^cramer-1988]: –––, 1988, “An Overview of the Transactional Interpretation of Quantum Mechanics”, *International Journal of Theoretical Physics*, 27(2): 227–236. doi:10.1007/BF00670751

[^cramer-2016]: –––, 2016, *The Quantum Handshake*, Cham: Springer International Publishing. doi:10.1007/978-3-319-24642-0

[^polavieja-1996]: de Polavieja, Gonzalo G., 1996, “A Causal Quantum Theory in Phase Space”, *Physics Letters A*, 220(6): 303–314. doi:10.1016/0375-9601(96)00523-3

[^dirac-1938]: Dirac, Paul Adrien Maurice, 1938, “Classical Theory of Radiating Electrons”, *Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences*, 167(929): 148–169. doi:10.1098/rspa.1938.0124

[^drummond-2021]: Drummond, Peter, 2021, “Time Evolution with Symmetric Stochastic Action”, *Physical Review Research*, 3(1): 013240. doi:10.1103/PhysRevResearch.3.013240

[^drummond-2020]: Drummond, Peter, and Margaret Reid, 2020, “Retrocausal Model of Reality for Quantum Fields”, *Physical Review Research*, 2(3): 033266. doi:10.1103/PhysRevResearch.2.033266

[^dummett-1964]: Dummett, Michael, 1964, “Bringing About the Past”, *The Philosophical Review*, 73(3): 338. doi:10.2307/2183661

[^einstein-1948]: Einstein, Albert, 1948, “Quanten-Mechanik Und Wirklichkeit”, *Dialectica*, 2(3–4): 320–324. doi:10.1111/j.1746-8361.1948.tb00704.x

[^einstein-1935]: Einstein, Albert, Boris Podolsky, and Nathan Rosen, 1935, “Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?”, *Physical Review*, 47(10): 777–780. doi:10.1103/PhysRev.47.777

[^evans-2015]: Evans, Peter W., 2015, “Retrocausality at No Extra Cost”, *Synthese*, 192(4): 1139–1155. doi:10.1007/s11229-014-0605-0

[^evans-2018]: –––, 2018, “Quantum Causal Models, Faithfulness, and Retrocausality”, *The British Journal for the Philosophy of Science*, 69(3): 745–774. doi:10.1093/bjps/axw037

[^evans-2020]: –––, 2020, “The End of a Classical Ontology for Quantum Mechanics?”, *Entropy*, 23(1): 12. doi:10.3390/e23010012

[^evans-2021]: –––, 2021, “A Sideways Look at Faithfulness for Quantum Correlations”, *The Journal of Philosophy*, 118(1): 28–42. doi:10.5840/jphil202111812

[^evans-2016]: Evans, Peter W., Sean Gryb and Karim P. Y. Thébault, 2016, “$\Psi$-epistemic quantum cosmology?”, *Studies in History and Philosophy of Modern Physics*, 56: 1–12. doi:10.1016/j.shpsb.2016.10.005

[^evans-2013]: Evans, Peter W., Huw Price, and Ken B. Wharton, 2013, “New Slant on the EPR-Bell Experiment”, *The British Journal for the Philosophy of Science*, 64(2): 297–324. doi:10.1093/bjps/axr052

[^faye-1994]: Faye, Jan, 1994, “Causal Beliefs and their Justification”, in *Logic and Causal Reasoning*, Jan Faye, Uwe Scheffler, and Max Urchs (eds.), Berlin: Akademie Verlag, pp. 141–168.

[^feynman-1942]: Feynman, Richard P., 1942 [2005], “The Principle of Least Action in Quantum Mechanics”, PhD Thesis, Princeton University. Reprinted in *Feynman’s Thesis: A New Approach to Quantum Theory*, Laurie M. Brown (ed.), Singapore: World Scientific Publishing, 2005, pp. 1–69. [[Feynman 1942 available online](https://cds.cern.ch/record/101498/files/Thesis-1942-Feynman.pdf)]

[^flew-1954]: Flew, Antony, 1954, “Can an Effect Precede its Cause?”, *Proceedings of the Aristotelian Society*, 28(Supplement): 45–62.

[^freedman-1972]: Freedman, Stuart J. and John F. Clauser, 1972, “Experimental Test of Local Hidden-Variable Theories”, *Physical Review Letters*, 28(14): 938–941. doi:10.1103/PhysRevLett.28.938

[^friederich-2021]: Friederich, Simon, 2021, “Introducing the Q-based interpretation of quantum mechanics”, *The British Journal for the Philosophy of Science*, online first. doi:10.1086/716196

[^frisch-2014]: Frisch, Mathias, 2014, *Causal Reasoning in Physics*, Cambridge: Cambridge University Press.

[^ghirardi-1986]: Ghirardi, G. C., A. Rimini, and T. Weber, 1986, “Unified Dynamics for Microscopic and Macroscopic Systems”, *Physical Review D*, 34(2): 470–491. doi:10.1103/PhysRevD.34.470

[^goldstein-2011]: Goldstein, Sheldon, Travis Norsen, Daniel Tausk, and Nino Zanghi, 2011, “Bell’s Theorem”, *Scholarpedia*, 6(10): 8378. doi:10.4249/scholarpedia.8378

[^greenberger-1989]: Greenberger, Daniel M., Michael A. Horne, and Anton Zeilinger, 1989, “Going Beyond Bell’s Theorem”, in *Bell’s Theorem, Quantum Theory and Conceptions of the Universe*, Menas Kafatos (ed.), Dordrecht: Springer Netherlands, 69–72. doi:10.1007/978-94-017-0849-4_10

[^hardy-2013]: Hardy, Lucien, 2013, “Are Quantum States Real?”, *International Journal of Modern Physics B*, 27(01n03): 1345012. doi:10.1142/S0217979213450124

[^harrigan-2010]: Harrigan, Nicholas and Robert W. Spekkens, 2010, “Einstein, Incompleteness, and the Epistemic View of Quantum States”, *Foundations of Physics*, 40(2): 125–157. doi:10.1007/s10701-009-9347-0

[^hausman-1999]: Hausman, Daniel M., 1999, “Lessons From Quantum Mechanics”, *Synthese*, 121(1/2): 79–92. doi:10.1023/A:1005281714660

[^hausman-1999-2]: Hausman, Daniel M. and James Woodward, 1999, “Independence, Invariance and the Causal Markov Condition”, *The British Journal for the Philosophy of Science*, 50(4): 521–583. doi:10.1093/bjps/50.4.521

[^hermens-2011]: Hermens, Ronnie, 2011, “The Problem of Contextuality and the Impossibility of Experimental Metaphysics Thereof”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 42(4): 214–225. doi:10.1016/j.shpsb.2011.06.001

[^hesslow-1976]: Hesslow, Germund, 1976, “Two Notes on the Probabilistic Approach to Causality”, *Philosophy of Science*, 43(2): 290–292. doi:10.1086/288684

[^hokkyo-1988]: Hokkyo, Noboru, 1988, “Variational Formulation of Transactional and Related Interpretations of Quantum Mechanics”, *Foundations of Physics Letters*, 1(3): 293–299. doi:10.1007/BF00690070

[^hossenfelder-2020]: Hossenfelder, Sabine and Tim Palmer, 2020, “Rethinking Superdeterminism”, *Frontiers in Physics*, 8: 139. 10.3389/fphy.2020.00139

[^hossenfelder-2008]: –––, 2008, “Retrocausation Acting in the Single-Electron Double-Slit Interference Experiment”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 39(4): 762–766. doi:10.1016/j.shpsb.2008.05.001

[^husimi-1940]: Husimi, Kôdi, 1940, “Some Formal Properties of the Density Matrix”, *Proceedings of the Physico-Mathematical Society of Japan*, 22(4): 264–314.

[^ismael-2016]: Ismael, Jenann, 2016, “How Do Causes Depend on Us? The Many Faces of Perspectivalism”, *Synthese*, 193(1): 245–267. doi:10.1007/s11229-015-0757-6

[^kastner-2006]: Kastner, Ruth E., 2006, “Cramer’s Transactional Interpretation and Causal Loop Problems”, *Synthese*, 150(1): 1–14. doi:10.1007/s11229-004-6264-9

[^kastner-2013]: –––, 2013, *The Transactional Interpretation of Quantum Mechanics: The Reality of Possibility*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511675768

[^kochen-1967]: Kochen, Simon and E.P. Specker, 1967, “The Problem of Hidden Variables in Quantum Mechanics”, *Journal of Mathematics and Mechanics*, 17(1): 59–87.

[^leifer-2014]: Leifer, Matthew Saul, 2014, “Is the Quantum State Real? An Extended Review of ψ-Ontology Theorems”, *Quanta*, 3(1): 67. doi:10.12743/quanta.v3i1.22

[^leifer-2017]: Leifer, Matthew S. and Matthew F. Pusey, 2017, “Is a Time Symmetric Interpretation of Quantum Theory Possible without Retrocausality?”, *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Science*, 473(2202): 20160607. doi:10.1098/rspa.2016.0607

[^leifer-2013]: Leifer, Matthew S. and Robert W. Spekkens, 2013, “Towards a Formulation of Quantum Theory as a Causally Neutral Theory of Bayesian Inference”, *Physical Review A*, 88(5): 052130. doi:10.1103/PhysRevA.88.052130

[^lewis-1926]: Lewis, G. N., 1926, “The Nature of Light”, *Proceedings of the National Academy of Sciences*, 12(1): 22–29. doi:10.1073/pnas.12.1.22

[^lewis-2013]: Lewis, Peter J., 2013, “Retrocausal Quantum Mechanics: Maudlin’s Challenge Revisited”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 44(4): 442–449. doi:10.1016/j.shpsb.2013.09.004

[^marchildon-2006]: Marchildon, Louis, 2006, “Causal Loops and Collapse in the Transactional Interpretation of Quantum Mechanics”., *Physics Essays*, 19(3): 422–429. doi:10.4006/1.3025811

[^maudlin-2011]: Maudlin, Tim, 2011, *Quantum Non-Locality and Relativity: Metaphysical Intimations of Modern Physics*, third edition, Malden, MA: Wiley-Blackwell.

[^mellor-1998]: Mellor, D. H., 1998, *Real Time II*, London: Routledge.

[^miller-1996]: Miller, D.J., 1996, “Realism and Time Symmetry in Quantum Mechanics”, *Physics Letters A*, 222(1–2): 31–36. doi:10.1016/0375-9601(96)00620-2

[^miller-1997]: –––, 1997, “Conditional Probabilities in Quantum Mechanics from a Time-Symmetric Formulation”, *Il Nuovo Cimento B*, 112(12): 1577–1592. [[Miller 1997 available online](https://www.sif.it/riviste/sif/ncb/econtents/1997/112/12/article/6)]

[^näger-2016]: Näger, Paul M., 2016, “The Causal Problem of Entanglement”, *Synthese*, 193(4): 1127–1155. doi:10.1007/s11229-015-0668-6

[^norsen-2011]: Norsen, Travis, 2011, “John S. Bell’s Concept of Local Causality”, *American Journal of Physics*, 79(12): 1261–1275. doi:10.1119/1.3630940

[^pearl-2009]: Pearl, Judea, 2009, *Causality: Models, Reasoning, and Inference*, second edition, New York: Cambridge University Press.

[^pegg-2006]: Pegg, David T., 2006, “Causality in Quantum Mechanics”, *Physics Letters A*, 349(6): 411–414. doi:10.1016/j.physleta.2005.09.061

[^pegg-2008]: –––, 2008, “Retrocausality and Quantum Measurement”, *Foundations of Physics*, 38(7): 648–658. doi:10.1007/s10701-008-9224-2

[^price-1984]: Price, Huw, 1984, “The Philosophy and Physics of Affecting the Past”, *Synthese*, 61(3): 299–323. doi:10.1007/BF00485056

[^price-1994]: –––, 1994, “A Neglected Route to Realism about Quantum Mechanics”, *Mind*, 103(411): 303–336. doi:10.1093/mind/103.411.303

[^price-1996]: –––, 1996, *Time’s Arrow & Archimedes’ Point: New Directions for the Physics of Time*, Oxford: Oxford University Press. doi:10.1093/acprof:oso/9780195117981.001.0001

[^price-1997]: –––, 1997, “Time Symmetry in Microphysics”, *Philosophy of Science*, 64: S235–S244. doi:10.1086/392603

[^price-2001]: –––, 2001, “Backward Causation, Hidden Variables and the Meaning of Completeness”, *Pramana: Journal of Physics*, 56(2–3): 199–209. doi:10.1007/s12043-001-0117-6

[^price-2007]: –––, 2007, “Causal Perspectivalism”, in Price and Corry 2007: 250–292.

[^price-2008]: –––, 2008, “Toy Models for Retrocausality”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 39(4): 752–761. doi:10.1016/j.shpsb.2008.05.006

[^price-2012]: –––, 2012, “Does Time-Symmetry Imply Retrocausality? How the Quantum World Says ‘Maybe’?”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 43(2): 75–83. doi:10.1016/j.shpsb.2011.12.003

[^price-2007-2]: Price, Huw and Richard Corry, 2007, *Causation, Physics, and the Constitution of Reality: Russell’s Republic Revisited*, Oxford: Oxford University Press.

[^price-2010]: Price, Huw and Brad Weslake, 2010, “The Time‐Asymmetry of Causation”, in *The Oxford Handbook of Causation*, Helen Beebee, Christopher Hitchcock, and Peter Menzies (eds.), New York: Oxford University Press, chapter 20, 414–443. doi:10.1093/oxfordhb/9780199279739.003.0021

[^price-2015]: Price, Huw and Ken Wharton, 2015, “Disentangling the Quantum World”, *Entropy*, 17(12): 7752–7767. doi:10.3390/e17117752

[^price-2021]: –––, 2021, “Entanglement Swapping and Action at a Distance”, *Foundations of Physics*, 51: 105. doi:10.1007/s10701-021-00511-3

[^pusey-2012]: Pusey, Matthew F., Jonathan Barrett, and Terry Rudolph, 2012, “On the Reality of the Quantum State”, *Nature Physics*, 8(6): 475–478. doi:10.1038/nphys2309

[^quine-1951]: Quine, W. V., 1951, “Ontology and Ideology”, *Philosophical Studies*, 2(1): 11–15. doi:10.1007/BF02198233

[^rietdijk-1978]: Rietdijk, C. W., 1978, “Proof of a Retroactive Influence”, *Foundations of Physics*, 8(7–8): 615–628. doi:10.1007/BF00717585

[^ringbauer-2017]: Ringbauer, Martin, 2017, “On the Reality of the Wavefunction”, in *Exploring Quantum Foundations with Single Photons*, by Martin Ringbauer, Cham: Springer International Publishing, 85–136. doi:10.1007/978-3-319-64988-7_4

[^russell-1913]: Russell, Bertrand, 1913, “On the Notion of Cause”, *Proceedings of the Aristotelian Society*, 13(1): 1–26. doi:10.1093/aristotelian/13.1.1

[^shrapnel-2018]: Shrapnel, Sally and Fabio Costa, 2018, “Causation Does Not Explain Contextuality”, *Quantum*, 2: 63. doi:10.22331/q-2018-05-18-63

[^schulman-1997]: Schulman, Lawrence S., 1997, *Time’s Arrows and Quantum Measurement*, Cambridge: Cambridge University Press. doi:10.1017/CBO9780511622878

[^schulman-2012]: –––, 2012, “Experimental Test of the ‘Special State’ Theory of Quantum Measurement”, *Entropy*, 14(4): 665–686. doi:10.3390/e14040665

[^silberstein-2008]: Silberstein, Michael, Michael Cifone, and William Mark Stuckey, 2008, “Why Quantum Mechanics Favors Adynamical and Acausal Interpretations Such as Relational Blockworld over Backwardly Causal and Time-Symmetric Rivals”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 39(4): 736–751. doi:10.1016/j.shpsb.2008.07.005

[^silberstein-2018]: Silberstein, Michael, W.M. Stuckey, and Timothy McDevitt, 2018, *Beyond the Dynamical Universe: Unifying Block Universe Physics and Time as Experienced*, Oxford: Oxford University Press. doi:10.1093/oso/9780198807087.001.0001

[^spekkens-2005]: Spekkens, Robert W., 2005, “Contextuality for Preparations, Transformations, and Unsharp Measurements”, *Physical Review A*, 71(5): 052108. doi:10.1103/PhysRevA.71.052108

[^spekkens-2007]: –––, 2007, “Evidence for the Epistemic View of Quantum States: A Toy Theory”, *Physical Review A*, 75(3): 032110. doi:10.1103/PhysRevA.75.032110

[^spirtes-2000]: Spirtes, Peter, Clark N. Glymour, and Richard Scheines, 2000, *Causation, Prediction, and Search*, second edition, (Adaptive Computation and Machine Learning), Cambridge, MA: MIT Press.

[^stuckey-2008]: Stuckey, W. M., Michael Silberstein, and Michael Cifone, 2008, “Reconciling Spacetime and the Quantum: Relational Blockworld and the Quantum Liar Paradox”, *Foundations of Physics*, 38(4): 348–383. doi:10.1007/s10701-008-9206-4

[^stuckey-2015]: Stuckey, W.M., Michael Silberstein, and Timothy McDevitt, 2015, “Relational Blockworld: Providing a Realist Psi-Epistemic Account of Quantum Mechanics”, *International Journal of Quantum Foundations*, 1(3): 123–170. [[Stuckey et al. 2015 available online](https://www.ijqf.org/archives/2402)]

[^sutherland-1983]: Sutherland, Roderick Ian, 1983, “Bell’s Theorem and Backwards-in-Time Causality”, *International Journal of Theoretical Physics*, 22(4): 377–384. doi:10.1007/BF02082904

[^sutherland-1985]: –––, 1985, “A Corollary to Bell’s Theorem”, *Il Nuovo Cimento B*, Series 11, 88(2): 114–118. doi:10.1007/BF02728894

[^sutherland-1989]: –––, 1989, “Implications of a Causality Paradox Related to Bell–s Theorem”, *Il Nuovo Cimento B*, Series 11, 104(1): 29–33. doi:10.1007/BF02742823

[^sutherland-2008]: –––, 2008, “Causally Symmetric Bohm Model”, *Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics*, 39(4): 782–805. doi:10.1016/j.shpsb.2008.04.004

[^sutherland-2015]: –––, 2015, “Lagrangian Description for Particle Interpretations of Quantum Mechanics: Single-Particle Case”, *Foundations of Physics*, 45(11): 1454–1464. doi:10.1007/s10701-015-9918-1

[^sutherland-2017]: –––, 2017, “How Retrocausality Helps”, *AIP Conference Proceedings*, 1841(1): 020001. doi:10.1063/1.4982765

[^tetrode-1922]: Tetrode, H., 1922, “Über den Wirkungszusammenhang der Welt. Eine Erweiterung der klassischen Dynamik”, *Zeitschrift für Physik*, 10(1): 317–328. doi:10.1007/BF01332574

[^watanabe-1955]: Watanabe, Satosi, 1955, “Symmetry of Physical Laws. Part III. Prediction and Retrodiction”, *Reviews of Modern Physics*, 27(2): 179–186. doi:10.1103/RevModPhys.27.179

[^wharton-2007]: Wharton, Ken B., 2007, “Time-Symmetric Quantum Mechanics”, *Foundations of Physics*, 37(1): 159–168. doi:10.1007/s10701-006-9089-1

[^wharton-2010a]: –––, 2010a, “A Novel Interpretation of the Klein-Gordon Equation”, *Foundations of Physics*, 40(3): 313–332. doi:10.1007/s10701-009-9398-2

[^wharton-2010b]: –––, 2010b, “Time-Symmetric Boundary Conditions and Quantum Foundations”, *Symmetry*, 2(1): 272–283. doi:10.3390/sym2010272

[^wharton-2013]: –––, 2013, “The Universe Is Not a Computer”, *New Scientist*, 217(2903): 30–31. doi:10.1016/S0262-4079(13)60354-1

[^wharton-2014]: –––, 2014, “Quantum States as Ordinary Information”, *Information*, 5(1): 190–208. doi:10.3390/info5010190

[^wharton-2016]: –––, 2016, “Towards a Realistic Parsing of the Feynman Path Integral”, *Quanta*, 5(1): 1. doi:10.12743/quanta.v5i1.41

[^wharton-2018]: –––, 2018, “A New Class of Retrocausal Models”, *Entropy*, 20(6): 410. doi:10.3390/e20060410

[^wharton-2020]: Wharton, Ken B. and Nathan Argaman,, 2020, “Colloquium: Bell’s theorem and locally mediated reformulations of quantum mechanics”, *Reviews of Modern Physics*, 92(2): 021002. doi:10.1103/RevModPhys.92.021002

[^wharton-2011]: Wharton, Ken B., David J. Miller, and Huw Price, 2011, “Action Duality: A Constructive Principle for Quantum Foundations”, *Symmetry*, 3(3): 524–540. doi:10.3390/sym3030524

[^wheeler-1945]: Wheeler, John Archibald and Richard Phillips Feynman, 1945, “Interaction with the Absorber as the Mechanism of Radiation”, *Reviews of Modern Physics*, 17(2–3): 157–181. doi:10.1103/RevModPhys.17.157

[^wheeler-1949]: –––, 1949, “Classical Electrodynamics in Terms of Direct Interparticle Action”, *Reviews of Modern Physics*, 21(3): 425–433. doi:10.1103/RevModPhys.21.425

[^wigner-1932]: Wigner, Eugene, 1932, “On the Quantum Correction for Thermodynamic Equilibrium”, *Physical Review*, 40: 033002. doi:10.1088/1367-2630/17/3/033002

[^wigner-1932-2]: –––, 1932, “On the quantum correction for thermodynamic equilibrium”, *Physical Review*, 40: 749–759.

[^wiseman-2017]: Wiseman, Howard M. and Eric G. Cavalcanti, 2017, “*Causarum Investigatio* and the Two Bell’s Theorems of John Bell”, in *Quantum [Un]Speakables II: Half a Century of Bell’s Theorem*, Reinhold Bertlmann and Anton Zeilinger (eds.), Cham: Springer International Publishing, 119–142. doi:10.1007/978-3-319-38987-5_6

[^wood-2015]: Wood, Christopher J and Robert W Spekkens, 2015, “The Lesson of Causal Discovery Algorithms for Quantum Correlations: Causal Explanations of Bell-Inequality Violations Require Fine-Tuning”, *New Journal of Physics*, 17(3): 033002. doi:10.1088/1367-2630/17/3/033002

[^woodward-2003]: Woodward, James, 2003, *Making Things Happen: A Theory of Causal Explanation*, New York: Oxford University Press. doi:10.1093/0195155270.001.0001

[^woodward-2007]: –––, 2007, “Causation with a Human Face”, in Price and Corry 2007: Chapter 4, pp. 66–105.
