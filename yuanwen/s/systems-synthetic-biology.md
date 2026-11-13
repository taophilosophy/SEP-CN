# Philosophy of Systems and Synthetic Biology
**First published Thu Jun 8, 2017; substantive revision Wed May 11, 2022**

*Green, Sara*

This entry aims to clarify how systems and synthetic biology contribute to and extend discussions within philosophy of science. Unlike fields such as developmental biology or molecular biology, systems and synthetic biology are not easily demarcated by a focus on a specific subject area or level of organization. Rather, they are characterized by the development and application of mathematical, computational, and synthetic modeling strategies in response to complex problems and challenges within the life sciences. Proponents of systems and synthetic biology often stress the necessity of a perspective that goes beyond the scope of molecular biology and genetic engineering, respectively. With the emphasis on systems and interaction networks, the approaches explicitly engage in one of the oldest philosophical discussions on reductionism vs. holism. Moreover, by pursuing ambitious aims such as the development of multiscale computational models and synthetic life forms, they uncover new ground for philosophical analysis. Systems and synthetic biology raise fundamental questions about how far research can be taken through computational approaches, about the relation between living and artificial systems, and about the implications of interdisciplinary research for science and society.

## 1. Introduction

Systems biology and synthetic biology are relatively recent interdisciplinary approaches that aim to improve our ability to understand, predict, and control living systems. They both capitalize on large-scale data production in genomics and related fields and explore new paths of cross-fertilization between biology and non-biological disciplines such as physics, computer science, mathematics, chemistry, and engineering. Systems and synthetic biology are often described as ‘sister-disciplines’ or ‘cousins’, focusing on the complementary and interrelated aims of *understanding* (systems biology) and *designing* (synthetic biology) living systems. Accordingly, they have been associated with knowledge-driven versus application-driven epistemologies, or with the aims of analysis versus synthesis. Philosophers of science examining the research practice have, however, argued that understanding and design are often interdependent, and that no simple distinction between basic and applied science can be made in this context (Kastenhofer 2013a,b; Knuuttila & Loettgers 2013a; O’Malley 2009)[^kastenhofer-2013a][^knuuttila-2013a][^o’malley-2009]. Moreover, the notions of systems and synthetic biology cover broad and highly diverse spectra of interdisciplinary hybrids (Calvert & Fujimura 2011; Gramelsberger et al. 2013)[^calvert-2011][^gramelsberger-2013][^gramelsberger-2013-2]. This entry will therefore aim to reach a balance between displaying the methodological flexibility and variability within these fields and highlighting common themes.

### 1.1 Research Practices in Systems Biology

Systems biology can be interpreted as a response to limitations of research strategies investigating molecules and pathways in isolation. To clarify the significance of their approach, systems biologists often stress the need to complement or go beyond what is perceived as reductionist strategies in molecular biology (De Backer et al. 2004; van Regenmortel 2004)[^regenmortel-2004]. The contrast between systems biology and molecular biology should not be overstated (see also Section 4.1). However, the contrasting comparison reveals how systems biology is motivated by the need for a theoretical framework that is better suited for studying the dynamics and organization of many interconnected components (Boogerd et al. 2007; Kitano 2001)[^boogerd-2007][^kitano-2001].

Molecular biology has been extremely successful in generating knowledge on biological mechanisms through the twin strategies of decomposition and localization of component parts and molecular operations (Bechtel & Richardson 1993 [2010])[^bechtel-1993]. But the very success of the detailed study of molecular pathways has also revealed dynamic interfaces and crosslinks between processes and components that were previously assigned to distinct mechanisms or subsystems. To account for a vast number of interacting components and multiple feedback loops dynamic modeling is needed (Bechtel & Abrahamsen 2012)[^bechtel-2012]. Network modeling and computational simulations in systems biology allow for the study of larger integrated systems and thus provide strategies for *recomposing* the findings in the context of larger systems (Bechtel 2016; Gross & Green 2017)[^bechtel-2016][^green-2017][^gross-2017][^gross-2017-2]. *Systems* are in this context generally understood as large networks of integrated components exhibiting non-linear dynamics. However, there is no unified view of what constitutes a systems-approach (Calvert 2010; Calvert & Fujimura 2011)[^calvert-2010][^calvert-2011]. As clarified below, systems biology comprises different research practices with different ties to molecular biology, genomics, as well as to non-biological disciplines (see also Krohs & Callebaut 2007)[^krohs-2007].

Systems biology research is sometimes divided into a *systems-theoretical* and a *pragmatic* stream (O’Malley and Dupré 2005)[^o’malley-2005]. The former is historically related to the initial use of the term ‘systems biology’ in 1968, denoting the merging of systems theory and biology (Mesarović 1968)[^mesarović-1968].[^note-1] This definition has been taken up as providing a theoretical vision and reorientation also for modern systems biology (Wolkenhauer & Mesarović 2005; Drack & Wolkenhauer 2011)[^drack-2011][^wolkenhauer-2005]. Systems-theoretical proponents view systems biology as an opportunity to revive important theoretical questions that for half a century stood in the shade of the success of experimental biology. Examples of such questions are what characterizes living systems and whether generic organizational principles can be identified (see Section 3.2). In contrast, the *pragmatic stream* views systems biology as a successor of genomics and as a powerful extension of molecular biology. This stream is sometimes referred to as molecular systems biology (De Backer et al. 2010), and practitioners within this field relate the emergence of systems biology to the production of data within genomics and other high-throughput technologies from the late 1990s and onwards (Güttinger & Dupré 2016)[^güttinger-2016].

Krohs and Callebaut (2007) consider omics-disciplines a third dimension or root of systems biology due to the impact of data-rich modeling strategies on the development of the approach.[^note-2] Omics fields allow for large-scale measurements of relations between vast number of molecular components (e.g., genes or associated protein concentrations). Since modeling tools in molecular biology have limited capacity for handling large quantitative datasets, researchers turned to the exploration and further development of mathematical and computational strategies developed in engineering and physics (Alberghina & Westerhoff 2005)[^alberghina-2005].

Although not all systems biologists put equal emphasis on the prospects of big data, there is a general acceptance in the community that mathematical and computational approaches are required to account for biological complexity. The first international conference on systems biology was held in 2000 (at the first Systems Biology Institute in Tokyo), and thematic journal issues and dedicated journals quickly followed (Kitano 2002a,b)[^kitano-2002a]. Since then, many systems biology research institutions have emerged, and large-scale international collaborations have been initiated.

#### 1.1.1 Network Approaches in Systems Biology

What is distinctive about systems biology can in part be understood through the characteristics and implications of different styles of representation. Whereas textbooks and research papers in molecular and cell biology typically contain mechanistic diagrams tracking interactions between specific genes and proteins, representations in systems biology often display interactions between a vast number of molecular components as abstract networks of interconnected nodes and links. This difference in representational style is epistemically significant, because it highlights an increasing focus on the *organizational structure* of the system as a whole.

By conducting correlation-based studies of how multiple genes and proteins are associated with each other, and how these are connected to specific biological processes, systems biology research has revealed common patterns in biological networks such as scale-free network architectures and multi-level hierarchies (Ravasz et al. 2002)[^ravasz-2002]. Systems biologists often distinguish between two major classes of networks based on their connectivity distribution (how components, or *nodes*, in the network are connected to other nodes). *Exponential* and *scale-free network* structures are illustrated on Figure 1 (for details on the differences, see Albert et al. 2000)[^albert-2000]. An exponential network is largely homogeneous with approximately the same number of links per node, and it is unlikely to find nodes with many links. In contrast, scale-free networks are inhomogeneous. Most nodes have only a few links but some nodes (called hubs) have a large number of connections.[^note-3]

*Figure 1:*

![[subfigre a labeled 'Exponential' and subfigure b labeled 'Scale-free']](../assets/systems-synthetic-biology/Figure1.jpg)

Figure 1: An example of a network representation in systems biology, showing the difference between an *exponential network* and a *scale-free network*. Red nodes are the five nodes with most links, green nodes are the first neighbors of red nodes (from Albert et al. 2000: 379, reprinted by permission from Macmillan Publishers Ltd: Nature, copyright 2000)[^albert-2000].

Interestingly, many real-world networks such as social networks, the World Wide Web, and regulatory networks in biology display scale-free architectures. This raises important questions about whether real-world networks can be related to more generic *structural types* with characteristic functional capacities. For example, the scale-free structure makes the average path length between any two nodes in the network small, and this structure has therefore been associated with capacities for coordinated regulation throughout the network (Albert et al. 2000)[^albert-2000]. Moreover, scale-free networks exhibit a high error tolerance, understood as robustness against failure of random nodes and links (e.g., random gene deletion). These functional properties are not shared by exponential networks, and illustrate some advantages of the scale-free structure. However, the functional importance of hubs in scale-free networks at the same time results in fragility to attacks on central notes (Albert et al. 2000; Barabási & Oltvai 2004)[^albert-2000][^barabási-2004]. Similarly, a multi-layered network structure called a *bow-tie network* connects many inputs and outputs through a central core (the knot of the bow-tie) that consists of a small number of elements (Kitano & Oda 2006)[^kitano-2006]. This structure has been associated with efficient information flow, but also with fragility towards perturbations of the intermediate nodes in the core of the network.

Some systems biologists examine network architectures in the hope that smaller functional units or patterns can be identified that are akin to modules in electronic networks (Hartwell et al. 1999)[^hartwell-1999]. One example of pattern-detection within large datasets has received special attention from philosophers of science, namely research on so-called *network motifs*. Network motifs are defined as “patterns of interaction that recurs in a network in many contexts” (Alon 2007: 268)[^alon-2007]. By comparing the gene regulatory network of the bacterium *E. coli* to random networks, it was discovered that a few circuit patterns occurred more frequently than expected by chance (Shen-Orr et al. 2002)[^shen-orr-2002]. Statistically significant circuits were defined as network motifs. Two examples of network motifs are shown in Figure 2, called coherent and incoherent feedforward loops (cFFL and iFFL).

*Figure 2:*

![[two diagrams. The top one is labeled 'Coherent FFL' and has an X with an arrow to the right pointing to a Y another arrow to the right goes from Y to a Z; this arrow is labeled 'Indirect'. The Z has a (+) to its left and also below. A third arrow goes from X down then to the right before going up to the Z; this arrow is labeled 'Direct'. The bottom diagram is the same except the overall label is 'Incoherent FFL', the (+) to the left of Z is replaced by (-), and the line from Y to Z is not an arrow but rather ends in vertical bar]](../assets/systems-synthetic-biology/Figure2.svg)

Figure 2: Two examples of network motifs, the coherent and incoherent feedforward loop (cFFL and iFFL). The diagrams represent the regulation of a gene Z, via a direct path between a transcription factor X to Z, and an indirect connection from X via another gene or transcription factor Y to Z. Arrows represent gene activation (+) and a vertical bar inactivation (-). In a coherent feedforward loop (cFFL), all connections are activating. In the incoherent feedforward loop (iFFL), the path from Y to Z inhibites gene expression. (Adapted from Alon 2007: 47)[^alon-2007].

Akin to common circuit types in electronic networks, it was hypothesized that the recurring wiring patterns may indicate generalizable functional behaviors. Mathematical analysis suggested that the cFFL may function as a sign-sensitive delay element that filters out noisy inputs for gene activation (e.g., sporadic levels of nutrients in the environment). In contrast, the regulatory function of the iFFL was hypothesized to be an accelerator that creates a rapid pulse of gene expression in response to an activation signal. These predicted functions have been experimentally demonstrated in living bacteria (Mangan et al. 2003)[^mangan-2003]. Moreover, similar and additional network motifs have been found in other species and in other regulatory networks important to cell-signaling, metabolism, and developmental processes (Alves & Sorribas 2011; Peter & Davidson 2015; Tyson & Novák 2010)[^alves-2011][^peter-2015][^tyson-2010]. Such results have sparked interesting debates on whether network motifs could be seen as *design principles*, whose functions are generalizable across different biological contexts (see Section 2.3).

Philosophers and scientists alike have debated the implications of research focusing on generic properties of biological networks, rather than the properties of specific molecular components (e.g., Barabási 2002; Bechtel 2015a,b; Craver 2016)[^barabási-2002][^bechtel-2015a][^craver-2016]. Among the controversial issues is how the enhanced focus on topological properties relates to more traditional mechanistic explanations in biology (Section 4.2). A related issue is whether functional capacities can be derived from an analysis of network architectures alone. Some systems biologists and philosophers have pointed to the limitations and possible biases associated with inferences of functions from automated pattern-detection in datasets (Calvert 2012; Keller 2005; Krohs 2012; see also Prill et al. 2010)[^calvert-2012][^keller-2005][^krohs-2012][^prill-2010]. Specifically, some have called for a more dynamic approach that can account for the context of the whole network and how it changes over time.

Network models are also used to study *temporal* aspects of coordinated processes in cells and the evolutionary dynamics and stability of gene regulatory networks (de Lichtenberg et al. 2005; Hogeweg 2012; Knight & Pinney 2009)[^lichtenberg-2005][^hogeweg-2012]. Of scientific as well as philosophical relevance is whether and how network approaches can extend mechanistic strategies by identifying how multiple biological processes are organized and coordinated in time (Green et al. 2018; Bechtel 2020)[^bechtel-2020][^green-2018][^green-2018-2], or, alternatively, provide new types of explanations (Kostić et al. 2020; Suárez & Deulofeu 2019)[^kostić-2020][^kostić-2020-2][^suárez-2019]. This topic will be further discussed in Section 4.2.

#### 1.1.2 Research Objectives and Recent Developments

Whereas some engineering-inspired systems biologists search for functional units or modules in biological networks, another line of research emphasizes the need for a ‘global’ approach inspired by dynamical systems theory (Huang et al. 2009; Jaeger & Crombach 2012)[^huang-2009][^jaeger-2012]. Drawing on Waddington’s idea of the epigenetic landscape of cell differentiation, the global approach represents dynamical states in a network through vectors, attractors, and trajectories in a state space (Huang 2012; for a philosophical analysis, see Fagan 2012)[^fagan-2012][^huang-2012]. The framework explores how inherent mathematical properties of the network architectures may constrain developmental and evolutionary processes, in a way analogous to how laws of motion constrain the possible planetary movements (Goodwin et al. 1993)[^goodwin-1993]. The global approach is sometimes highlighted as being in opposition to mechanistic or “modular” engineering approaches (Huang 2011; Fagan 2016)[^fagan-2016][^huang-2011]. Controversies of this kind can reveal interesting differences in research aims as well as different standards for models and explanation present in systems biology (Section 5.1).

Some systems biologists describe their approach as one occupied with *functional*, rather than evolutionary questions (Boogerd et al. 2007; Hofmeyr 2007)[^boogerd-2007][^hofmeyr-2007]. By stressing the autonomy of functional biology, beyond discussions of selected effects, philosophy of systems biology can help balance the extensive emphasis on evolutionary biology in philosophy of biology (Pradeu 2016)[^pradeu-2016]. At the same time, *evolutionary systems biology* presents a new research approach aiming to extend both systems biology and evolutionary biology (Section 3.3).

Another important extension of systems biology is the emergence of *systems medicine*, the medical application of systems biology. Systems biology has from the outset been associated with ambitions to solve grand societal challenges. Examples are the aims to provide a better understanding of complex diseases like cancer, and the vision of developing patient-specific models that will allow for individualized disease prediction and prevention (Section 5.3).

The aforementioned aims are often pursued through large-scale international collaborations where many research teams provide data and models to be integrated in complex models of whole cells (e.g., *The Virtual Cell Project*), whole organs (e.g., the *Virtual Liver Project*), and even the whole human body (e.g., *The Virtual Physiological Human* and *the Physiome Project*). Such projects raise new exciting questions for philosophy of science concerning strategies for model building and model validation (Carusi 2014)[^carusi-2014]. Moreover, they provide new sources for philosophical discussions on reduction and explanation (Section 4) and on the societal applications of big data biology (Section 5).

### 1.2 Research Practices in Synthetic Biology

The term synthetic biology was used already in the 1970s and 1980s, but the development of synthetic biology in its modern context is also connected to genomics (Morange 2009; O’Malley 2009; Gelfert 2013)[^gelfert-2013][^morange-2009][^o’malley-2009]. In the wake of big data production around year 2000, comprehensive gene regulatory networks could be constructed that allowed for more systematic and more ambitious design projects. Just like systems biologists commonly define their approach in opposition to the focus on isolated molecules or pathways in molecular biology, so is synthetic biology sometimes framed as a system-oriented approach that moves beyond isolationist approaches in genetic engineering (O’Malley et al. 2008)[^o’malley-2008]. Also in this context, however, the ties to precursors are diverse, and there are different views on whether modular approaches are compatible with biological complexity (see below).

The term synthetic biology became an official label with the first Synthetic Biology Conference in 2004, highlighting the BioBrickᵀᴹ standard as a paradigm example of the engineering aim to design living systems through assembling of modular parts (Endy 2005; Bensaude-Vincent 2013)[^bensaude-vincent-2013][^endy-2005]. But the relation to engineering is complex, and synthetic biology displays a plurality of epistemic aims, visions and methodological frameworks.

#### 1.2.1 Aims and Visions

A central research aim in synthetic biology is to modify gene regulatory pathways so as to control biochemical reactions and produce biochemicals of societal value. For example, genetically modified microorganisms can work as biosensors that detect toxic chemicals or help clean up contaminated soil and water by metabolizing toxic compounds (Khalil & Collins 2010)[^khalil-2010]. Many efforts are also directed towards improvements of biomedical research and clinical practices, e.g., through diagnostic tools, and personalized cancer treatments (Christiansen 2016b)[^christiansen-2016b]. Products of synthetic biology that are already commercially available include biomedical compounds used in treatments against diabetes and malaria, nitrogen fertilizers, and flavouring substances for “bleeding” plant-based burgers (Voigt 2020)[^voigt-2020]. Most prominently, the fast development of effective synthetic mRNA vaccines against Covid-19 points to the potential of synthetic biology in supporting “pandemic preparedness” (Vickers and Freemont 2022)[^vickers-2022], although these developments draw on molecular techniquest that precede the field of synthetic biology.

Much of synthetic biology research can be characterized as application-oriented innovations that utilize and modify biological structures. But not all practices fit this description. Some synthetic biologists pursue a basic science approach to understand the origin of life or the conditions for minimal life (Section 3.2). Others are driven by the wish to create artificial life in the lab, inspired by von Neumann’s (1966) vision of a self-reproducing automaton. This aim may be achieved through the design of macroscale ‘living technology’ (Bedau 2009)[^bedau-2009]. Examples are 3D printers that can print biological tissue structures and perhaps—with time—also replicate themselves.[^note-4] Thus, synthetic biology is an umbrella term covering very diverse research practices.

#### 1.2.2 Knowledge-Making Practices in Synthetic Biology

Examining the diversity of knowledge-making practices in synthetic biology, O’Malley et al. (2008) suggest a distinction between *DNA-based device construction*, *genome-driven cell engineering*, and *protocell creation*.

*DNA-based device construction*, or what Benner and Sismour (2005) characterize more broadly as the engineering trend, explores the extent to which interchangeable and functionally distinct components can be designed and implemented in a modular fashion. The BioBrick Foundation is a paradigmatic example of this approach (biobricks.org). The guiding principles for this approach are standardization, decoupling, and abstraction of parts and functional descriptions (Endy 2005)[^endy-2005]. Examples of DNA-based devices are the repressilator (Elowitz & Leibler 2000, see Section 2.1)[^elowitz-2000], the synthetic toggle switch (Gardner et al. 2000; see Section 2.3)[^gardner-2000], as well as production of synthetic artemisinin for antimalarial drugs (Keasling 2010)[^keasling-2010]. The orientation towards functional devices and machine-like control is also explicit in the so-called iGEM competition (Genetically Engineered Machine) where student teams compete in the task of constructing genetically engineered biological systems to address societal problems. Whether the ideal of constructing standardized and replaceable parts is compatible with biological complexity is an ongoing topic of debate (Sections 2 and 3).

*Genome-driven cell engineering* in synthetic biology departs from the modularity assumption of DNA-based device construction by focusing on the functioning of whole genomes or whole cells (O’Malley et al. 2008)[^o’malley-2008]. This practice includes transplantation of foreign or modified genomes into empty ‘chassis cells’ to acquire new functions (Chan et al. 2005)[^chan-2005], and synthesis of “minimal genomes” (Andrianantoandro et al. 2006; Simons 2021)[^andrianantoandro-2006][^simons-2021]. The notion of a minimal genome highlights the idea that existing organisms may have genomes more complex than necessary for the basic functions of survival and reproduction. The human parasite *Mycoplasma genitalium* has been considered a model organism for the exploration of such questions due to its small genome, and it has also been the target for the first whole-cell model in systems biology (Karr et al. 2012)[^karr-2012]. In 2010, scientists at the J. Craig Venter Institute (JCVI) created a synthetic genome of another bacterial species of the same genus, *Mycoplasma mycoides* (Gibson et al. 2010)[^gibson-2010]. From the synthetic DNA sequence, the researchers could partly control the production of new *Mycoplasma mycoides* cells. This genome was further reduced to a working approximation for the simplest synthetic minimal genome (JCVI-syn 3.0), allowing cells to function and reproduce with only 473 genes (Hutchison et al. 2016; see also Sung et al. 2016)[^hutchison-2016][^sung-2016]. At the same time as lower boundaries for biological complexity are explored, other synthetic biologists aim to manipulate and control the functions of genomes of more complex species, such as yeast and algae (Calvert & Frow 2015; Georgianna & Mayfield 2012; see Simons 2021)[^calvert-2015][^georgianna-2012][^simons-2021].

The third category of synthetic biology, *protocell creation*, takes on the ambitious aim to construct simple approximations of living cells *de novo* (O’Malley et al. 2008)[^o’malley-2008]. Researchers within this stream are often interested in the fundamental question of what life is, and the notion of applied science may not be an appropriate description of this research approach (see Section 3.2). Historically, the theoretical discussion of what life is has often been coupled to wet-lab synthesis of compounds associated with early or minimal life.[^note-5] Synthetic biology takes this approach further through synthesis and manipulation of vesicles resembling primitive cells, as well as through advanced computational simulations of gene regulatory networks (Luisi 2006; Kauffman 2015)[^kauffman-2015][^luisi-2006]. This research practice connects to projects within genome-driven cell engineering investigating the minimal requirements for a living system to function, survive, and reproduce. Research on protocells may focus primarily on understanding the origin of life as we know it, or aim to create synthetic life forms in other and simpler ways (Rasmussen et al. 2008)[^rasmussen-2008].

Deplazes (2009) has suggested the following extended classification of practices within synthetic biology: i) bioengineering, ii) synthetic genomics, iii) protocell synthetic biology, iv) unnatural molecular biology, and v) *in silico* approaches (see Figure 3). While the categories of work on protocells and synthetic genomes overlap with the categorization by O’Malley et al. (2008), DNA-based device construction is here further divided into *bioengineering* (exemplified by assembly standards like BioBricksᵀᴹ) and *unnatural molecular biology*. Unnatural molecular biology aims to create systems with different components, e.g., artificial nucleic acids based on a different coding system. Philosophers have debated whether the term ‘unnatural’ distinguishes practices in synthetic biology from other bioengineering approaches (Lewens 2013; Preston 2013)[^lewens-2013][^preston-2013]. But the emphasis on synthetic artifacts underscores the affinity to synthetic chemistry and perhaps also to the ‘chemist style of thinking’, emphasizing synthesis and invention in addition to analysis and discovery (Bensaude-Vincent 2009, 2013, 2015; see also Bursten 2020, ed.)[^bensaude-vincent-2009].

*Figure 3:*

![[5 circles arranged in a pentagon each connected to all the others by lines. The circles in clockwise order are labeled 'Bioengineering', 'In silico synthetic biology', 'Synthetic genomics', 'Unnatural molecular biology', and 'Protocell synthetic biology'. The In slico... circle has labeled arrows on all the lines to the others: To all the arrows are labeled 'Computer design' {for Bioengineering there is also a reverse arrow 'New metabolic pathways'}. Bioengineering also has another arrow pointing to Protocell... with the label 'New metabolic pathways'. The Synthetic ... circle has an arrow to Bioengineering labeled 'Minimal chassis organisms' and to Protocell... labeled 'Synthetic genomes'; it has an arrow to and from Unnatural... labeled 'Unnatural genome fragments'. Unnatural has arrows to Bioengineering and Protocell labeled 'Unnatural genome fragments'. ]](../assets/systems-synthetic-biology/Figure3.png)

Figure 3: Schematic representation of the five categories of synthetic biology and their connections. (From Deplazes 2009: 431, Copyright 2009 by John Wiley & Sons, Inc. reprinted by permission of John Wiley & Sons, Inc.)[^deplazes-2009].

Deplazes’ fifth category, *in silico* synthetic biology, focuses on the development and practical implementation of computer simulations. Deplazes argues that *in silico* synthetic modeling should be a distinct category because many of the computational models have “little or no direct reference to living organisms” (Deplazes 2009: 430)[^deplazes-2009]. As Figure 3 illustrates, computational design is an important part of research practices in synthetic biology. But the characteristics of various roles of simulations can shed new light on philosophical discussions of the relation between models and target systems, and between modeling, experimentation, and synthesis (Knuuttila & Loettgers 2013a,b; Carusi et al. 2012)[^carusi-2012][^carusi-2012-2][^knuuttila-2013a].

Abstracting from the variety of research practices, a distinctive feature of synthetic biology is that it aims “to go beyond mere modeling and to treat biological systems as fully constructible objects” (O’Malley 2009: 381; see also Schyfter 2013)[^o’malley-2009][^schyfter-2013]. Thus, synthetic biology opens new philosophical questions concerning the relation between synthesis and analysis, between artificial and natural target systems, and between machine and organism (Holm & Powell 2013; Nordman 2015)[^holm-2013][^holm-2013-2].

## 2. Design Approaches in Biology

### 2.1 Designing and Understanding Life

Systems and synthetic biology offer new opportunities to reconsider the prospects and limitations of engineering approaches for biological research (Braillard 2015; Calcott et al. 2015)[^braillard-2015][^braillard-2015-2][^calcott-2015]. Engineering approaches are often considered inadequate to grasp biological complexity. Specifically, design thinking has often been associated with adaptationism, i.e., the assumption that biological traits are optimally “designed” by natural selection (Orzack & Forber 2010)[^orzack-2010]. Accordingly, critics have argued that the engineering approach may lead to a simplified understanding of evolution as driven solely by natural selection (Lynch 2007)[^lynch-2007]. But whereas some approaches in systems biology can be described as adaptationist (Green 2014)[^green-2014], it cannot be assumed that design approaches always entail adaptationist implications. Systems biologists may adopt a ‘thin’ notion of design focusing primarily on the relations between structures and functions (Green et al. 2015b)[^green-2015b][^green-2015b-2]. Because research in systems and synthetic biology often is often dissociated from evolutionary considerations, these research practices may force philosophers to reexamine the concepts of biological function and design beyond traditional aetiological accounts (Holm 2012; Preston 2008; see also Mossio et al. 2009)[^holm-2012][^mossio-2009][^preston-2008].

In this context, it is debatable whether the thin notion of design is compatible with biological complexity. Some scholars have raised concerns that the machine-view of organisms (and use of design metaphors) may lead to a neglect of distinct biological features such as autonomy, evolvability, and intrinsic purposiveness (Nicholson 2019; see also Jacob 1977; Kogge & Richter 2013; McLeod and Nerlich 2017)[^jacob-1977][^kogge-2013][^mcleod-2017][^nicholson-2019]. Design approaches may implicitly enforce the view that operations and outputs of specific parts are stable and predictable across different contexts. In biology, context-sensitivity and degeneracy between genotype-phenotype-relations may provide severe limitations to the utility of this heuristic (Boudry & Pigliucci 2013; Güttinger 2013; see also Section 3.1)[^boudry-2013][^güttinger-2013]. Yet, as outlined in the following sections, the ties to engineering are multi-faceted in both systems and synthetic biology.

### 2.2 Reverse and Forward Engineering

Feynman’s ‘last blackboard’ statement in 1988 that “what I cannot create, I do not understand” is often cited in the context of synthetic biology and has sparked philosophical reflections on the relation between understanding and design (O’Malley 2009; Holm 2012; Calvert & Frow 2013)[^holm-2012][^o’malley-2009]. Although synthetic biology is distinct from systems biology in the explicit aim to design synthetic systems, it is often described as a practice relying on systems biology as a theoretical foundation for design (Barrett et al. 2006)[^barrett-2006].

Synthetic and systems biology are sometimes described through the complementary aims of forward and reverse engineering. *Forward engineering* refers to the design of systems with novel functions, often by drawing on an existing high-level model (e.g., an existing code or living cell). Forward engineering, or re-engineering, can lead to more complex systems, but simplicity may also be pursued through implementation of a more abstract coding language or through reduction or rewiring of (genetic) circuits. *Reverse engineering* refers to the aim to understand the functioning of a system ‘backwards’ by examining an existing system in contexts where consulting a design protocol is not an option. The search for recurring network motifs (Section 1.1.1) is an example of how systems biologists may reverse engineer the structure of a system to understand its functional capacities. Because functional features such as robustness are not only important to the survival of organisms but also to design problems in engineering, reverse engineering of organizational features that underpin such capacities is an important aim in both fields (Csete & Doyle 2002; Hartwell et al. 1999; Kitano 2004; Stelling et al. 2004)[^csete-2002][^hartwell-1999][^kitano-2004][^stelling-2004].

Reverse and forward engineering approaches may challenge the philosophical perspective on how-possibly-models, which are often taken to be stepping-stones for how-actually explanations. In systems and synthetic biology, however, how-possibly models can be explanatory in their own right—in explaining *how possibly* biological functions can be realized in natural or artificial systems (Green 2015; Koskinen 2017)[^koskinen-2017]. In engineering, reverse engineering is an activity geared towards the identification of generic features of system design, or *design principles*, that can be reused in other systems. Similarly, reverse engineering in systems biology aims to identify *biological design principles* that can increase the understanding of structure-function relations across different systems (Csete & Doyle 2002; Doyle & Stelling 2006; Voit 2003)[^csete-2002][^doyle-2006][^voit-2003], and potentially also be used in the design of novel systems in synthetic biology (Koskinen 2019)[^koskinen-2019].

### 2.3 Design Principles in Biology

Systems and synthetic biology not only adopt mathematical tools from electronic and control engineering but also a conceptual framework in which biological functions are understood in terms of control principles and generic representations such as feedback control (Gramelsberger 2013; MacLeod & Nersessian 2013a,b)[^gramelsberger-2013][^gramelsberger-2013-2][^macleod-2013a]. The search for functional principles, with applications to different systems in biology and engineering, dates back to the ideals of cybernetics and biochemical systems theory (Savageau 1976; Wiener 1948)[^savageau-1976][^wiener-1948]. Negative feedback control has long been a central principle in mechanical and electronic engineering to maintain stable concentrations and minimize fluctuations. An important insight from cybernetics is that the same formalization can also describe biological processes, e.g., where a reaction is inhibited as a result of accumulation of the product of the same reaction. An abstract model of negative feedback can therefore denote a functional principle that holds for a larger class of systems (Green & Wolkenhauer 2013)[^green-2013][^wolkenhauer-2013].

Characteristic of the search for design principles in modern systems biology is that the strategy is enforced through automated pattern-detection in network models based on large biological datasets, as exemplified by the search for network motifs (Section 1.1.1). The hope is that simple control principles, using e.g., positive and negative feedback, can make up basic building blocks of biological functioning such as filters, switches, oscillators, amplifiers, detectors etc. (Alon 2007; Tyson et al. 2003)[^alon-2007][^tyson-2003]. One such example is the so-called toggle-switch, a simple regulatory circuit that is considered a design principle in both systems and synthetic biology.

Like a toggle-switch that turns an electrical device ON or OFF, genetic toggle-switches have been found to regulate many biological processes such as the cell cycle of budding yeast and developmental processes in fruit flies (Tyson et al. 2003; Jaeger & Crombach 2012)[^jaeger-2012][^tyson-2003]. A genetic toggle-switch is a double-negative feedback loop that shifts the system between two distinct stable states of gene expression—allowing synthesis of one protein while another is repressed. Synthetic biologists have succeeded in constructing a synthetic toggle switch in *E. coli* (Gardner et al. 2000)[^gardner-2000], and the toggle switch is now considered part of the design composites or ‘computational templates’ for building new synthetic systems (Choffnes et al. 2011; Humphreys 2004)[^choffnes-2011][^humphreys-2004]. Recent work in synthetic biology also involve RNA-based regulatory genetic switches, called *riboswitches*, that can control gene expression by binding to specific ligands (Mehrshahi et al. 2020). The dynamic behavior of genetic toggle-switches have also been investigated in studies of parameter spaces for robust functioning of network motifs (Tyson & Novák 2010)[^tyson-2010], and in approaches combining the modeling framework of dynamical systems theory with reverse engineering of gene regulatory networks from experimental data (Huang et al. 2009; Jaeger & Crombach 2012)[^huang-2009][^jaeger-2012]. Because of the abstract nature of proposed design principles, an interesting philosophical question is how such strategies relate to discussions about the possibilities of laws-like generalizations in biology.

Biological systems are often taken to be too contingent, diverse, and context-dependent to allow for derivation of laws or general principles akin to those found in physics (Burian et al. 1996)[^burian-1996]. The quest for design principles and generic topological features in biology is therefore interesting test cases to explore such issues (Green 2015b; Moreno and Suárez 2020)[^green-2015b][^green-2015b-2][^moreno-2020]. A key issue in this debate is whether generalizable functions can be inferred from organizational structures, relatively independently of cellular, organismal, and environmental contexts. This issue has often been discussed as a question of *multiple realizability,* i.e. whether a higher-level state or property is relatively independent of the causal details or properties at a lower level because the system's structure determines the function. Systems biology bring new light to these debates, e.g., by discussing the extent to which network motifs provide concrete examples of this phenomenon (Fang 2020)[^fang-2020]. Multiple realizability of functions via network motifs has also been argued to provide a design heuristic explored in synthetic biology, e.g., when engineering minimal genetic systems and artificial biochemical systems (Koskinen 2019)[^koskinen-2019]. The search for network motifs and other functional units make apparent that assumptions of modularity are not completely abandoned. Rather, the notion of modularity may be reconfigured via strategies for *structural* decomposition of larger networks (Serban 2020)[^serban-2020][^serban-2020-2]. However, some systems biologists and philosophers have questioned whether functional ‘units’ can be meaningfully isolated from the workings of the network as a whole (DiFrisco and Jaeger 2019; Huang 2011; Isalan et al. 2008)[^difrisco-2019][^huang-2011][^isalan-2008], thus casting new light on debates on reductionism and holism in the life sciences. A related question is how the enhanced focus on generic features of biological networks relates to mechanistic accounts of biological explanation (Section 4.2).

## 3. Revisiting Biological Complexity

Engineering is often promoted through the idea of rational design. Some synthetic biologists have adopted a similar vision of synthetic organisms as structures that can be assembled via replaceable and standardized components, akin to Lego-bricks (front cover of *Science*, 2 September 2011 [333(6047)]). Yet, philosophers have argued that the actual research practices in synthetic and systems biology paint a different picture (Knuuttila & Loettgers 2013a, 2014)[^knuuttila-2013a].

### 3.1 Reverse and Forward Tinkering?

Rather than following a fixed design protocol, research in synthetic biology often progresses through what is taken to be the opposite of rational design, namely *kludging*: a solution that is *k*lumsy, *l*ame, *u*gly, *d*umb but *g*ood *e*nough (O’Malley 2009, 2011b)[^o’malley-2009]. The research process can perhaps be described as *reverse and forward* *tinkering*, in which opportunities for modular decomposition and recomposition are explored in iterative cycles to arrive at piecemeal solutions. Some have argued that synthetic biology exhibits a reflexive double bind to engineering, because the design assumptions guiding the construction of the synthetic systems are continuously reevaluated (Knuuttila & Loettgers 2013a)[^knuuttila-2013a]. That is, synthetic biology does not only progress through similarities between biology and engineering. Through the exploration of engineering approaches, important differences (or *negative analogies*) between biological and engineered systems are discovered (Knuuttila & Loettgers 2014)[^knuuttila-2014]

An example of a possible negative analogy discussed in this context is the role of noise in biological versus engineered systems. In engineering, oscillations are often associated with noise and lack of precision, but oscillatory dynamics are characteristic of many biological processes including metabolism and day and night rhythms (Knuuttila & Loettgers 2013a; see also Bechtel 2016)[^bechtel-2016][^knuuttila-2013a]. To study oscillations in gene expression, synthetic biologists at the Elowitz lab constructed a synthetic genetic circuit called the *repressilator* (Elowitz & Leibler 2000)[^elowitz-2000]. The repressilator was designed to test whether the oscillatory dynamics of gene expression could be mathematically described via connected feedback loops in a simple regulatory circuit and implemented in a synthetic model.

Interestingly, important insights resulted from the repressilator because it *failed* to produce regular oscillations as predicted by the underlying mathematical model. The mismatch between the mathematical and synthetic model led to a reevaluation of the assumptions underlying the deterministic mathematical model (Knuuttila & Loettgers 2013a, 2014)[^knuuttila-2013a]. Subsequent investigation of the dynamics of a stochastic version of the same model suggested that noise may be an inherent feature of oscillations in gene expression in living cells. The exploration of the functional role of noise and the potentials for stochastic modeling has since developed into an important research program of interest to biologists and engineers alike (Briat et al. 2016; Munsky et al. 2009; O’Malley 2011b)[^briat-2016][^munsky-2009][^o’malley-2011b]. The repressilator and similar examples also sparked debates on whether design procedures in synthetic biology need to account for cellular contexts, distributed organization of functions, and other features that are unlike modular machines (Güttinger 2013)[^güttinger-2013].[^note-6]

To what extent the ideal of precision engineering is pursued in synthetic biology is therefore debatable. Some have stressed the centrality of the engineering perspective because the construction of synthetic models is guided by knowledge on which design principles can be expected to create specific dynamic behaviors (e.g., Gramelsberger 2013)[^gramelsberger-2013][^gramelsberger-2013-2]. Others have emphasized that synthetic modeling, as a kind of *material recomposition* strategy, offer material constraints that always involve open-ended aspects (Knuuttila & Loettgers 2013b)[^knuuttila-2013b]. The latter view highlights exploratory features of the triangulation of mathematical, computational, and synthetic approaches. The notion of *exploratory experimentation* has also been used to characterize research processes in systems biology, where scholars search for structural and functional patterns in biological networks without being driven by a specific biological hypothesis (O’Malley & Soyer 2012; Steinle 1997)[^o’malley-2012][^soyer-2012][^steinle-1997]. Research on network motifs (Section 1.1.1) is one example where engineering approaches were applied in an exploratory fashion to generate, rather than test, hypotheses on biological functions (Alon 2007)[^alon-2007]. Also in this context, the analysis may lead to a reevaluation of design assumptions, e.g., whether the functions of network motifs are independent of the network context they are embedded in (Isalan et al. 2008)[^isalan-2008].

It should also be noted that synthetic biologists often aim to produce biological technology that is more machine-like than natural organisms (Kastenhofer 2013a,b; O’Malley 2011b)[^kastenhofer-2013a][^o’malley-2011b]. An alternative response to biological complexity may therefore be to make the designed system simpler, for instance through genetic rewiring that ensures a higher degree of modularity (Knuuttila & Loettgers 2013a)[^knuuttila-2013a]. The explicit aim to simplify synthetic models has been interpreted as acknowledgment of biological complexity, and it is therefore debated whether the criticism of the machine-view in synthetic biology is misguided (cf., Holm 2015; Nicholson 2013)[^holm-2015]. The heuristic value of design approaches is, however, an ongoing topic of debate in both systems and synthetic biology.

### 3.2 Defining and Creating Minimal Life

Unlike DNA-based device construction and genome-driven cell engineering, synthetic biologists in the practice of *protocell creation* engage in classical theoretical discussions on what life is, and how it originated and evolved (Luisi 2006; O’Malley et al. 2008)[^luisi-2006][^o’malley-2008]. This research stream connects to discussions of the fundamental properties of life in systems biology (Cornish-Bowden 2006; Letelier et al. 2011; Wolkenhauer and Hofmeyr 2007)[^cornish-bowden-2006][^hofmeyr-2007][^letelier-2011][^wolkenhauer-2007] and philosophy (Bich 2010; Bich & Damiano 2007; Bedau & Cleland 2010; Moreno & Mossio 2015)[^bedau-2010][^bich-2010][^bich-2007][^moreno-2015].

One strand of research attempts to design minimal cells resembling early cellular life-forms. Inspired by Maturana and Varela’s (1972/1980) formulation of autopoiesis, some synthetic biologists experiment on conditions for minimal cells through chemical models that combine the continuous formation and destruction of the compartment (the cell membrane) with metabolic processes inside the cell (e.g., Zepik et al. 2001)[^zepik-2001]. This research program specializes in synthesis of lipid compartments, such as vesicles, to study coordinated processes that possibly resemble self-maintenance in the pre-biotic world (Luisi 2006)[^luisi-2006]. Moreover, vesicles have been used to experiment on how catalytic molecules such as ribozymes and peptides could become entrapped in lipid compartments and create precursors for metabolic circuits (de Souza et al. 2014)[^souza-2014].

An important research goal is to provide a model for the fundamental features that distinguish living systems from the non-living. So far, however, there is no consensus on the defining features of life. Whether this should be seen as a disappointment, indicating the uselessness of attempts to define life, is an ongoing issue of philosophical debate. Different views on this question may depend on different interpretations of what the project of *defining life* entails in philosophy and science, e.g., whether the aim is to establish demarcate a natural kind (Cleland 2012)[^cleland-2012] or to provide operational definitions of practical use in model and theory construction (Bich & Green 2018; Luisi 1998)[^bich-2018][^green-2018][^green-2018-2][^luisi-1998]. More specific topics of debate are whether definitions of life must include Darwinian evolution, how evolution and units of selection should be defined, and whether it is fruitful to categorize all the varieties of life forms under one definition (Dupré & O’Malley 2009; Laland et al. 2009; Ruiz-Mirazo et al. 2010; Szostak et al. 2001)[^dupré-2009][^laland-2009][^o’malley-2009][^ruiz-mirazo-2010][^szostak-2001]

Systems biologists engaging in debates on the properties of life often stress the relevance of insights from classical philosophers. Examples are references to Aristotle or Kant in discussions on whether our current notion of causation can adequately capture how parts and wholes in living systems stand in reciprocal causes and effect relationships (Drack & Wolkenhauer 2011; Hofmeyr 2017)[^drack-2011][^hofmeyr-2017]. Other important sources of inspiration are Rosen’s formalization of metabolism-repair systems, (mathematical) general systems theory, and category theory (e.g., Drack 2015; Rosen 1991; Mesarović et al. 2004; Letelier et al. 2011)[^drack-2015][^letelier-2011][^mesarović-2004][^rosen-1991]. The systems-theoretical stream is also influenced by mathematical biophysics (Rashevsky 1961)[^rashevsky-1961], Waddington’s theoretical biology (Fagan 2012)[^fagan-2012], Biochemical Systems Theory (Hofmeyr 2007; Savageau 1976)[^hofmeyr-2007][^savageau-1976], and classical systems-oriented physiology (Noble 2008)[^noble-2008].

Systems-theoretical and organizational accounts often highlight the functional roles of constraints, autonomy, and causal closure of the processes of self-maintenance (Moreno & Mossio 2015; Wolkenhauer & Hofmeyr 2007)[^hofmeyr-2007][^moreno-2015][^wolkenhauer-2007]. While also stressing the utility of the search for general principles, some prefer the term *organizing principles* instead of design principles (Green & Wolkenhauer 2013; Mesarović et al. 2004)[^green-2013][^mesarović-2004][^wolkenhauer-2013]. This choice of terminology signals the view that understanding living systems requires a systems-theoretical approach in a broader sense than cybernetics. An intriguing question in this context is whether a different kind of formal or mathematical framework is required—one that is adapted to biology rather than to engineering or physics (Bich & Damiano 2008; Gramelsberger 2017; Rosen 1991)[^bich-2008][^gramelsberger-2017][^rosen-1991].

Another debated issue in discussions about the fundamental properties of life is the relative priority of autonomy, openness and collaboration. Whereas much research in philosophy and origin of life has focused on individual organisms, recent insights from microbiology and synthetic biology have extended the focus on individual cells to also include the interactions of cell colonies and pangenomic populations (Dupré & O’Malley 2009; Bich & Green 2018; O’Malley et al. 2019)[^bich-2018][^dupré-2009][^green-2018][^green-2018-2][^o’malley-2009][^o’malley-2019]. For example, synthetic models can be used to investigate the dynamics of colonies of giant oleate-based vesicles under hypothesized prebiotic conditions. For example, an experiment conducted by Carrara and colleagues (2012) showed that that the permeability of the vesicles to catalysts and macromolecules were much higher for the colonies, compared to individual vesicles. In some cases, the colonies also attracted each other and exchanged material. The results raise important questions about whether life has arisen from ‘cooperative mechanisms’ between prebiotic systems, and whether we need to rethink ontological assumptions about what constitutes a ‘unity of life’. Synthetic models can also be used to study the role of structural and cognitive interactions for biological identity and autonomy (Bich 2020)[^bich-2020]. Meanwhile, research on minimal genomes and imagined artificial life forms can explore what is biologically possible beyond what is found in natural systems (Koskinen 2017; Knuttila & Koskinen 2021)[^koskinen-2017]. Synthetic biology, understood as a technoscience exploring the *design* of minimal and alternative life forms, thus has potential to address questions about universal biology beyond the historical question about how life originated (Simons 2021)[^simons-2021].

### 3.3 Evolutionary Systems Biology

Systems biology is often defined as an approach primarily concerned with functional questions (Boogerd et al. 2007)[^boogerd-2007]. Evolutionary systems biology (ESB) explicitly seeks to expand this focus through investigations of the evolutionary dynamics of interacting networks (Soyer 2012)[^soyer-2012]. ESB aims to put the results of systems biology in a proper evolutionary context and also to enhance and extend current evolutionary biology. Specifically, ESB aims to develop more detailed models of genotype-phenotype maps to study causal changes over evolutionary time-scales and to enhance the predictive potential of evolutionary models. These aims are pursued by combining methods from molecular and evolutionary biology with *in silico* evolution, comparative genomic analysis, as well as with dynamical modeling of network architectures (Bapteste and Papale 2021; Soyer & O’Malley 2013)[^bapteste-2021][^soyer-2013].

ESB can be considered a meeting ground not only for systems biology and evolutionary biology but also for the integrated study of developmental phenomena in an evolutionary perspective (O’Malley et al. 2015)[^o’malley-2015]. Systems biology complements statistical sequence analysis in population genetics and studies of constraints on evolutionary pathways in Evolutionary Developmental biology (EvoDevo) through *in silico* modelling of large data-sets (Jaeger & Crombach 2012; Kim et al. 2011; see also Brigandt 2015)[^brigandt-2015][^jaeger-2012][^kim-2011]. Some projects also draw on synthetic modelling of intracellular networks to investigate how the evolutionary potential of a lineage is affected by specific combinations of mutations (Palmer & Kishony 2013)[^palmer-2013].

Evolutionary network modeling contributes to conceptual development in evolutionary biology, e.g., by throwing new light on discussions on the unit of selection (Bapteste and Papale 2021)[^bapteste-2021]. Another important line of investigation in ESB examines the evolutionary background for global network architectures, modular structures, and recurring network motifs (Section 1.1.1; see also Krohs 2009)[^krohs-2009]. The structures may have arisen due to natural selection, but ESB also takes seriously the possibilities that patterns can arise as side-effects of genomic evolution and drift, or from a combination of selective and non-selective factors (Steinacher & Soyer 2012)[^soyer-2012][^steinacher-2012]. An example of an insight from simulations of evolving yeast networks is that hierarchical structures with an overabundance of network motifs (feedforward loops) can emerge by *non-selective tinkering* with promoter regions (Cordero & Hogeweg 2006)[^cordero-2006]. In extended models, the integrated effects of selective and non-selective factors can be studied at multiple levels (Hogeweg 2012)[^hogeweg-2012]. With the emphasis on pattern-generation and the potential for future evolutionary change, ESB takes up Hugo de Vries’ challenge to explain not only the *survival* of the fittest but also the *arrival* of the fittest (Wagner 2012, 2014)[^wagner-2012]. The hope is that evolutionary simulations can extend evolutionary biology by providing a forward-looking account.

Evolutionary biology has traditionally been considered as a historical discipline that provides explanations without giving predictions. ESB offers an opportunity to develop more detailed models of evolving genotype-phenotype relations and to explore whether some evolutionary pathways are predictable given enough information about the network structures, dynamic states, and environmental conditions. Unlike forward engineering in synthetic biology, the aim is not to shape new designs but to understand the possible trajectories of change under different conditions. That is, ESB goes beyond historical accounts in exploring the potential for evolvability or innovation—what some have called the ‘tinkering potential’ of system evolution (Koonin & Wolf 2010)[^koonin-2010]. Research on evolvability can, however, also inform and inspire functional analysis and design in synthetic biology (Calvert & Frow 2015; Lewens 2013)[^calvert-2015][^lewens-2013]. Thus, also in this context, the relation between biology and engineering must also be reexamined.

The phenomena of tinkering and contingency in evolution are typically taken to highlight the *limitations* of engineering approaches in biology (Jacob 1977; Lynch 2007)[^jacob-1977][^lynch-2007]. Interestingly, however, some systems biologists and philosophers emphasize that a non-adaptationist framework can be reached through further cross-fertilization of biology and engineering (Calcott et al. 2015)[^calcott-2015]. ESB and synthetic biology can provide a broader perspective on engineering by considering how design often operates through modification of existing systems. For instance, there are interesting similarities between *evolvability* in biology and a *diachronic* *engineering goal* in software engineering, where the aim is to design systems that can be adapted to serve future functional requests, without having to rewrite the code from scratch (Calcott 2014; see also Solé and Valverde 2020)[^calcott-2014][^solé-2020].

The ambition to predict evolutionary trajectories, even for simple organisms, may turn out to be extremely difficult. But ESB provides new ways to investigate whether evolutionary pathways follow some recognizable dynamical patterns. Simulations of how gene regulatory networks change over evolutionary time-scales can be coupled to experimental evolution in bacteria or insects. For instance, the development of bacterial antibiotic resistance has been shown to be constrained by interactions between different mutations, which may make evolutionary biology informative also for the development and combination of antibiotics used in medical treatment (Palmer & Krishony 2013; Weinreich et al. 2006)[^palmer-2013][^weinreich-2006].

Some proponents expect that ESB will uncover regularities or stable evolutionary patterns across various types of networks and species. Such regularities may not resemble universal laws, but the hope is that some general principles underlying evolutionary dynamics can be identified, referred to as “laws of evolution” (Koonin 2011)[^koonin-2011], “evolutionary design principles” (Steinacher & Soyer 2012)[^soyer-2012][^steinacher-2012] or “generic principles” of evolution (Jaeger & Monk 2013)[^jaeger-2013]. ESB thus offers excellent cases for debating the possibility of turning evolutionary biology into a more predictive field with generalizable principles (Lobkovsky & Koonin 2012; Papp et al. 2011)[^lobkovsky-2012][^papp-2011]. Moreover, it is a rich field for discussing the implications of an ‘extended modern synthesis’ that combines molecular, mathematical, computational, synthetic, and population genetic approaches to evolution (Pigliucci 2007; O’Malley et al. 2015)[^o’malley-2015][^pigliucci-2007].

## 4. Revisiting Classical Philosophical Questions

With the emphasis on systems and interacting networks, both systems and synthetic biology explicitly engage in one of the oldest philosophical discussions on the relationship between the whole and its parts, or between holism and reductionism. This section examines how classical questions are reframed in the new light of strategies for large-scale data production and dynamic modeling.

### 4.1 Reductionism and the Sum of the Parts

As mentioned in the introduction, proponents of systems biology often explicitly define their approach in contrast to reductionist strategies in molecular biology. Molecular biology is depicted as a field studying molecular components and pathways in isolation, whereas systems biology integrates the pieces of the puzzle in the context of the system as a whole (van Regenmortel 2004; Keller 2005; Kitano 2002a,b)[^keller-2005][^kitano-2002a][^regenmortel-2004]. The contrast between molecular biology and systems biology is often overstated, and much of systems biology research is also focused on specific molecular difference-makers (De Backer et al. 2010; Gross 2017; O’Malley & Dupré 2005)[^gross-2017][^gross-2017-2][^o’malley-2005]. However, systems biology may give a novel interpretation of Aristotle’s dictum that *the whole is more than the sum of the parts* by specifying what *more* means in the context of contemporary biology.

#### 4.1.1. Modular and Bottom-Up Reductionism

When systems biologists criticize reduction in molecular biology, the issue at stake is typically the limitations of studying biological parts or modules in isolation. Because the target of the criticism often differs from the more traditional philosophical focus on reduction of higher-level to lower-level explanations (Brigandt & Love 2017)[^brigandt-2017], systems biologists can be said to oppose what has been termed *modular reductionism* (Gross & Green 2017)[^green-2017][^gross-2017][^gross-2017-2]. An anti-reductionist stance towards modular reductionism needs not reject the idea that living systems can be modelled and explained *bottom up*. For instance, while global approaches within these fields reject the modularity assumption, some keep the focus on genomes and molecular networks as the primary determinants of biological functions (O’Malley et al. 2008)[^o’malley-2008].[^note-7]

Many systems biologists have, however, also argued against reduction of higher-level models and explanations, and there is an ongoing debate about how far genomics, proteomics, etc. will take us in solving complex problems like understanding cancer (cf., Barabási et al. 2011; Hood et al. 2015)[^barabási-2011][^hood-2015]. Similarly, researchers involved in projects aiming to simulate multiscale structures like the human heart emphasize the need to include macroscale parameters as they provide functionally important constraints on the behavior of microscale processes (Bassingthwaighte et al. 2009; Kohl & Noble 2009)[^bassingthwaighte-2009][^kohl-2009]. An interesting reframing of Aristotle’s dictum in this discussion is that living systems at the same time are *more* and *less* than the sum of the parts (see Hofmeyr 2017; Noble 2012)[^hofmeyr-2017][^noble-2012]. In other words, the system as a whole constrains the degree of freedom of lower-level parts and provides a functional organization of these that are required for some system capacities (see below).

Given the increasing emphasis on comprehensive multiscale models, systems biology research may have a unique potential for philosophical insights considering the explanatory role of macroscale properties and top-down effects. Systems biologists for instance point to how enzyme activity is constrained by the chemical environment and the cellular context (Hofmeyr 2017)[^hofmeyr-2017], or how the biophysical properties of muscle fibers and cell membranes provide functional constraints on ionic oscillations central to the generation of heart rhythms (Noble 2012)[^noble-2012]. Interpreting top-down effects as constraining relations may exemplify what philosophers of science have called ‘medium downward causation’ (Emmeche et al. 2000)[^emmeche-2000], which interprets downward causation as boundary conditions. Noble (2012) explicitly endorses such a view when arguing that downward causation is necessary by pointing out how equations describing the kinetics of ion channels in cardiac modeling cannot be solved without defining the boundary conditions (e.g., the cell voltage). Multi-scale modeling may thus help to give a more concrete mathematical reinterpretation of the controversial notion of downwards causation (see also Ellis et al. 2011; Green 2018)[^green-2018][^green-2018-2]. Moreover, discussions of downward causation in systems biology have practical as well as theoretical implications, e.g., for experimental design in cancer research on studies of cancer as a genetic or tissue-based disease (Bertolaso 2011; Soto et al. 2008; see also Section 5.3)[^bertolaso-2011][^soto-2008].

#### 4.1.2 Emergence and Predictability

Discussions of downward causation are often connected to debates about whether biological systems exhibit *emergent properties* (cf., Alberghina & Westerhoff 2005; Boogerd et al. 2005, 2007; Kolodkin et al. 2011)[^alberghina-2005][^boogerd-2005][^kolodkin-2011][^kolodkin-2011-2]. Emergence in the context of systems biology typically means that systems properties cannot be explained from the properties of parts. Discussions can center on epistemic questions about whether systems properties can be predicted from analyses of lower-level constituents (epistemological emergence) to debates on whether multilevel systems are fundamentally irreducible (ontological emergence).

Some systems biologists are optimistic that current limitations in the predictive capacity of models can be overcome by increasing the complexity of computational models, thus presenting a epistemic departure from the methodological principle of Ockham’s razor (Kolodkin & Westerhoff 2011)[^kolodkin-2011][^kolodkin-2011-2]. Others stress that biological complexity forces life scientists to draw on abstract and idealized models (Hofmeyr 2017; Gross 2017; 2019)[^gross-2017][^gross-2017-2][^hofmeyr-2017]. These debates center on fundamental questions about how far biological research can be taken by integrating more parameters and data points (Kolodkin et al. 2012)[^kolodkin-2012], and how far we can ‘extend ourselves’ through computational approaches (Humphreys 2004; Vermeulen 2011)[^humphreys-2004][^vermeulen-2011]. But they also concern ontological questions about whether there are principled limitations to our ability to predict and control living systems “bottom-up” (Bassingthwaighte et al. 2009; Green 2018; Noble 2012; Moreno and Suárez 2020)[^bassingthwaighte-2009][^green-2018][^green-2018-2][^moreno-2020][^noble-2012]. Large-scale modeling projects such as the *Virtual Cell, the Physiome Project*, and the *Virtual Physiological Human* offer exciting cases for philosophical analysis of the prospects and challenges associated with parameterizing and validating complex models (Carusi et al. 2012; Carusi 2014; Hunter et al. 2013)[^carusi-2012][^carusi-2014][^carusi-2012-2][^hunter-2013]. Ultimately, such projects may push the boundaries for prediction and control in the life science, or may reveal deeper challenges of biological complexity.

### 4.2 Explanatory Pluralism

Systems biology also brings new insights to discussions of scientific explanation. In particular, network analysis in systems biology have further sparked discussion about the roles of mathematical abstractions to identify organizational features, counterfactual dependencies, and generalizable aspects of biological systems. The integration of different disciplinary inputs and emphasis on mathematical modeling make systems biology a particularly interesting case for discussions of whether the mechanistic account can fully capture the diversity of explanatory practices in contemporary biology.

Mechanistic accounts initially emphasized the differences between the explanatory ideal of covering laws in physics and explanations in molecular biology (Craver & Tabery 2015)[^craver-2015]. Mechanistic explanations cite how biological functions arise from the interactions and organization of component parts or entities (Bechtel & Richardson 1993; Machamer et al. 2000; Glennan 2002)[^bechtel-1993][^glennan-2002][^machamer-2000]. Since research in systems biology is often integrated with research in molecular and cell biology, some have argued that many cases in systems biology can readily be seen as an extension of mechanistic research (Boogerd et al. 2013; Richardson & Stephan 2007)[^boogerd-2013][^richardson-2007]. But although abstract modeling is compatible with mechanistic research, it is a contested issue whether abstract models are developed towards research aims that are distinct from mechanistic explanations. While some contend that mathematical models are primarily used as inputs to or heuristics for mechanistic explanations, i.e., as mechanistic schemas (Darden 2002; Matthiessen 2015)[^darden-2002][^matthiessen-2015], others interpret the emphasis on quantitative and dynamic aspects as a departure from mechanistic explanations. One argument in support of the latter is that the modeling process does not proceed from abstract to more detailed models, but in the opposite direction, suggesting that mechanistic details may be vehicles for more generic explanations rather than the other way around (Braillard 2010; Serban & Green 2020)[^braillard-2010][^serban-2020][^serban-2020-2]. A second argument refers to the difficulty of reconstructing a causal story from the abstract mathematical models (Issad & Malaterre 2015)[^issad-2015]. Systems biology may therefore also offer cases of non-mechanistic explanations.

*Topological* or *structural* explanations emphasize how networks architectures generically determine dynamic behaviors, independently of the causal details of the network (Huneman 2010; Kostić 2020; Kostić et al. 2020; Suárez & Deulofeu 2019)[^huneman-2010][^kostić-2020][^kostić-2020-2][^suárez-2019]. Mathematical analysis of network structures underlying biological robustness has been argued to exemplify this explanatory goal (Jones 2014)[^jones-2014]. Another type of non-mechanistic explanations is what Wouters (2007) calls *design explanations,* first outlined in the context of comparative physiology. Design explanations do not describe how a biological function is causally produced but instead clarify why a given design (and not an alternative design) is present. They do so by pointing to constraints on the possible designs that make some designs good, some suboptimal, and others impossible. The relevance of design explanations for systems biology lies in the interest to specify relations between functional capacities (e.g., robustness) and system organization (e.g., integral feedback control) via design principles that are independent of specific contexts of implementation (Braillard 2010; Boogerd 2017, see also Shinar & Feinberg 2011 for a candidate example from systems biology)[^boogerd-2017][^braillard-2010][^shinar-2011]. Design explanations highlight explanatory features similar to what Batterman and Rice (2014) call *minimal model explanations* (see also Gross 2015)[^gross-2015]. These explanatory accounts have been interpreted as varieties of *constraint-based explanations* (Green and Jones 2016)[^green-2016][^green-2016-2], because they prioritize physical and formal constraints at the expense of mechanistic details. Aside from highlighting differences in the epistemic aims of explanation, some accounts also provide an *ontological justification* for different explanatory strategies, i.e., that higher-level phenomena are characterized by a functional loss of and autonomy from mechanistic details at lower levels (Batterman and Green 2021; Moreno and Suárez 2020)[^batterman-2021][^moreno-2020].

Another approach is to consider explanations in systems biology as mergers of different types of explanations. Some accounts highlight the compatibility of different explanatory aims as ingredients in a pluralistic approach to biological explanation (Brigandt et al. 2018; Mekios 2015)[^brigandt-2018][^mekios-2015]. One way to clarify the compatibility is that different approaches highlight *constitutive* or *causal* aspects (Fagan 2015)[^fagan-2015]. Distinguishing between these can possibly help identify the distinct contributions of causal mechanistic modeling and mathematical analysis of network dynamics. Whereas causal relations are often prioritized in mechanistic accounts, Fagan (2015) suggests a joint account of *collaborative explanations* that combine descriptions of the spatial organization and the causal relations in the system. The increasing reliance on formal modeling in systems biology also call for an examination of the relation between *mathematical* and *mechanistic explanations* (Baker 2005; Brigandt 2013; Mekios 2015)[^baker-2005][^brigandt-2013][^mekios-2015]. Some have argued that an updated account of *dynamic mechanistic explanations* is required, highlighting the importance of mathematical and computational modeling for understanding non-linear dynamics, cyclic organization, and complex feedback relations (Bechtel & Abrahamsen 2011, 2012; Brigandt 2013)[^bechtel-2011][^brigandt-2013]. In this context, idealized models are important for understanding the organization of mechanisms within a larger network structure (Bechtel 2015b; Levy & Bechtel 2013; van Eck & Wright 2021)[^bechtel-2015b][^levy-2013][^eck-2021].[^note-8]

Although much, or perhaps most, of the philosophical work on systems biology has focused on explanation, one cannot assume that explanation is the sole aim of systems biology research (MacLeod & Nersessian 2015; Kastenhofer 2013a,b)[^kastenhofer-2013a][^macleod-2015]. Design principle may not only explain how biological functions are realized but also allow for explorations of whether the same function could be realized in other or simpler ways (Briat et al. 2016)[^briat-2016]. Thus, synthetic and systems biology also call for philosophers to examine other epistemic aims, such as prediction, control, and design, and well as theoretical and practical interests in understanding the minimal requirements for biological functions and life itself.

## 5. Social and Societal Implications

### 5.1 Interdisciplinary Integration, Collaboration and Education

Large-scale interdisciplinary collaboration is increasingly highlighted as a necessary requirement for addressing the grand challenges of modern science and society (Vermeulen 2010; Calvert 2010; Andersen 2016)[^andersen-2016][^calvert-2010][^vermeulen-2010]. Interdisciplinarity is a hallmark of systems and synthetic biology, and both approaches offer rich sources for philosophical analysis of the epistemic features of interdisciplinary integration (O’Malley & Soyer 2012)[^o’malley-2012][^soyer-2012], interdisciplinary identities (Calvert 2012)[^calvert-2012], and of large-scale collaboration across different universities (Calvert & Frow 2015; for examples of large-scale projects see the list of internet resources below)[^calvert-2015].

Studying the prospects and challenges of interdisciplinary integration also offers a window to the cognitive processes involved in interdisciplinary problem-solving, where research cannot rely on a single theoretical framework (MacLeod & Nersessian 2013a,b)[^macleod-2013a]. Through this process, different epistemic ideals operating in contemporary science often become apparent. While combining different conceptual frameworks can lead to innovation and scientific progress, the existence of different epistemic cultures can also pose challenges for interdisciplinary collaboration (Calvert & Fujimura 2011; Carusi 2011; Kastenhofer 2007)[^calvert-2011][^carusi-2011][^kastenhofer-2007]. Philosophical analysis has been proposed to help facilitate collaboration in situations where epistemic standards clash. Philosophy of science can help explicate the differences and the backgrounds for these, and uncover ‘blind spots’ considering the aims, values, constraints, and challenges of other disciplines (Nersessian 2017)[^nersessian-2017].

One divide that is commonly highlighted is the gap between experimental biologists and modelers with a background in engineering, mathematics, or physics. Empirical analyses of collaborations between modelers and experimentalists in systems biology show that these two groups often have different views on what kinds of data and models are most relevant (Joaquium et al. 2019; Nersessian 2017; Rowbottom 2011)[^nersessian-2017][^rowbottom-2011]. For instance, modelers may not be interested in studying biological systems at the same level of detail as experimental biologists, and experimentalists may find highly abstract and idealized models inspired by physics or engineering misleading (MacLeod 2018)[^macleod-2018]. From the perspective of engineers or physicists, the preoccupation with molecular details involves a risk of missing out on dynamic patterns that could be captured with more generic models, while experimentalists may find that such generic models often lack specificity or merely reproduce current biological knowledge. These differences may in part be grounded in different explanatory standards as also discussed in Section 4.2 (Fagan 2016; Green et al. 2015a)[^fagan-2016][^green-2015a][^green-2015a-2].

Making explanatory standards and values more explicit, and clarifying the relative prospects and limitations of different research strategies, are ways in which philosophy of science could contribute to science and science education. At the same time, collaborative practices in synthetic and systems biology may call for an extension of the scope of philosophical analysis. Whereas philosophers traditionally have focused on logical and argumentative relations in scientific texts, understanding collaborative practices in systems and synthetic biology may further require the exploration of the aesthetic, cognitive, and creative dimensions of scientific practice (Carusi 2011; Ginsberg et al. 2015)[^carusi-2011][^ginsberg-2015]. Important questions are which aspects underlie choices of visualization strategies, and how the representation of biological data through diagrams, heat maps, network models, or state spaces influence biological reasoning and collaboration (Abrahamsen & Bechtel 2015; Carusi 2012; Jones & Wolkenhauer 2012)[^abrahamsen-2015][^carusi-2012][^carusi-2012-2][^jones-2012].

### 5.2 Biology in the Digital Age

The emergence of systems biology and synthetic biology in the 21th century is to a large extent driven by the development of techniques and strategies for producing, digitalizing, collecting, disseminating, and standardizing data. A first step in these research practices is often to consult online databases or bio-ontologies that are used for data sharing, data integration, annotation, and curation of experimental datasets (Leonelli 2016)[^leonelli-2016]. For instance, the search for network motifs (Section 1.1.1) started with the development of network models based on data downloaded from the database RegulonDB as well as other sources (Shen-Orr et al. 2002)[^shen-orr-2002]. Numerous databases, bio-ontologies, and software tools have been developed, emphasizing the ideals of Open Data and large-scale collaborative efforts (Leonelli 2013)[^leonelli-2013]. These practices raise questions as to whether some projects within systems and synthetic biology may be described as ‘big science’ (Vermeulen 2010)[^vermeulen-2010], and about the epistemic and social implications of data-intensive research practices and collaborations.

One debated issue is the extent to which big data will radically change or even revolutionize scientific methods, shifting the focus from hypothesis-driven inquiry to data-driven discoveries (Mazzocchi 2015)[^mazzocchi-2015]. Whereas some have seen data-intensive strategies as a theory-free approach (Allen 2001)[^allen-2001], others have argued that theory plays different, although not less important, roles in data-intensive science (Leonelli 2016)[^leonelli-2016]. In particular, big data biology presents new opportunities for eliminative inferences and exploratory experiments (Ratti 2015)[^ratti-2015]. Moreover, since the aim of bio-ontologies is to provide a standardized language and repository for shared information, choices concerning vocabulary and categorizations become important philosophical topics, including whether standardization is compatible with local data uses (Leonelli 2016)[^leonelli-2016]. Important philosophical questions include how choices concerning collection, sampling, standardization, visualization, and interpretation of data affect the result of the analysis. Specifically, the results of correlation-based methods such as GWAS are sensitive to sampling procedures and specific statistical thresholds, and the clinical validity and utility of genetic biomarkers is a debated issue (e.g., Hey 2015; Maher 2008; McPherson and Tybjaerg-Hansen 2016)[^hey-2015][^maher-2008][^mcpherson-2016].

Finally, data-intensive practices also have implications for the institutional organization of science, as exemplified by the push for open access on one hand and commercial interests in big data on the other (Calvert & Frow 2015; Kastenhofer 2013a,b; Leonelli 2013, 2014; Royal Society 2012; Vermeulen 2011)[^calvert-2015][^kastenhofer-2013a][^leonelli-2013][^royal-2012][^vermeulen-2011]. Data are often produced and compiled without specific aims in mind and are used and reused for multiple purposes, and scholars have stressed the need to reconsider the relation between data and evidence, and between basic and applied science. Moreover, as contexts for ownership of data change, also reward-systems in terms of authorship and credits may need to be reconsidered (Ankeny & Leonelli 2015)[^ankeny-2015].

### 5.3 Applications and Ethical Issues

Systems biology and synthetic biology are expected to help address societal challenges with payoffs for biomedical research, health care, and environmental resource management. While offering new exciting potentials, concerns have also been raised about the social and ethical implications of the new techno-scientific strategies.

Systems medicine, the medical application of systems biology, aims for major breakthroughs towards understanding of complex diseases such as cancer and heart conditions (Voit & Brigham 2008; Wolkenhauer et al. 2013)[^voit-2008][^wolkenhauer-2013]. Ambitious projects within systems biology such as the *Virtual Physiological Human* raise intriguing questions about how computational modeling will influence future biomedical research (Kohl & Noble 2009; Kolodkin et al. 2011; Hunter et al. 2013)[^hunter-2013][^kohl-2009][^kolodkin-2011][^kolodkin-2011-2]. Multi-scale cardiac models are already being developed with important implications for the potential to address physiological variability, and for philosophical discussions of model validation and the relation between experiment and simulation (Carusi et al. 2012; Carusi 2014)[^carusi-2012][^carusi-2014][^carusi-2012-2].

Developments in systems and synthetic biology have encouraged philosophers to revisit traditional conceptions of disease as dysfunctional states (Holm 2013, 2014)[^holm-2013][^holm-2013-2], or broken mechanisms (Gross 2011)[^gross-2011]. Rather than focusing on the function or dysfunction of specific genes or molecular mechanisms, network approaches to disease may suggest a more dynamic approach to disease that accounts for an increasing number of integrated processes (Del Sol et al. 2010; Huang et al. 2009)[^del-2010][^huang-2009]. Cancer research is a major priority of systems biology research, and exemplifies a field where data-intensive approaches may be needed to address biological complexity (Plutynski 2021)[^plutynski-2021]. Developments in cancer genomics have revealed an astonishing diversity of tumor types, suggesting that finer-grained disease-categories and more targeted treatments may be needed. This line of research has opened new research venues, such as the development of multi-action remedies targeting numerous disease-related pathways identified via genomic analysis. The discovered diversity of mutations identified in sequenced tumors has, however, also led to heated debates on whether the behavior and identity of cancer cells can fully be understood at the molecular level. Some have stressed the need to move beyond gene-centric or cell-centric approaches and to consider cancer as a problem of tissue-organization (Soto & Sonnenschein 2011)[^soto-2011]. Although some systems biological explanations of cancer illustrate the possibility of integrating “top-down” and “bottom-up” approaches (Bertolaso 2016; Plutynski and Bertolaso 2018)[^bertolaso-2016][^plutynski-2018], systems biology research also displays a variety and sometimes conflicting approaches to cancer. These debates not only have philosophical implications for discussions about reductionism but also practical implications for how cancer should be approached experimentally and treated in clinical practice (Bertolaso 2011; Soto et al. 2008)[^bertolaso-2011][^soto-2008].

One of the important problems in contemporary medicine is how to account for patient-specific variation. Systems medicine is sometimes highlighted as a route to personalized or precision medicine (Hood et al. 2015)[^hood-2015]. The aim to personalize medicine is as old as the medical profession itself, but it is now promoted through data-intensive computational strategies with exciting new potentials (Tutton 2014)[^tutton-2014]. Proponents are optimistic that large-scale modeling of patient-specific data can result in a paradigm-shift from a one-size-fits-all model in traditional medicine, toward a more efficient systemic approach that can tailor disease prevention, diagnosis, and treatment to individual patients. Against this optimism, some have raised concerns about uncertainties and potential harmful results associated with genetic risk profiling, including the risk of overdiagnosis and unnecessary medicalization of healthy individuals (Green & Vogt 2016; Vogt et al. 2016, 2019)[^green-2016][^green-2016-2][^vogt-2016]. Philosophers and social scientists have also critically examined how risk information is communicated to the public by companies capitalizing on personalized genomics, and discussed how such information may affect health outcomes and perceptions of health (Bartol 2013; Prainsack 2017; Reydon et al. 2012)[^bartol-2013][^prainsack-2017][^reydon-2012]. More generally, systems medicine has spurred debates about whether the vision to predict and control future health outcomes is compatible with a humanistic approach to medicine and social complexity (Tutton 2014; Vogt et al. 2014)[^tutton-2014][^vogt-2014]. Moreover, combination of systems medicine and synthetic biology applications opens also for what O’Malley (2011a) termed *constructive personalized* medicine, where predictive modeling and synthetic interventions are combined. Promising technologies for these purposes now include CRISPR-Cas9 gene editing, organ-on-chip models, 3D bioprinting and organoid-based models for replacement therapies. While creating unprecedented potentials for disease treatment, they also raise ethical questions about artificial chimerism and human enhancement (Pio-Lopez 2021)[^pio-lopez-2021].

In the context of synthetic biology, discussions often center on whether the attempt to create synthetic organisms and the use of design metaphors can compromise our perspective on and respect for life (Christiansen 2016a; Douglas et al. 2013; McLeod and Nerlich 2017)[^christiansen-2016a][^douglas-2013][^mcleod-2017]. Other ethical debates consider the risk of negative consequences of specific synthetic applications. Discussions often involve so-called dual-use problems where the benefits of genetically modified organisms are weighted against potential problems and risks. Examples are biohazards associated with intentional or unintentional release of synthetic pathogens, or the possibility that synthetic production of biomedical compounds opens for efficient and inexpensive production of illegal drugs (Christiansen 2016b)[^christiansen-2016b]. Concerns have also been raised about the commercialization of biotechnologies. Examples are applications of broad patents concerning minimal genomes or synthetic genes (O’Malley et al. 2008)[^o’malley-2008], and considerations about structural injustice if industrial production via synthetic organisms outcompete conventional farming in developing countries (Christiansen 2016b)[^christiansen-2016b]. Thus, the strong push to address societal problems through systems and synthetic biology gives rise to new exciting possibilities but also calls for critical examination from philosophers and social scientists.

## 6. Concluding Remarks

Systems and synthetic biology are often described as distinguishable in their emphasis on analysis versus synthesis, but the ties to engineering approaches are complex and multi-faceted in both fields. Systems and synthetic biology have been addressed together in this entry because many scientific and philosophical issues overlap. Both approaches draw inspiration from engineering, mathematics, physics, and computer science, but in various different ways and towards the different aims of understanding, predicting, and modifying biological systems. Accordingly, both approaches provide excellent sources for philosophical discussions of interdisciplinary integration, particularly the implications of the increasing embedding of mathematical and computational approaches in biology. Some practices encourage philosophers to revisit classical philosophical topics such as reductionism and scientific explanation, but systems and synthetic biology also broaden the scope of philosophical topics to include data-intensive practices and modeling strategies towards the aims of design and control.

Since this entry has examined the philosophical implications of both systems biology and synthetic biology, much attention has been given to the implications of engineering approaches, including the quest for so-called design principles. It is, however, important to note that systems biology and synthetic biology cover a broad spectrum of research practices, some of which are more strongly inspired by chemistry or physics than engineering. This entry should thus be taken as an attempt to only cover some ground of the vast philosophical landscape that these research fields reach into. With the rapid development of both approaches and their explicit aim to address grand scientific and societal challenges, exciting times lie ahead for philosophy of biology.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=systems-synthetic-biology). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/systems-synthetic-biology/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=systems-synthetic-biology&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/systems-synthetic-biology/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Cancer Genome Atlas](https://cancergenome.nih.gov/)
- [Elowitz Lab](http://www.elowitz.caltech.edu/research.html)
- [Gene Ontology Resource](http://geneontology.org/)
- [GWAS catalogue](https://www.ebi.ac.uk/gwas/)
- [International Genetically Engineered Machine Competition](http://igem.org/Main_Page)
- [Network Motifs](http://www.weizmann.ac.il/mcb/UriAlon/research/network-motifs), Uri Alon Lab, Molecular Cell Biology, Weizmann Institute of Science.
- [International Society for Systems Biology](http://www.issb.org/)
- [J. Craig Venter Institute](https://www.jcvi.org/)
- [Open WetWare](http://www.openwetware.org/wiki/Main_Page)
- [Physiome Project](http://physiomeproject.org/)
- [Virtual Cell](http://vcell.org/)
- [VPH Institute](http://www.vph-institute.org/what-is-vph-institute.html) (Virtual Physiological Human)

## Related Entries

[artificial intelligence](https://plato.stanford.edu/entries/artificial-intelligence/)  | adaptationism | biology: philosophy of | cancer | emergent properties | genetics: molecular | genomics and postgenomics | mechanism in science | molecular biology | reduction, scientific: in biology | scientific explanation: 20th century theories | scientific explanation: causal approaches to

### Acknowledgments

Lucy Holt, Maria Serban, Sune Holm, William Bechtel, Fridolin Gross, Mikkel W. Johannsen, Line Andersen, Leonardo Bich, Javier Suarez, and an anonymous reviewer provided extremely valuable comments to an earlier version of this entry.

## Notes（原文脚注）

## Notes to Philosophy of Systems and Synthetic Biology

[^note-1]: Systems theory is the study of generic properties of complex systems through mathematical or formal representations. The aim to identify principles shared by a class of systems with a similar organization is also important to some modern systems biologists. For an analysis of the connection between systems theory and modern systems biology, see e.g. (Drack 2015; Drack & Wolkenhauer 2011; Green & Wolkenhauer 2013; Mekios 2016; Wolkenhauer & Mesarović 2005)[^drack-2015][^drack-2011][^green-2013][^mekios-2016][^wolkenhauer-2013][^wolkenhauer-2005].

[^note-2]: They also emphasize the differences between bottom-up and top-down strategies. The former is commonly understood as model construction based on detailed experimental analysis, akin to strategies in molecular biology. In contrast, top-down strategies are often understood as pattern-detection and functional inference based on larger, but also coarser-grained, datasets (see also MacLeod & Nersessian 2013a,b, 2015)[^macleod-2013a].

[^note-3]: The term scale-free signifies that the connectivity pattern—described mathematically as a power law distribution—is invariant across the scale (or size) of the network (Barabási & Albert 1999)[^barabási-1999].

[^note-4]: Another candidate of artificial life with a different “design” than living systems, as we know them, is a type of protocells whose metabolic processes operate at the cell surface (Rasmussen et al. 2008)[^rasmussen-2008].

[^note-5]: Among the important precursors is the classical Miller-Urey experiment showing that organic compounds (amino acids) can originate from inorganic substrates under prebiotic conditions (Miller 1953)[^miller-1953].

[^note-6]: A related example shows that the cellular context may play adaptive roles in ensuring robustness. A synthetic model of a dual-feedback oscillator surprisingly outperformed the mathematical model by exhibiting robust oscillations for wider range of parameters than predicted (Stricker et al. 2008; Knuuttila & Loettgers 2013a)[^knuuttila-2013a][^stricker-2008].

[^note-7]: Note also that some approaches are compatible with a form of modular reductionism, e.g., the aim to design simpler synthetic systems allowing for assembly of modular parts (Endy 2005; Güttinger 2013)[^endy-2005][^güttinger-2013].

[^note-8]: A related aspect is the focus on quantitative features, including concentration, that may require an extension of traditional mechanistic accounts (Love & Nathan 2015)[^love-2015].

[^abrahamsen-2015]: Abrahamsen, Adele & William Bechtel, 2015, “Diagrams as Tools for Scientific Reasoning”, *Review of Philosophy and Psychology*, 6(1): 117–131. doi:10.1007/s13164-014-0215-2

[^alberghina-2005]: Alberghina, Lilia & Hans V. Westerhoff, 2005, *Systems Biology: Definitions and Perspectives*, New York: Springer. doi:10.1007/b95175

[^albert-2000]: Albert, Réka, Hawoong Jeong, & Albert-László Barabási, 2000, “Error and Attack Tolerance of Complex Networks”, *Nature*, 406(6794): 378–382. doi:10.1038/35019019

[^allen-2001]: Allen, John F., 2001, “Bioinformatics and Discovery: Induction Beckons Again”, *BioEssays*, 23(1): 104–107. doi:10.1002/1521-1878(200101)23:1<104::AID-BIES1013>3.0.CO;2-2

[^alon-2007]: Alon, Uri, 2007, *An Introduction to Systems Biology: Design Principles of Biological Circuits*, Boca Raton, FL: Chapman and Hall.

[^alves-2011]: Alves, Rui & Albert Sorribas, 2011, “Special Issue on Biological Design Principles”, *Mathematical Biosciences*, 231: 1–2. doi:10.1016/j.mbs.2011.03.009

[^andersen-2016]: Andersen, Hanne, 2016, “Collaboration, Interdisciplinarity, and the Epistemology of Contemporary Science”, *Studies in History and Philosophy of Science Part A*, 56: 1–10. doi:10.1016/j.shpsa.2015.10.006

[^andrianantoandro-2006]: Andrianantoandro, Erenesto, Subhayu Basu, David K. Karig, & Ron Weiss, 2006, “Synthetic Biology: New Engineering Rules for an Emerging Discipline”, *Molecular Systems Biology*, 2: 2006.0028. doi:10.1038/msb4100073

[^ankeny-2015]: Ankeny, Rachel A. & Sabina Leonelli, 2015, “Valuing Data in Postgenomic Biology: How Data Donation and Curation Practices Challenge the Scientific Publication System”, in *PostGenomics. Perspectives on Biology after the Genome*, Sarah S. Richardson & Hallam Stevens (eds.), Durham, NC: Duke University Press, pp. 126–149.

[^baker-2005]: Baker, Alan, 2005, “Are There Genuine Mathematical Explanations of Physical Phenomena?”, *Mind*, 114(454): 223–238. doi:10.1093/mind/fzi223

[^bapteste-2021]: Bapteste, Eric, and François Papale, 2021, “Modeling the Evolution of Interconnected Processes: It is the Song and the Singers: Tracking Units of Selection with Interaction Networks”, *BioEssays*, 43(1): 2000077.

[^barabási-2002]: Barabási, Albert-László, 2002, *Linked: How Everything is Connected to Everything Else and What it Means for Business, Science, and Everyday Life*, New York, NY: Basic Books/Perseus Publishing.

[^barabási-1999]: Barabási, Albert-László & Réka Albert, 1999, “Emergence of Scaling in Random Networks”, *Science*, 286(5439): 509–512. doi:10.1126/science.286.5439.509

[^barabási-2004]: Barabási, Albert-László & Zoltán N. Oltvai, 2004, “Network Biology: Understanding the Cell’s Functional Organization”, *Nature Reviews Genetics*, 5(2): 101–113. doi:10.1038/nrg1272

[^barabási-2011]: Barabási, Albert-László, Natali Gulbahce, & Joseph Loscalzo, 2011, “Network Medicine: a Network-based Approach to Human Disease”, *Nature Reviews Genetics*, 12(1): 56–68. doi:10.1038/nrg2918

[^barrett-2006]: Barrett, Christian L., Tae Yong Kim, Hyun Uk Kim, Bernhard Ø. Palsson, & Sang Yup Lee, 2006, “Systems Biology as a Foundation for Genome-scale Synthetic Biology”, *Current Opinion in Biotechnology*, 17(5): 488–492. doi:10.1016/j.copbio.2006.08.001

[^bartol-2013]: Bartol, Jordan, 2013, “Re-examining the Gene in Personalized Genomics”, *Science & Education*, 22(10): 2529–2546. doi:10.1007/s11191-012-9484-2

[^bassingthwaighte-2009]: Bassingthwaighte, James, Peter Hunter, & Denis Noble, 2009, “The Cardiac Physiome: Perspectives for the Future”, *Experimental Physiology*, 94(5): 597–605. doi:10.1113/expphysiol.2008.044099

[^batterman-2014]: Batterman, Robert W., & Collin Rice, 2014, “Minimal model explanations”, *Philosophy of Science*, 81(3): 349–376.

[^batterman-2021]: Batterman, Robert W., and Sara Green. 2021, “Steel and Bone: Mesoscale Modeling and Middle-Out Strategies in Physics and Biology”, *Synthese*, 199(1): 1159–1184.

[^bechtel-2015a]: Bechtel, William, 2015a, “Can Mechanistic Explanation be Reconciled with Scale-free Constitution and Dynamics?”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 53: 84–93. doi:10.1016/j.shpsc.2015.03.006

[^bechtel-2015b]: –––, 2015b, “Generalizing Mechanistic Explanations Using Graph-theoretic Representations”, in Braillard & Malaterre 2015: 199–225. doi:10.1007/978-94-017-9822-8_9

[^bechtel-2016]: –––, 2016, “Mechanists Must be Holists Too! Perspectives from Circadian Biology”, *Journal of the History of Biology*, 49(4): 705–731. doi:10.1007/s10739-016-9439-6

[^bechtel-2020]: –––, 2020, “Hierarchy and Levels: Analysing Networks to Study Mechanisms in Molecular Biology”, *Philosophical Transactions of the Royal Society B*, 375(1796): 20190320. doi:10.1098/rstb.2019.0320

[^bechtel-2011]: Bechtel, William & Adele A. Abrahamsen, 2011, “Complex Biological Mechanisms: Cyclic, Oscillatory, and Autonomous”, in *Philosophy of Complex Systems* (Handbook of the Philosophy of Science, 10), Cliff A. Hooker (ed.), Amsterdam: Elsevier, pp. 257–285.

[^bechtel-2012]: –––, 2012, “Thinking Dynamically About Biological Mechanisms: Networks of Coupled Oscillators”, *Foundations of Science*, 18(4): 707–723. doi:10.1007/s10699-012-9301-z

[^bechtel-1993]: Bechtel, William & Richard C. Richardson, 1993 [2010], *Discovering Complexity: Decomposition and Localization as Strategies in Scientific Research*, Princeton, NJ: Princeton University Press. Reprinted by the MIT Press in 2010.

[^bedau-2009]: Bedau, Mark A., 2009, “Living Technology Today and Tomorrow”, *Technoetic Arts*, 7(2): 199–206. doi:10.1386/tear.7.2.199/1

[^bedau-2010]: Bedau, Mark A. & Carol E. Cleland, 2010, *The Nature of Life: Classical and Contemporary Perspectives from Philosophy and Science*, Cambridge, MA: Cambridge University Press.

[^benner-2005]: Benner, Steven A. & A. Michael Sismour, 2005, “Synthetic Biology”, *Nature Reviews Genetics*, 6(7): 533–543. doi:10.1038/nrg1637

[^bensaude-vincent-2009]: Bensaude-Vincent, Bernadette, 2009, “The Chemists’ Style of Thinking”, *Berichte zur Wissenschaftsgeschichte*, 32(4): 365–378. doi:10.1002/bewi.200901385

[^bensaude-vincent-2013]: –––, 2013, “Discipline-building in Synthetic Biology”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(2): 122–129. doi:10.1016/j.shpsc.2013.03.007

[^bensaude-vincent-2015]: –––, 2015, “Life by Design: Philosophical Perspectives on Synthetic Biology”, *BIO Web of Conferences*, 4: 00015. doi:10.1051/bioconf/20150400015

[^bertolaso-2011]: Bertolaso, Marta, 2011, “Hierarchies and Causal Relationships in Interpretative Models of the Neoplastic Process”,

[^bertolaso-2016]: –––, 2016, *Philosophy of Cancer. A Dynamic and Relational View*, Rome: Springer International Publishing.*History and Philosophy of the Life Sciences*, 33(4): 515–536.

[^bich-2010]: Bich, Leonardo, 2010, “Biological Autonomy and Systemic Integration”, *Origins of Life and Evolution of Biospheres*, 40(4): 480–484. doi:10.1007/s11084-010-9213-2

[^bich-2020]: –––, 2020, “Interactive Models in Synthetic Biology: Exploring Biological and Cognitive Inter-Identities”, *Frontiers in Psychology*, 11: 682. doi:10.3389/fpsyg.2020.00682

[^bich-2007]: Bich, Leonardo & Luisa Damiano, 2007, “Question 9: Theoretical and Artificial Construction of the Living: Redefining the Approach from an Autopoietic Point of View”, *Origins of Life and Evolution of Biospheres*, 37(4): 459–464. doi:10.1007/s11084-007-9082-5

[^bich-2008]: –––, 2008, “Order in the Nothing: Autopoiesis and the Organizational Characterization of the Living”, in *Physics of Emergence and Organization*, Ignazio Licata & Ammar Sakaji (eds.), Singapore: World Scientific, pp. 339–369. doi:10.1142/9789812779953_0015

[^bich-2018]: Bich, Leonardo & Sara Green, 2018, “Is Defining Life Pointless? Operational Definitions at the Frontiers of Biology”, *Synthese*, 195: 3919–3946. doi:10.1007/s11229-017-1397-9

[^boogerd-2017]: Boogerd, Fred C., 2017, “Systems Biology in the Broad Sense”, in Green 2017: 49–58. doi:10.1007/978-3-319-47000-9_4

[^boogerd-2007]: Boogerd, Fred C., Frank J. Bruggeman, Jan-Hendrik S. Hofmeyr, & Hans V. Westerhoff, 2007 (eds.), *Systems Biology: Philosophical Foundations*, Amsterdam: Elsevier.

[^boogerd-2013]: Boogerd, Fred C., Frank J. Bruggeman, & Robert C. Richardson, 2013, “Mechanistic Explanations and Models in Molecular Systems Biology”, *Foundations of Science*, 18(4): 725–744. doi:10.1007/s10699-012-9302-y

[^boogerd-2005]: Boogerd, Fred C., Frank J. Bruggeman, Robert C. Richardson, A. Stephan, & Hans V. Westerhoff, 2005, “Emergence and Its Place in Nature: A Case Study of Biochemical Networks”, *Synthese*, 145(1): 131–164. doi:10.1007/s11229-004-4421-9

[^boudry-2013]: Boudry, Maarten & Massimo Pigliucci, 2013, “The Mismeasure of Machine: Synthetic Biology and the Trouble with Engineering Metaphors”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(4): 660–668. doi:10.1016/j.shpsc.2013.05.013

[^braillard-2010]: Braillard, Pierre-Alain, 2010, “Systems Biology and the Mechanistic Framework”, *History and Philosophy of the Life Sciences*, 32(1): 43–62.

[^braillard-2015]: –––, 2015, “Prospect and Limits of Explaining Biological Systems in Engineering Terms”, in Braillard & Malaterre 2015: 319–344. doi:10.1007/978-94-017-9822-8_14

[^braillard-2015-2]: Braillard Pierre-Alain & Christophe Malaterre (eds.), 2015, *Explanation in Biology. An Enquiry into the Diversity of Explanatory Patterns in the Life Sciences*, Dordrecht: Springer. doi:10.1007/978-94-017-9822-8

[^briat-2016]: Briat, Corentin, Ankit Gupta, & Mustafa Khammash, 2016, “Antithetic Integral Feedback Ensures Robust Perfect Adaptation in Noisy Biomolecular Networks”, *Cell Systems*, 2(1): 15–26. doi:10.1016/j.cels.2016.01.004

[^brigandt-2013]: Brigandt, Ingo, 2013, “Systems Biology and the Integration of Mechanistic Explanation and Mathematical Explanation”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(4): 477–492. doi:10.1016/j.shpsc.2013.06.002

[^brigandt-2015]: Brigandt, Ingo, 2015, “Evolutionary Developmental Biology and the Limits of Philosophical Accounts of Mechanistic Explanation”, in Braillard & Malaterre 2015: 135–173.

[^brigandt-2017]: Brigandt, Ingo & Alan Love, 2017, “Reductionism in Biology”, *The Stanford Encyclopedia of Philosophy* (Spring 2017 Edition), Edward N. Zalta (ed.). URL = <[https://plato.stanford.edu/archives/spr2017/entries/reduction-biology/](https://plato.stanford.edu/archives/spr2017/entries/reduction-biology/)>.

[^brigandt-2018]: Brigandt, Ingo, Sara Green, & Maureen O’Malley, 2018, “Systems Biology and Mechanistic Explanation”, in Glennan & Illari 2018: 362–374.

[^burian-1996]: Burian, Richard M., Robert C. Richardson, & Wim J. Van der Steen, 1996, “Against Generality: Meaning in Genetics and Philosophy”, *Studies in History and Philosophy of Science*, 27(1): 1–29. doi:10.1016/0039-3681(95)00034-8

[^bursten-2021]: Bursten, Julia R.S., 2021, ed., *Perspectives on Classification in Synthetic Sciences. Unnatural kinds*. Routledge.

[^calcott-2014]: Calcott, Brett, 2014, “Engineering and Evolvability”, *Biology & Philosophy*, 29(3): 293–313. doi:10.1007/s10539-014-9425-3

[^calcott-2015]: Calcott, Brett, Arnon Levy, Mark L. Siegal, Orkun S. Soyer, & Andreas Wagner, 2015, “Engineering and Biology: Counsel for a Continued Relationship”, *Biological Theory*, 10(1): 50–59. doi:10.1007/s13752-014-0198-3

[^calvert-2010]: Calvert, Jane, 2010, “Systems Biology, Interdisciplinarity and Disciplinary Identity”, in *Collaboration in the New Life Sciences*, John N. Parker, Niki Vermeulen & Bart Penders (eds.), Farnham, Surrey: Ashgate, pp. 219–244.

[^calvert-2012]: –––, 2012, “Systems Biology, Synthetic Biology and Data-driven Research: a Commentary on Krohs, Callebaut, and O’Malley and Soyer”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 43(1): 81–84. doi:10.1016/j.shpsc.2011.10.008

[^calvert-2015]: Calvert, Jane & Emma Frow, 2015, “Synthetic Yeast Project as a Topic for Social Scientific Investigation”, *The Macquarie Law Journal*, 15: 27–37. [[Calvert & Frow 2015 available online](http://www.austlii.edu.au/au/journals/MqLawJl/2015/3.html)]

[^calvert-2011]: Calvert, Jane & Joan H. Fujimura, 2011, “Calculating Life? Duelling Discourses in Interdisciplinary Systems Biology”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 42(2): 155–163. doi:10.1016/j.shpsc.2010.11.022

[^carrara-2012]: Carrara, Paolo, Pasquale Stano, & Pier Luigi Luisi, 2012, “Giant Vesicles ‘Colonies’: a Model for Primitive Cell Communities”, *ChemBioChem*, 13(1): 1497–1502. doi:10.1002/cbic.201200133

[^carusi-2011]: Carusi, Annamaria, 2011, “Computational Biology and the Limits of Shared Vision”, *Perspectives on Science*, 19(3): 300–335. doi:10.1162/POSC_a_00044

[^carusi-2012]: –––, 2012, “Making the Visual Visible in Philosophy of Science”, *Spontaneous Generations: A Journal for the History and Philosophy of Science*, 6(1): 106–114. doi:10.4245/sponge.v6i1.16141

[^carusi-2014]: –––, 2014, “Validation and Variability: Dual Challenges on the Path from Systems Biology to Systems Medicine”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 48(part A): 28–37. doi:10.1016/j.shpsc.2014.08.008

[^carusi-2012-2]: Carusi, Annamaria, Kevin Burrage, & Bianca Rodríguez, 2012, “Bridging Experiments, Models and Simulations: An Integrative Approach to Validation in Computational Cardiac Electrophysiology”, *American Journal of Physiology—Heart and Circulatory Physiology*, 303(2): H144–H155. doi:10.1152/ajpheart.01151.2011

[^chan-2005]: Chan, Leon Y., Sriram Kosuri, & Drew Endy, 2005, “Refactoring Bacteriophage T7”, *Molecular Systems Biology*, 1: 2005.0018. doi:10.1038/msb4100025

[^choffnes-2011]: Choffnes, Eileen R., David A. Relman, & Leslie Pray, 2011, *The Science and Applications of Synthetic and Systems Biology: Workshop Summary*, Washington, DC: National Academies Press.

[^christiansen-2016a]: Christiansen, Andreas, 2016a, “Synthetic Biology and the Moral Significance of Artificial Life: A Reply to Douglas, Powell and Savulescu”, *Bioethics*, 30(5): 372–9. doi:10.1111/bioe.12248

[^christiansen-2016b]: –––, 2016b, *The Ethics of Synthetic Biology. Respecting Life and Managing Risk*, PhD thesis, Department of Media, Cognition and Communication, University of Copenhagen.

[^cleland-2012]: Cleland, Carol E., 2012, “Life Without Definitions”, *Synthese*, 185(1): 125–144. doi:10.1007/s11229-011-9879-7

[^costanzo-2010]: Costanzo, Michael, Anastasia Baryshnikova, Jeremy Bellay, et al., 2010, “The Genetic Landscape of a Cell”, *Science*, 327(5964): 425–431. doi:10.1126/science.1180823

[^cordero-2006]: Cordero, Otto X. & Paulien Hogeweg, 2006, “Feed-forward Loop Circuits as a Side Effect of Genome Evolution”, *Molecular Biology and Evolution*, 23(1): 1931–1936. doi:10.1093/molbev/msl060

[^cornish-bowden-2006]: Cornish-Bowden, Athel, 2006, “Putting the Systems Back into Systems Biology”, *Perspectives in Biology and Medicine*, 49(4): 475–489. doi:10.1353/pbm.2006.0053

[^craver-2016]: Craver, Carl F., 2016. “The Explanatory Power of Network Models”, *Philosophy of Science*, 83(5): 698–709. doi:10.1086/687856

[^craver-2015]: Craver, Carl & James Tabery 2015, “Mechanisms in Science”, *The Stanford Encyclopedia of Philosophy*, Edward N. Zalta (ed.). URL= <[https://plato.stanford.edu/archives/spr2017/entries/science-mechanisms/](https://plato.stanford.edu/archives/spr2017/entries/science-mechanisms/)>

[^csete-2002]: Csete, Marie E. & John C. Doyle, 2002, “Reverse Engineering of Biological Complexity”, *Science*, 295(5560): 1664–1669. doi:10.1126/science.1069981

[^darden-2002]: Darden, Lindley, 2002, “Strategies for Discovering Mechanisms: Schema Instantiation, Modular Subassembly, Forward/Backward Chaining”, *Philosophy of Science*, 69(S3): S354–S365.

[^de-2010]: De Backer, Philippe, Danny De Waele, & Linda Van Speybroeck, 2010, “Ins and Outs of Systems Biology vis-à-vis Molecular Biology: Continuation or Clear Cut?”, *Acta Biotheoretica*, 58: 15–49. doi:10.1007/s10441-009-9089-6

[^lichtenberg-2005]: de Lichtenberg, Ulrik, Lars Juhl Jensen, Søren Brunak, & Peer Bork, 2005, “Dynamic Complex Formation During the Yeast Cell Cycle”, *Science*, 307(5710): 724–727. doi:10.1126/science.1105103

[^souza-2014]: de Souza, Teresa Pereira, Alfred Fahr, Pier Luigi Luisi, & Pasquale Stano, 2014, “Spontaneous Encapsulation and Concentration of Biological Macromolecules in Liposomes: An Intriguing Phenomenon and Its Relevance in Origins of Life”, *Journal of Molecular Evolution*, 79(5): 179–192. doi:10.1007/s00239-014-9655-7

[^deulofeu-2021]: Deulofeu, Roger, Javier Suárez, and Alberto Pérez-Cervera, 2021, “Explaining the Behaviour of Random Ecological Networks: The Stability of the Microbiome as a Case of Integrative Pluralism”, *Synthese*, 198(3): 2003–2025. doi:10.1007/s11229-019-02187-9

[^deplazes-2009]: Deplazes, Anna, 2009, “Piecing Together a Puzzle”, *EMBO Reports*, 10(5): 428–432. doi:10.1038/embor.2009.76

[^del-2010]: Del Sol, Antonio, Rudi Balling, Leroy Hood, & David Galas, 2010, “Diseases as Network Perturbations”, *Current Opinion in Biotechnology*, 21(4): 566–571. doi:10.1016/j.copbio.2010.07.010

[^difrisco-2019]: DiFrisco, James, & Johannes Jaeger, 2019, “Beyond Networks: Mechanism and Process in Evo-Devo”, *Biology & Philosophy*, 34(6): 1–24.

[^douglas-2013]: Douglas, Thomas, Russell Powell, & Julian Savulescu, 2013, “Is the Creation of Artificial Life Morally Significant?”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(4, part B): 688–696. doi:10.1016/j.shpsc.2013.05.016

[^doyle-2006]: Doyle, Francis J. & Jörg Stelling, 2006, “Systems Interface Biology”, *Journal of the Royal Society Interface*, 3(10): 603–616. doi:10.1098/rsif.2006.0143

[^drack-2015]: Drack, Manfred, 2015, “Ludwig von Bertalanffy’s Organismic View on the Theory of Evolution”, *Journal of Experimental Zoology Part B: Molecular and Developmental Evolution*, 324(2): 77–90. doi:10.1002/jez.b.22611

[^drack-2011]: Drack, Manfred & Olaf Wolkenhauer, 2011, “System Approaches of Weiss and Bertalanffy and Their Relevance for Systems Biology Today”, *Seminars in Cancer Biology*, 21(3): 150–155. doi:10.1016/j.semcancer.2011.05.001

[^dupré-2009]: Dupré, John, & Maureen A. O’Malley, 2009, “Varieties of Living Things: Life at the Intersection of Lineage and Metabolism”, *Philosophy and Theory in Biology*, 1: e003. doi:10.3998/ptb.6959004.0001.003

[^elowitz-2000]: Elowitz, Michael B. & Stanislas Leibler, 2000, “A Synthetic Oscillatory Network of Transcriptional Regulators”, *Nature*, 403(6767): 335–338. doi:10.1038/35002125

[^emmeche-2000]: Emmeche, Claus, Simo Køppe, & Frederick Stjernfeldt, 2000, “Levels, Emergence, and Three Versions of Downward Causation”, in *Downward Causation. Minds, Bodies and Matter*, Peter Bøgh Andersen, Claus Emmeche, Niels Ole Finnemann & Peder Voetmann Christiansen (eds.), Aarhus, Denmark: Aarhus University Press, pp. 13–33.

[^endy-2005]: Endy, Drew, 2005, “Foundations for Engineering Biology”, *Nature*, 438(7067): 449–453. doi:10.1038/nature04342

[^fagan-2012]: Fagan, Melinda Bonnie, 2012, “Waddington Redux: Models and Explanation in Stem Cell and Systems Biology”, *Biology & Philosophy*, 27(2): 179–213. doi:10.1007/s10539-011-9294-y

[^fagan-2015]: –––, 2015, “Collaborative Explanation and Biological Mechanisms”, *Studies in History and Philosophy of Science Part A*, 52: 67–78. doi:10.1016/j.shpsa.2015.03.004

[^fagan-2016]: –––, 2016, “Stem Cells and Systems Models: Clashing Views of Explanation”, *Synthese*, 193(3): 873–907. doi:10.1007/s11229-015-0776-3

[^fang-2020]: Fang, Wei, 2020, “Multiple Realization in Systems Biology”, *Philosophy of Science*, 87: 663–684.

[^gardner-2000]: Gardner, Timothy S., Charles R. Cantor, & James J. Collins, 2000, “Construction of a Toggle Switch in *Escherichia coli*”, *Nature*, 403: 339–342(6767). doi:10.1038/35002131

[^gelfert-2013]: Gelfert, Axel, 2013, “Synthetic Biology Between Technoscience and Thing Knowledge”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(2): 141–149. doi:10.1016/j.shpsc.2013.03.009

[^georgianna-2012]: Georgianna, D. Ryan & Stephen P. Mayfield, 2012, “Exploiting Diversity and Synthetic Biology for the Production of Algal Biofuels”, *Nature*, 488(7411): 329–335. doi:10.1038/nature11479

[^gibson-2010]: Gibson, Daniel G., John I. Glass, Carole Lartigue, Vladimir N. Noskov, Ray-Yuan Chuang, Mikkel A. Algire, et al., 2010, “Creation of a Bacterial Cell Controlled by a Chemically Synthesized Genome”, *Science*, 329(5987): 52–56. doi:10.1126/science.1190719

[^ginsberg-2015]: Ginsberg, Alexandra Daisy, Jane Calvert, Pablo Schyfter, Alistair Elfick, & Drew Endy 2015, *Synthetic Aesthetics. Investigating Synthetic Biology’s Designs on Nature*, Cambridge, MA: MIT press.

[^glennan-2002]: Glennan, Stuart, 2002, “Rethinking Mechanistic Explanation”, *Philosophy of Science*, 69(S3): 342–353. doi:10.1086/341857

[^goodwin-1993]: Goodwin, Brian C., Stuart Kauffman, & J.D. Murray, 1993, “Is Morphogenesis An Intrinsically Robust Process?”, *Journal of Theoretical Biology*, 163(1): 135–144. doi:10.1006/jtbi.1993.1112

[^gramelsberger-2013]: Gramelsberger, Gabriele, 2013, “The Simulation Approach in Synthetic Biology”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(2): 150–157. doi:10.1016/j.shpsc.2013.03.010

[^gramelsberger-2017]: –––, 2017, “Problems in Mathematizing Systems Biology”, in Green 2017: 99–108. doi:10.1007/978-3-319-47000-9_9

[^gramelsberger-2013-2]: Gramelsberger, Gabriele, Tarja Knuuttila, & Axel Gelfert, 2013, “Philosophical Perspectives on Synthetic Biology”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(2): 119–121. doi:10.1016/j.shpsc.2013.03.006

[^green-2014]: Green, Sara, 2014, “A Philosophical Evaluation of Adaptationism as a Heuristic Strategy”, *Acta Biotheoretica*, 62(4): 479–498. doi:10.1007/s10441-014-9232-x

[^green-2015a]: –––, 2015a, “Can Biological Complexity be Reverse Engineered?”, *Studies in History and Philosophy of Biology and Biomedical Sciences*, 53: 73–83. doi:10.1016/j.shpsc.2015.03.008

[^green-2015b]: –––, 2015b, “Revisiting Generality in the Life Sciences: Systems Biology and the Quest for Design Principles”, *Biology & Philosophy*, 30(5): 629–652. doi:10.1007/s10539-015-9496-9

[^green-2017]: –––, (ed.), 2017, *Philosophy of Systems Biology: Perspectives from Scientists and Philosophers*, Cham, Switzerland: Springer International Publishing. doi:10.1007/978-3-319-47000-9

[^green-2018]: –––, 2018, “Scale Dependency and Downward Causation in Biology”, *Philosophy of Science*, 85(5): 998–1011.

[^green-2016]: Green, Sara & Nicholaos Jones, 2016, “Constraint- Based Reasoning for Search and Explanation: Strategies for Understanding Variation and Patterns in Biology”, *Dialectica*, 70(3): 343–374. doi:10.1111/1746-8361.12145

[^green-2013]: Green, Sara & Olaf Wolkenhauer, 2013, “Tracing Organizing Principles: Learning from the History of Systems Biology”, *History and Philosophy of the Life Sciences*, 35(4): 553–576.

[^green-2015a-2]: Green, Sara, Melinda Fagan, & Johannes Jaeger, 2015a, “Explanatory Integration Challenges in Evolutionary Systems Biology”, *Biological Theory*, 10(1): 18–35. doi:10.1007/s13752-014-0185-8

[^green-2015b-2]: Green, Sara, Arnon Levy, & William Bechtel, 2015b, “Design Sans Adaptation”, *European Journal of Philosophy of Science*, 5(1): 15–29. doi:10.1007/s13194-014-0096-3

[^green-2016-2]: Green, Sara & Henrik Vogt, 2016, “Personalizing Medicine: Disease Prevention *in Silico* and *in Socio*”, *Humana.Mente Journal of Philosophical Studies*, 30: 105–145.

[^green-2018-2]: Green, Sara, Maria Şerban, Raphael Scholl, Nicholaos Jones, Ingo Brigandt, & William Bechtel, 2018, “Network Analyses in Systems Biology: New Strategies for Dealing with Biological Complexity”, *Synthese*, 195: 1751–1777. doi:10.1007/s11229-016-1307-6

[^gross-2011]: Gross, Fridolin, 2011, “What Systems Biology Can Tell Us About Disease”, *History and Philosophy of the Life Sciences*, 33(4): 477–496.

[^gross-2015]: –––, 2015, “The Relevance of Irrelevance: Explanation in Systems Biology”, in Braillard & Malaterre 2015: 175–198. doi:10.1007/978-94-017-9822-8_8

[^gross-2017]: –––, 2017, “Towards a Methodology for Systems Biology”, in Green 2017: 109–116. doi:10.1007/978-3-319-47000-9_10

[^gross-2019]: –––, 2019, “Occam’s Razor in Molecular and Systems Biology”, *Philosophy of Science*, 86(5): 1134–1145.

[^gross-2017-2]: Gross, Fridolin & Sara Green, 2017, “The Sum of the Parts: Large-scale Modeling in Systems Biology”, *Philosophy, Theory and Practice in Biology*, 9: 10.

[^güttinger-2013]: Güttinger, Stephan, 2013, “Creating Parts that Allow for Rational Design: Synthetic Biology and the Problem of Context-sensitivity”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(2): 199–207. doi:10.1016/j.shpsc.2013.03.015

[^güttinger-2016]: Güttinger, Stephan, & John Dupré, 2016, “Genomics and Postgenomics”, *The Stanford Encyclopedia of Philosophy* (Winter 2016 Edition), Edward N. Zalta (ed.). URL = <[https://plato.stanford.edu/archives/win2016/entries/genomics/](https://plato.stanford.edu/archives/win2016/entries/genomics/)>.

[^hartwell-1999]: Hartwell, Leland H., John J. Hopfield, Stanislas Leibler, & Andrew W. Murray, 1999, “From Molecular to Modular Cell Biology”, *Nature*, 402(supp): C47–C52. doi:10.1038/35011540

[^hey-2015]: Hey, Spencer Phillips, 2015, “Judging Quality and Coordination in Biomarker Diagnostic Development”, *THEORIA. Revista de Teoría, Historia y Fundamentos de la Ciencia*, 30(2): 207–227. doi:10.1387/theoria.12697

[^hofmeyr-2007]: Hofmeyr, Jan-Hendrik S., 2007, “The Biochemical Factory that Autonomously Fabricates Itself: a Systems Biological View of the Living Cell”, in Boogerd, Bruggeman, Hofmeyr, & Westerhoff 2007: 215–242.

[^hofmeyr-2017]: –––, 2017, “Exploring the Metabolic Marketplace Through the Lens of Systems Biology”, in Green 2017: 117–124. doi:10.1007/978-3-319-47000-9_11

[^hogeweg-2012]: Hogeweg, Paulien, 2012, “Toward a Theory of Multilevel Evolution: Long-term Information Integration Shapes the Mutational Landscape and Enhances Evolvability”, in Soyer 2012: 195–223. doi:10.1007/978-1-4614-3567-9_10

[^holm-2012]: Holm, Sune, 2012, “Biological Interests, Normative Functions, and Synthetic Biology”, *Philosophy & Technology*, 25(4): 525–541. doi:10.1007/s13347-012-0075-6

[^holm-2013]: –––, 2013, “Health as a Property of Engineered Living Systems”, *Bioethics*, 27(8): 419–425. doi:10.1111/bioe.12053

[^holm-2014]: –––, 2014, “Disease, Dysfunction, and Synthetic Biology”, *Journal of Medicine and Philosophy*, 39(4): 329–45. doi:10.1093/jmp/jhu025

[^holm-2015]: –––, 2015, “Is Synthetic Biology Mechanical Biology?”, *History and Philosophy of the Life Sciences*, 37(4): 413–429. doi:10.1007/s40656-015-0081-y

[^holm-2013-2]: Holm, Sune & Russell Powell, 2013, “Organism, Machine, Artifact: The Conceptual and Normative Challenges of Synthetic Biology”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(4, partB): 627–631. doi:10.1016/j.shpsc.2013.05.009

[^hood-2015]: Hood, Leroy, Jennifer C. Lovejoy, & Nathan D. Price, 2015, “Integrating Big Data and Actionable Health Coaching to Optimize Wellness”, *BMC Medicine*, 13: 4. doi:10.1186/s12916-014-0238-7

[^huang-2011]: Huang, Sui, 2011, “Systems Biology of Stem Cells: Three Useful Perspectives to Help Overcome the Paradigm of Linear Pathways”, *Philosophical Transactions of the Royal Society B: Biological Sciences*, 366(1575): 2247–2259. doi:10.1098/rstb.2011.0008

[^huang-2012]: –––, 2012, “The Molecular and Mathematical Basis of Waddington’s Epigenetic Landscape: a Framework for Post-Darwinian Biology?”, *BioEssays*, 34(2): 149–157. doi:10.1002/bies.201100031

[^huang-2009]: Huang, Sui, Ingemar Ernberg, & Stuart Kauffman, 2009, “Cancer Attractors: a Systems View of Tumors from a Gene Network Dynamics and Developmental Perspective”, *Seminars in Cell & Developmental Biology*, 20(7): 869–876. doi:10.1016/j.semcdb.2009.07.003

[^humphreys-2004]: Humphreys, Paul, 2004, *Extending Ourselves: Computational Science, Empiricism, and Scientific Method*, Oxford, NY: Oxford University Press.

[^huneman-2010]: Huneman, Phillippe, 2010, “Topological Explanations and Robustness in Biological Sciences”, *Synthese*, 177(2): 213–245. doi:10.1007/s11229-010-9842-z

[^hunter-2013]: Hunter, Peter, Tara Chapman, Peter V. Coveney, et al., 2013, “A Vision and Strategy for the Virtual Physiological Human: 2012 Update”, *Interface Focus*, 3(2): 20130004. doi:10.1098/rsfs.2013.0004

[^hutchison-2016]: Hutchison, Clyde A., Ray-Yuan Chuang, Vladimir N. Noskov, Nacyra Assad-Garcia, Thomas J. Deerinck, Mark H. Ellisman, et al., 2016, “Design and Synthesis of a Minimal Bacterial Genome”, *Science*, 351(6280): aad6253. doi:10.1126/science.aad6253

[^isalan-2008]: Isalan, Mark, Caroline Lemerle, Konstantionos Michalodimitrakis, Carsten Horn, Pedro Beltrao, Emanuele Raineri, Mireia Garriga-Canut, & Luis Serrano, 2008, “Evolvability and Hierarchy in Rewired Bacterial Gene Networks”, *Nature*, 452(7189): 840–846. doi:10.1038/nature06847

[^issad-2015]: Issad,Tarik& Christophe Malaterre, 2015, “Are Dynamic Mechanistic Explanations Still Mechanistic?”, in Braillard & Malaterre 2015: 265–292. doi:10.1007/978-94-017-9822-8_12

[^jacob-1977]: Jacob, François, 1977, “Evolution and Tinkering”, *Science*, 196(4295): 1161–1166. doi:10.1126/science.860134

[^jaeger-2012]: Jaeger, Johannes & Anton Crombach, 2012, “Life’s Attractors: Understanding Developmental Systems Through Reverse Engineering and *in Silico* Evolution”, in Soyer 2012: 93–119. doi:10.1007/978-1-4614-3567-9_5

[^jaeger-2013]: Jaeger, Johannes & Nick Monk, 2013, “Keeping the Gene it Its Place”, in *The Intuitive Way of Knowing. A Tribute to Brian Goodwin*, David Lambert & Chris Chetland (eds.), Glasgow: Floris Books, pp. 153–189.

[^joaquim-2019]: Joaquim, Leyla Mariane, & Charbel N. El-Hani, 2019, “From Physics to Biology: Physicists in the Search for Systemic Biological Explanations”, *European Journal for Philosophy of Science*, 9(2): 1–32.

[^jones-2014]: Jones, Nicholaos, 2014, “Bowtie Structures, Pathway Diagrams, and Topological Explanation”, *Erkenntnis*, 79(5): 1135–1155. doi:10.1007/s10670-014-9598-9

[^jones-2018]: –––, 2018, “Strategies of Explanatory Abstraction in Molecular Systems Biology”, *Philosophy of Science*, 85: 955–968.

[^jones-2012]: Jones, Nicholaos & Olaf Wolkenhauer, 2012, “Diagrams as Locality Aids for Explanation and Model Construction in Cell Biology”, *Biology & Philosophy*, 27(5): 705–721. doi:10.1007/s10539-012-9311-9

[^karr-2012]: Karr, Jonathan R., Jayodita C. Sanghvi, Derek N Macklin, Miriam V. Gutschow, Jared M. Jacobs, Benjamin Bolival Jr., Nacyra Assad-Garcia, John I. Glass, & Markus W. Covert, 2012, “A Whole-Cell Computational Model Predicts Phenotype from Genotype”, *Cell*, 150(2): 389–401. doi:10.1016/j.cell.2012.05.044

[^kastenhofer-2007]: Kastenhofer, Karen, 2007, “Converging Epistemic Cultures? A Discussion Drawing on Empirical Findings”, *Innovation: The European Journal of Social Science Research*, 20(4): 359–373. doi:10.1080/13511610701767908

[^kastenhofer-2013a]: –––, 2013a, “Synthetic Biology as Understanding, Control, Construction and Creation? Techno-Epistemic and Socio-Political Implications of Different Stances in Talking and Doing Technoscience”, *Futures*, 48: 13–22. doi:10.1016/j.futures.2013.02.001

[^kastenhofer-2013b]: –––, 2013b, “Two Sides of the Same Coin? The (Techno)Epistemic Cultures of Systems and Synthetic Biology”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(2): 130–140. doi:10.1016/j.shpsc.2013.03.008

[^kauffman-2015]: Kauffman, Stuart, 2015, “What is Life?”, *Israel Journal of Chemistry*, 55(8): 875–879. doi:10.1002/ijch.201500003

[^keasling-2010]: Keasling, Jay D., 2010, “Manufacturing Molecules Through Metabolic Engineering”, *Science*, 330(6009): 1355–1358. doi:10.1126/science.1193990

[^keller-2005]: Keller, Evelyn Fox, 2005, “Revisiting ‘Scale-free’ Networks”, *BioEssays*, 27(1): 1060–1068. doi:10.1002/bies.20294

[^khalil-2010]: Khalil, Ahmad S. & James J. Collins, 2010, “Synthetic Biology: Applications Come of Age”, *Nature Reviews Genetics*, 11(5): 367–379. doi:10.1038/nrg2775

[^kim-2011]: Kim, Tae-Hwan, Junil Kim, Pat Heslop-Harrison, & Kwang-Hyun Cho, 2011, “Evolutionary Design Principles and Functional Characteristics Based on Kingdom-Specific Network Motifs”, *Bioinformatics*, 27(2): 245–251. doi:10.1093/bioinformatics/btq633

[^kitano-2001]: Kitano, Hiroaki, 2001 (ed.), *Foundations of Systems Biology*, Cambridge, MA: MIT press.

[^kitano-2002a]: –––, 2002a, “Computational Systems Biology”, *Nature*, 420(6912): 206–210. doi:10.1038/nature01254

[^kitano-2002b]: –––, 2002b, “Systems Biology: A Brief Overview”, *Science*, 295(5560): 1662–1664. doi:10.1126/science.1069492

[^kitano-2004]: –––, 2004, “Biological Robustness”, *Nature Reviews Genetics*, 5(11): 826–837. doi:10.1038/nrg1471

[^kitano-2006]: Kitano, Hiroaki & Kanae Oda, 2006, “Robustness Trade-offs and Host-Microbial Symbiosis in the Immune System”, *Molecular Systems Biology*, 2: 2006.0022. doi:10.1038/msb4100039

[^knuuttila-2013a]: Knuuttila, Tarja & Andrea Loettgers, 2013a, “Basic Science Through Engineering? Synthetic Modeling and the Idea of Biology-inspired Engineering”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(2): 158–169. doi:10.1016/j.shpsc.2013.03.011

[^knuuttila-2013b]: –––, 2013b, “Synthetic Modeling and Mechanistic Account: Material Recombination and Beyond”, *Philosophy of Science*, 80(5): 874–885. doi:10.1086/673965

[^knuuttila-2014]: –––, 2014, “Varieties of Noise: Analogical Reasoning in Synthetic Biology”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 48: 76–88. doi:10.1016/j.shpsa.2014.05.006

[^knuuttila-2021]: Knuuttila, Tarja, and Rami Koskinen, 2021, “Synthetic Fictions: Turning Imagined Biological Systems into Concrete Ones”, *Synthese*, 198 (9): 8233–8250.

[^kohl-2009]: Kohl, Peter & Denis Noble, 2009, “Systems Biology and the Virtual Physiological Human”, *Molecular Systems Biology*, 5: 292. doi:10.1038/msb.2009.51

[^kogge-2013]: Kogge, Werner & Michael Richter, 2013, “Synthetic Biology and Its Alternatives. Descartes, Kant and the Idea of Engineering Biological Machines”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(2): 181–189. doi:10.1016/j.shpsc.2013.03.013

[^kolodkin-2011]: Kolodkin, Alexey N. & Hans V. Westerhoff, 2011, “Parsimony for Systems Biology: Shaving Occam’s Razor Away”, *European Communications in Mathematical and Theoretical Biology*, 14: 149–152.

[^kolodkin-2011-2]: Kolodkin, Alexey, Fred C. Boogerd, Nick Plant, Frank J. Bruggeman, Valeri Goncharuk, Jeantine Lunshof, Rafael Moreno-Sanchez, Nilgun Yilmaz, Barbara M. Bakker, Jacky L. Snoep, Rudi Balling, & Hans V. Westerhoff, 2011, “Emergence of the Silicon Human and Network Targeting Drugs”, *European Journal of Pharmaceutical Sciences*, 46(4): 190–197. doi:10.1016/j.ejps.2011.06.006

[^kolodkin-2012]: Kolodkin, Alexey, Evangelos Simeonidis, Rudi Balling, & Hans V. Westerhoff, 2012, “Understanding Complexity in Neurodegenerative Diseases: *in Silico* Reconstruction of Emergence”, *Frontiers in Physiology*, 3: 291. doi:10.3389/fphys.2012.00291

[^koonin-2011]: Koonin, Eugene V., 2011, “Are There Laws of Genome Evolution?”, *PLoS Computational Biology*, 7: e1002173. doi:10.1371/journal.pcbi.1002173

[^koonin-2010]: Koonin, Eugene V. & Yuri I. Wolf, 2010, “Constraints and Plasticity in Genome and Molecular-Phenome Evolution”, *Nature Reviews Genetics*, 11(7): 487–498. doi:10.1038/nrg2810

[^koskinen-2017]: Koskinen, Rami, 2017, “Synthetic Biology and the Search for Alternative Genetic Systems: Taking How-Possibly Models Seriously,” *European Journal for Philosophy of Science*, 7(3): 493–506. doi:10.1007/s13194-017-0176-2

[^koskinen-2019]: Koskinen, Rami, 2019, “Multiple Realizability as a Design Heuristic in Biological Engineering”, *European Journal for Philosophy of Science*, 9: 15.

[^kostić-2020]: Kostić, Daniel, 2020, “General Theory of Topological Explanations and Explanatory Asymmetry,” *Philosophical Transactions of the Royal Society B*, 375(1796): 20190321.

[^kostić-2020-2]: Kostić, Daniel, Claus C. Hilgetag, and Marc Tittgemeyer, 2020, “Unifying the Essential Concepts of Biological Networks: Biological Insights and Philosophical Foundations,” *Philosophical Transactions of the Royal Society B*, 375(1796): 20190314. doi:10.1098/rstb.2019.0314

[^krohs-2009]: Krohs, Ulrich, 2009, “The Cost of Modularity”, in *Functions in Biological and Artificial Worlds: Comparative Philosophical Perspectives*, Ulrich Krohs & Peter Kroes (eds.), Cambridge, MA: MIT Press, 259–276. doi:10.7551/mitpress/9780262113212.003.0015

[^krohs-2012]: –––, 2012, “Convenience Experimentation”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 43(1): 52–57. doi:10.1016/j.shpsc.2011.10.005

[^krohs-2007]: Krohs, Ulrich & Werner Callebaut, 2007, “Data Without Models Merging with Models Without Data”, in Boogerd, Bruggeman, Hofmeyr, & Westerhoff 2007: 181–212.

[^laland-2009]: Laland, Kevin N., John Odling-Smee, Marcus W. Feldman, & Jeremy Kendel, 2009, “Conceptual Barriers to Progress Within Evolutionary Biology”, *Foundations of Science*, 14(3): 195–216. doi:10.1007/s10699-008-9153-8

[^leonelli-2012]: Leonelli, Sabina, 2012, “Introduction: Making Sense of Data-driven Research in the Biological and Biomedical Sciences”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 43(1): 1–3. doi:10.1016/j.shpsc.2011.10.001

[^leonelli-2013]: –––, 2013, “Why the Current Insistence on Open Access to Scientific Data? Big Data, Knowledge Production and the Political Economy of Contemporary Biology”, *Bulletin of Science, Technology and Society*, 33(1–2): 6–11. doi:10.1177/0270467613496768

[^leonelli-2014]: –––, 2014, “What Difference Does Quantity Make? On the Epistemology of Big Data in Biology”, *Big Data & Society*, 1: 2053951714534395. doi:10.1177/2053951714534395

[^leonelli-2016]: –––, 2016, *Data-Centric Biology: A Philosophical Study*, Chicago: University of Chicago Press.

[^letelier-2011]: Letelier, Juan-Carlos, María Luz Cárdenas, & Athel Cornish-Bowden, 2011, “From L’Homme Machine to Metabolic Closure: Steps Towards Understanding Life”, *Journal of Theoretical Biology*, 286: 100–113. doi:10.1016/j.jtbi.2011.06.033

[^levy-2013]: Levy, Arnon & William Bechtel, 2013, “Abstraction and the Organization of Mechanisms”, *Philosophy of Science*, 80(2): 241–261. doi:10.1086/670300

[^lewens-2013]: Lewens, Tim, 2013, “From *Bricolage* to BioBricks™: Synthetic Biology and Rational Design”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(4, part B): 641–648. doi:10.1016/j.shpsc.2013.05.011

[^lobkovsky-2012]: Lobkovsky, Alexander E. & Eugene V. Koonin, 2012, “Replaying the Tape of Life: Quantification of the Predictability of Evolution”, *Frontiers in Genetics*, 3: 246. doi:10.3389/fgene.2012.00246

[^loscalzo-2011]: Loscalzo, Joseph & Albert-László Barabási, 2011, “Systems Biology and the Future of Medicine”, *Wiley Interdisciplinary Reviews: Systems Biology and Medicine*, 3(6): 619–627. doi:10.1002/wsbm.144

[^love-2015]: Love, Alan C. & Marco J. Nathan, 2015, “The Idealization of Causation in Mechanistic Explanation”, *Philosophy of Science*, 82(5): 761–774. doi:10.1086/683263

[^luisi-1998]: Luisi, Pier Luigi, 1998, “About Various Definitions of Life”, *Origins of Life and Evolution of the Biosphere*, 28: 613–622

[^luisi-2006]: –––, 2006, *The Emergence of Life. From Chemical Origins to Synthetic Biology*, Cambridge: Cambridge University Press.

[^lynch-2007]: Lynch, Michael, 2007, “The Frailty of Adaptive Hypotheses for the Origins of Organismal Complexity”, *Proceedings of the National Academy of Sciences*, 104(S1): 8597–8604. doi:10.1073/pnas.0702207104

[^machamer-2000]: Machamer, Peter, Lindley Darden, & Carl F. Craver, 2000, “Thinking About Mechanisms”, *Philosophy of Science*, 67(1): 1–25. doi:10.1086/392759

[^macleod-2018]: MacLeod, Miles, 2018, “What Makes Interdisciplinarity Difficult? Some Consequences of Domain Specificity in Interdisciplinary Practice”, *Synthese*, 195(2): 697–720.

[^macleod-2013a]: MacLeod, Miles & Nancy J. Nersessian, 2013a, “Building Simulations from the Ground Up: Modelling and Theory in Systems Biology”, *Philosophy of Science*, 80(4): 533–566. doi:10.1086/673209

[^macleod-2013b]: –––, 2013b, “Coupling Simulation and Experiment: the Bimodal Strategy in Integrative Systems Biology”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(4, part A): 572–584. doi:10.1016/j.shpsc.2013.07.001

[^macleod-2015]: –––, 2015, “Modeling Systems-level Dynamics: Understanding Without Mechanistic Explanation in Integrative Systems Biology”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 49: 1–11. doi:10.1016/j.shpsc.2014.10.004

[^mcleod-2017]: McLeod, Carmen, & Brigitte Nerlich, 2017, “Synthetic Biology, Metaphors and Responsibility”, *Life Sciences, Society and Policy*, 13: 13.

[^maher-2008]: Maher, Brendan, 2008, “Personal Genomes: The Case of the Missing Heritability”, *Nature*, 456(7218): 18–21. doi:10.1038/456018a

[^mangan-2003]: Mangan, Shmoolik, A. Zaslaver, & Uri Alon, 2003, “The Coherent Feedforward Loop Serves as a Sign-Sensitive Delay Element in Transcription Networks”, *Journal of Molecular Biology*, 334(2): 197–204. doi:10.1016/j.jmb.2003.09.049

[^matthiessen-2015]: Matthiessen, D., 2015, “Mechanistic Explanation in Systems Biology: Cellular Networks”, *The British Journal for the Philosophy of Science*, 68(1): 1–25. doi:10.1093/bjps/axv011

[^maturana-1972]: Maturana, Humberto R. & Francisco J. Varela, 1972/1980, *Autopoiesis and Cognition: The Realization of the Living*, Dordrecht: D. Reidel Publishing Company.

[^mazzocchi-2015]: Mazzocchi, Fulvio, 2015, “Could Big Data be the End of Theory in Science?”, *EMBO Reports*, 16(10): 1250–1255. doi:10.15252/embr.201541001.

[^mcpherson-2016]: McPherson, Ruth & Anne Tybjaerg-Hansen, 2016, “Genetics of Coronary Artery Disease”, *Circulation Research*, 118(4): 564–578. doi:10.1161/CIRCRESAHA.115.306566

[^mesarović-1968]: Mesarović, Mihajlo D., 1968, “Systems Theory and Biology—View of a Theoretician”, in *Systems Theory and Biology. Proceedings of the III Systems Symposium at Case Institute of Technology*, M.D. Mesarović (ed.), New York, NY: Springer, pp. 59–87. doi:10.1007/978-3-642-88343-9_3

[^mesarović-2004]: Mesarović, M., S.N. Sreenath, & J.D. Keene, 2004, “Search for Organizing Principles: Understanding in Systems Biology”, *Systems Biology*, 1: 19–27.

[^mekios-2015]: Mekios, Constantinos, 2015, “Explanation in Systems Biology: Is it All About Mechanisms?”, in Braillard & Malaterre 2015: 47–72. doi:10.1007/978-94-017-9822-8_3

[^mekios-2016]: –––, 2016, “Organizing Principles as Tools for Bridging the Gap Between System Theory and Biological Experimentation”, *History and Philosophy of the Life Sciences*, 38(1): 65–89. doi:10.1007/s40656-016-0095-0

[^miller-1953]: Miller, Stanley L., 1953, “Production of Amino Acids Under Possible Primitive Earth Conditions”, *Science*, 117(3046): 528–529. doi:10.1126/science.117.3046.528

[^morange-2009]: Morange, Michel, 2009, “A Critical Perspective on Synthetic Biology”, *HYLE: International Journal for Philosophy of Chemistry*, 15: 21–30. [[Morange 2009 available online](http://www.hyle.org/journal/issues/15-1/morange.htm)]

[^moreno-2015]: Moreno, Alvaro & Matteo Mossio, 2015, *Biological Autonomy: A Philosophical and Theoretical Enquiry*, Dordrecht: Springer International Publishing. doi:10.1007/978-94-017-9837-2

[^moreno-2020]: Moreno, Alvaro & Javier Suárez, 2020, “Plurality of Explanatory Strategies in Biology: Mechanisms and Networks”, in Gonzales (ed.) 2020: 141–165.

[^mossio-2009]: Mossio, Matteo, Cristian Saborido, and Alvaro Moreno, 2009, “An Organizational Account of Biological Functions”, *The British Journal for the Philosophy of Science*, 60: 813–841.

[^munsky-2009]: Munsky, Brian, Brooke Trinh, & Mustafa Khammash, 2009, “Listening to the Noise: Random Fluctuations Reveal Gene Network Parameters”, *Molecular Systems Biology*, 5: 318. doi:10.1038/msb.2009.75

[^nersessian-2017]: Nersessian, Nancy J., 2017, “Systems Biology Modeling Practices: Reflections of a Philosopher-Ethnographer”, in Green 2017: 215–226. doi:10.1007/978-3-319-47000-9_20

[^nicholson-2019]: Nicholson, Daniel J., 2019, “Is the Cell Really a Machine?”, *Journal of Theoretical Biology*, 477: 108–126.

[^noble-2008]: Noble, Denis, 2008, “Claude Bernard, the First Systems Biologist, and the Future of Physiology”, *Experimental Physiology*, 93(1): 16–26. doi:10.1113/expphysiol.2007.038695

[^noble-2012]: –––, 2012, “A Theory of Biological Relativity: No Privileged Level of Causation”, *Interface Focus*, 2(1): 55–64. doi:10.1098/rsfs.2011.0067

[^nordmann-2015]: Nordmann, Alfred, 2015, “Synthetic Biology at the Limits of Science”, in *Synthetic Biology*, Bernd Giese, Arnim von Gleich, Christian Pade, & Henning Wigger (eds.), Cham: Springer International Publishing, pp. 31–58. doi:10.1007/978-3-319-02783-8_2

[^o’malley-2009]: O’Malley, Maureen A., 2009, “Making Knowledge in Synthetic Biology: Design Meets Kludge”, *Biological Theory*, 4(4): 378–389. doi:10.1162/BIOT_a_00006

[^o’malley-2011a]: –––, 2011a, “Constructive Personalized Medicine: the Potential Integration of Synthetic Biology and Personalized Medicine”, *Current Pharmacogenomics and Personalized Medicine*, 9(3): 177–183. doi:10.2174/187569211796957593

[^o’malley-2011b]: –––, 2011b, “Exploration, Iterativity and Kludging in Synthetic Biology”, *Comptes Rendus Chimie*, 14(4): 406–412. doi:10.1016/j.crci.2010.06.021

[^o’malley-2005]: O’Malley, Maureen A. & John Dupré, 2005, “Fundamental Issues in Systems Biology”, *BioEssays*, 27(12): 1270–1276. doi:10.1002/bies.20323

[^o’malley-2008]: O’Malley, Maureen A., Alexander Powell, Jonathan F. Davies, & Jane Calvert, 2008, “Knowledge-Making Distinctions in Synthetic Biology”, *BioEssays*, 30(1): 57–65. doi:10.1002/bies.20664

[^o’malley-2012]: O’Malley, Maureen A. & Orkun S. Soyer, 2012, “The Roles of Integration in Molecular Systems Biology”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 43(1): 58–68. doi:10.1016/j.shpsc.2011.10.006

[^o’malley-2015]: O’Malley, Maureen A., Orkun S. Soyer, & Mark L. Siegal, 2015, “A Philosophical Perspective on Evolutionary Systems Biology”, *Biological Theory*, 10(1): 6–17. doi:10.1007/s13752-015-0202-6

[^o’malley-2019]: O’Malley, Maureen A., Michelle M. Leger, Jeremy G. Wideman, and Iñaki Ruiz-Trillo, 2019, “Concepts of the Last Eukaryotic Common Ancestor”, *Nature Ecology & Evolution*, 3(3): 338–344.

[^orzack-2010]: Orzack, Stephen H. & Patrick Forber, 2010, “Adaptationism”, *The Stanford Encyclopedia of Philosophy* (Fall 2010), Edward N. Zalta (ed.), URL = <[https://plato.stanford.edu/archives/fall2010/entries/adaptationism/](https://plato.stanford.edu/archives/fall2010/entries/adaptationism/)>

[^palmer-2013]: Palmer, Adam C. & Roy Kishony, 2013, “Understanding, Predicting and Manipulating the Genotypic Evolution of Antibiotic Resistance”, *Nature Reviews Genetics*, 14(4): 243–248. doi:10.1038/nrg3351

[^papp-2011]: Papp, Balázs, Richard A. Notebaart, & Csaba Pall, 2011, “Systems-Biology Approaches for Predicting Genomic Evolution”, *Nature Reviews Genetics*, 12(9): 591–602. doi:10.1038/nrg3033

[^peter-2015]: Peter, Isabelle S. & Eric H. Davidson, 2015, *Genomic Control Process: Development and Evolution*, London, UK: Academic Press/Elsevier.

[^pigliucci-2007]: Pigliucci, Massimo, 2007, “Do We Need An Extended Evolutionary Synthesis?”, *Evolution*, 61(12): 2743–2749. doi:10.1111/j.1558-5646.2007.00246.x

[^pio-lopez-2021]: Pio-Lopez, Léo, 2021, “The Rise of the Biocyborg: Synthetic Biology, Artificial Chimerism and Human Anhancement”, *New Genetics and Society*, 40(4): 599–619.

[^plutynski-2018]: Plutynski, Anya, 2018, “What and How Do Cancer Systems Biologists Explain?”, *Philosophy of Science*, 85: 942–954. doi: 10.1086/699716

[^plutynski-2021]: –––, 2021, “How is Cancer Complex?”, *European Journal for Philosophy of Science*, 11(55): 1–30. doi:10.1007/s13194-021-00371-8

[^pradeu-2016]: Pradeu, Thomas, 2016, “Thirty Years of *Biology & Philosophy*: Philosophy of Which Biology?”, *Biology & Philosophy*, 32(2): 149–167. doi:10.1007/s10539-016-9558-7

[^prainsack-2017]: Prainsack, Barbara, 2017, *Personalized Medicine: Empowered Patients in the 21st Century?* New York: New York University Press.

[^preston-2008]: Preston, Christopher J., 2008, “Synthetic Biology: Drawing a Line in Darwin’s Sand”, *Environmental Values*, 17(1): 23–39. doi:10.3197/096327108X271932

[^preston-2013]: Preston, Beth, 2013, “Synthetic Biology as Red Herring”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(4, part B): 649–659. doi:10.1016/j.shpsc.2013.05.012

[^prill-2010]: Prill, Robert J., Daniel Marbach, Julio Saez-Rodriguez, Peter K. Sorger, Leonidas G. Alexopoulos, Xiaowei Xue, Neil D. Clarke, Gregoire Altan-Bonnet, & Gustavo Stolovitzky, 2010, “Towards a Rigorous Assessment of Systems Biology Models: the DREAM3 Challenges”, *PLoS One*, 5(3): e9202. doi:10.1371/journal.pone.0009202

[^rashevsky-1961]: Rashevsky, Nicolas, 1961, *Mathematical Principles in Biology and their Applications* (American lecture series, 414), Springfield, IL: C.C. Thomas.

[^rasmussen-2008]: Rasmussen, Steen, Mark A. Bedau, Liachai Chen, David Deamer, David C. Krakauer, Norman H. Packard, & Peter F. Stadler, 2008, *Protocells: Bridging Nonliving and Living Matter*, Cambridge, MA: MIT Press. doi:10.7551/mitpress/9780262182683.001.0001

[^ratti-2015]: Ratti, Emanuele, 2015, “Big Data Biology: Between Eliminative Inferences and Exploratory Experiments”, *Philosophy of Science*, 82(2): 198–218.

[^ravasz-2002]: Ravasz, E., A.L. Somera, D.A. Mongru, Z.N. Oltvai, & Albert-László Barabási, 2002, “Hierarchical Organization of Modularity in Metabolic Networks”, *Science*, 297(5586): 1551–1555. doi:10.1126/science.1073374

[^reydon-2012]: Reydon, Thomas A.C., Kostas Kampourakis, & George P. Patrinos, 2012, “Genetics, Genomics and Society: the Responsibilities of Scientists for Science Communication”, *Personalized Medicine*, 9(6): 633–643. doi:10.2217/pme.12.69

[^richardson-2007]: Richardson, Robert C. & Achim Stephan, 2007, “Mechanism and Mechanical Explanation in Systems Biology”, in Boogerd, Bruggeman, Hofmeyr, & Westerhoff 2007: 123–144.

[^rosen-1991]: Rosen, Robert, 1991, *Life Itself: A Comprehensive Inquiry into the Nature, Origin, and Fabrication of Life*, New York, NY: Columbia University Press.

[^royal-2012]: Royal Society, 2012, “Science as an Open enterprise”, *The Royal Society Science Policy Centre report 02/12*, [available online](https://royalsociety.org/~/media/policy/projects/sape/2012-06-20-saoe.pdf).

[^rowbottom-2011]: Rowbottom, Darrell P., 2011, “Approximations, Idealizations and ‘Experiments’ at the Physics-Biology Interface”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 42(2): 145–154. doi:10.1016/j.shpsc.2010.11.021

[^ruiz-mirazo-2010]: Ruiz-Mirazo, Kepa, Juli Peretó, & Alavaro Moreno, 2010, “Defining Life or Bringing Biology to Life”, *Origins of Life and Evolution of Biospheres*, 40(2): 203–213. doi:10.1007/s11084-010-9201-6

[^savageau-1976]: Savageau, Michael A., 1976, *Biochemical Systems Analysis: A Study of Function and Design in Molecular Biology*, Reading, MA: Addison-Wesley.

[^schyfter-2013]: Schyfter, Pablo, 2013, “How a ‘Drive to Make’ Shapes Synthetic Biology”, *Studies in History and Philosophy of Biological and Biomedical Sciences*, 44(4, part B): 632–640. doi:10.1016/j.shpsc.2013.05.010

[^serban-2020]: Serban, Maria, 2020, “Exploring Modularity in Biological Networks”, *Philosophical Transactions of the Royal Society B*, 375(1796): 20190316.

[^serban-2020-2]: Serban, Maria, & Sara Green, 2020, “Biological Robustness: Design, Organization, and Mechanisms”, in Serban, Holt, & Holm (eds.) 2020: 141–164.

[^shen-orr-2002]: Shen-Orr, Shai S., Ron Milo, Shmoolik Mangan, & Uri Alon, 2002, “Network Motifs in the Transcriptional Regulation Network of *Escherichia coli*”, *Nature Genetics*, 31(1): 64–68. doi:10.1038/ng881

[^shinar-2011]: Shinar, Guy & Martin Feinberg, 2011, “Design Principles for Robust Biochemical Reaction Networks: What Works, What Cannot Work, and What Might Almost Work”, *Mathematical Biosciences*, 231: 39–48. doi:10.1016/j.mbs.2011.02.012

[^simons-2021]: Simons, Massimiliano, 2021, “Synthetic Biology as a Technoscience: The Case of Minimal Genomes and Essential Genes”, *Studies in History and Philosophy of Science Part A*, 85: 127–136. doi:10.1016/j.shpsa.2020.09.012

[^solé-2020]: Solé, Ricard, and Sergi Valverde, 2020, “Evolving Complexity: How Tinkering Shapes Cells, Software and Ecological Networks”, *Philosophical Transactions of the Royal Society B*, 375(1796): 20190325.

[^soto-2011]: Soto, Ana M. & Carlos Sonnenschein, 2011, “The Tissue Organization Field Theory of Cancer: a Testable Replacement for the Somatic Mutation Theory”, *BioEssays*, 33(5): 322–340. doi:10.1002/bies.201100025

[^soto-2008]: Soto, A.M., Carlos Sonnenschein, & Paul-Antoine Miquel, 2008, “On Physicalism and Downward Causation in Developmental and Cancer Biology”, *Acta Biotheoretica*, 56(4): 257–274. doi:10.1007/s10441-008-9052-y

[^soyer-2012]: Soyer, Orkun S., 2012 (ed.), *Evolutionary Systems Biology*, London: Springer. doi:10.1007/978-1-4614-3567-9

[^soyer-2013]: Soyer, Orkun & Maureen A. O’Malley, 2013, “Evolutionary Systems Biology: What it is and Why it Matters”, *BioEssays*, 35(8): 696–705. doi:10.1002/bies.201300029

[^steinacher-2012]: Steinacher, Arno & Orkun S. Soyer, 2012, “Evolutionary Principles. Underlying Structure and Response Dynamics of Cellular Networks”, in Soyer 2012: 225–247. doi:10.1007/978-1-4614-3567-9_11

[^steinle-1997]: Steinle, Friedrich, 1997, “Entering New Fields: Exploratory Uses of Experimentation”, *Philosophy of Science*, S65–S74. doi:10.1086/392587

[^stelling-2004]: Stelling, Jörg, Uwe Sauer, Zoltan Szallasi, Francis J. Doyle III, & John Doyle, 2004, “Robustness of Cellular Functions”, *Cell*, 118(6): 675–685. doi:10.1016/j.cell.2004.09.008

[^stricker-2008]: Stricker, Jesse, Scott Cookson, Matthew R. Bennet, William H. Mather, Levi S. Tsimring, & Jeff Hasty, 2008, “A Fast, Robust and Tunable Synthetic Gene Oscillator”, *Nature*, 456(7221): 516–519. doi:10.1038/nature07389

[^suárez-2019]: Suárez, Javier, and Roger Deulofeu, 2019, “Equilibrium Explanation as Structural Non-Mechanistic Explanations,” *Teorema: Revista internacional de filosofía*, 38(3): 95–120.

[^sung-2016]: Sung, Bong Hyun, Donghui Choe, Sun Chang Kim & Byung-Kwan Cho, 2016, “Construction of a Minimal Genome as a Chassis for Synthetic Biology”, *Essays in Biochemistry*, 60(4): 337–346. doi:10.1042/EBC20160024

[^szostak-2001]: Szostak, Jack W., David P. Bartel, & Pier Luigi Luisi, 2001, “Synthesizing Life”, *Nature*, 409(6818): 387–390. doi:10.1038/35053176

[^tutton-2014]: Tutton, Richard, 2014, *Genomics and the Reimagining of Personalized Medicine*, Farnham, UK: Ashgate Publishing.

[^tyson-2010]: Tyson, John J. & Béla Novák, 2010, “Functional Motifs in Biochemical Reaction Networks”, *Annual Review of Physical Chemistry*, 61: 219–240. doi:10.1146/annurev.physchem.012809.103457

[^tyson-2003]: Tyson, John J., Katherine C. Chen, & Béla Novak, 2003, “Sniffers, Buzzers, Toggles and Blinkers: Dynamics of Regulatory and Signaling Pathways in the Cell”, *Current Opinion in Cell Biology*, 15(2): 221–231. doi:10.1016/S0955-0674(03)00017-6

[^eck-2021]: van Eck, Dingmar, and Cory Wright, 2021, “Mechanist Idealisation in Systems Biology”, *Synthese*, 199(1): 1555–1575.

[^regenmortel-2004]: van Regenmortel, Marc H.V., 2004, “Reductionism and Complexity in Molecular Biology”, *EMBO Reports*, 5(11): 1016–1020. doi:10.1038/sj.embor.7400284

[^vermeulen-2010]: Vermeulen, Niki, 2010, *Supersizing Science: On Building Large-scale Research Projects in Biology*, Boca Raton, Fl: Universal-Publishers.

[^vermeulen-2011]: –––, 2011, “Growing a Cell *in Silico*: on How the Creation of a Bio-object Transforms the Organisation of Science”, in *Bio-Objects. Life in the 21st Century*, Niki Vermeulen, Sakari Tamminen, & Andrew Webster (eds.), Aldershot: Ashgate, pp. 171–186.

[^vickers-2022]: Vickers, Claudia E. & Peter S. Freemont, 2022, “Pandemic Preparedness: Synthetic Biology and Publicly Funded Biofoundries Can Rapidly Accelerate Response Time”, *Nature Communications*, 13: 453. doi: 10.1038/s41467-022-28103-3

[^vogt-2014]: Vogt, Henrik, Elling Ulvestad, Thor Eirik Eriksen, & Linn Getz, 2014, “Getting Personal: Can Systems Medicine Integrate Scientific and Humanistic Conceptions of the Patient?”, *Journal of Evaluation in Clinical Practice*, 20(6): 942–952. doi:10.1111/jep.12251.

[^vogt-2016]: Vogt, Henrik, Bjørn Hofmann, & Linn Getz, 2016, “The New Holism: P4 Systems Medicine and the Medicalization of Health and Life Itself”, *Medicine, Health Care and Philosophy*, 19(2): 307–323. doi:10.1007/s11019-016-9683-8

[^vogt-2019]: Vogt, Henrik, Sara Green, Claus Thorn Ekstrøm, & John Brodersen, 2019, “How Precision Medicine and Screening with Big Data Could Increase Overdiagnosis”, *BMJ*, 366: l5270.

[^voigt-2020]: Voigt, Christopher A., 2020, “Synthetic Biology 2020–2030: Six Commercially-Available Products that are Changing our World”, *Nature Communications*, 11(1): 1-6.

[^voit-2003]: Voit, Eberhard O., 2003, “Design Principles and Operating Principles: The Yin and Yang of Optimal Functioning”, *Mathematical Biosciences*, 182: 81–92. doi:10.1016/S0025-5564(02)00162-1

[^voit-2008]: Voit, Eberhard O. & Kenneth L. Brigham, 2008, “The Role of Systems Biology in Predictive Health and Personalized Medicine”, *The Open Pathology Journal*, 2: 68–70. doi:10.2174/1874375700802010068

[^neumann-1966]: von Neumann, John, 1966, *The Theory of Self-Reproducing Automata*, Arthur W. Burks (ed.), Urbana, IL: University of Illinois Press.

[^wagner-2012]: Wagner, Andreas, 2012, “Metabolic Networks and Their Evolution”, in Soyer 2012: 29–52. doi:10.1007/978-1-4614-3567-9_2

[^wagner-2014]: –––, 2014, *Arrival of the Fittest: Solving Evolution’s Greatest Puzzle*, New York, NY: Penguin.

[^watts-1998]: Watts, Duncan J. and Steven H. Strogatz, 1998, “Collective Dynamics of ‘Small Worlds’ Networks”, *Nature*, 393(6684): 440–442. doi:10.1038/30918

[^weinreich-2006]: Weinreich, Daniel M., Nigel F. Delaney, Mark A. DePristo, and Daniel L. Hartl, 2006, “Darwinian Evolution Can Follow Only Very Few Mutational Paths to Fitter Proteins”, *Science*, 312(5770): 111–114. doi:10.1126/science.1123539

[^wiener-1948]: Wiener, Norbert, 1948, *Cybernetics: Or Control and Communication in the Animal and the Machine*, Paris: MIT Press.

[^wolkenhauer-2013]: Wolkenhauer, Olaf and Sara Green, 2013, “The Search for Organizing Principles as a Cure Against Reductionism in Systems Medicine”, *FEBS Journal*, 280(23): 5938–48. doi:10.1111/febs.12311

[^wolkenhauer-2007]: Wolkenhauer, Olaf and Jan-Hendrik S. Hofmeyr, 2007, “An Abstract Cell Model that Describes the Self-Organization of Cell Function in Living Systems”, *Journal of Theoretical Biology*, 246(3): 461–476. doi:10.1016/j.jtbi.2007.01.005

[^wolkenhauer-2005]: Wolkenhauer, Olaf and Mihajlo Mesarović, 2005, “Feedback Dynamics and Cell Function: Why Systems Biology is Called Systems Biology”, *Molecular BioSystems*, 1: 14–16. doi:10.1039/b502088n

[^wouters-2007]: Wouters, Arno G., 2007, “Design Explanation: Determining the Constraints on What Can be Alive”, *Erkenntnis*, 67(1): 65–80. doi:10.1007/s10670-007-9045-2

[^zepik-2001]: Zepik, Helmut H., Eveline Blöchliger, and Pier Luigi Luisi, 2001, “A Chemical Model of Homeostasis”, *Angewandte Chemie*, 40(1): 199–202. doi:10.1002/1521-3773(20010105)40:1<199::AID-ANIE199>3.0.CO;2-H
