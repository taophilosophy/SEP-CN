# Ontology and Information Systems
**First published Sat Jan 3, 2026**

*Pease, Adam*

When two agents communicate they must have some significant body of shared understanding about the meaning of the symbols they use. Humans have attempted to codify some of those shared meanings in dictionaries. In the computer and information sciences we face the challenge of how to enable machines to share at least some of the catalog of the symbols humans use and what they mean. In dealing with machines one must rely on mathematics to state meaning rather than relying on the experience and intuitions of the communicating agents. Ontology (in information systems) is the field that attempts to create shared meanings of symbols. Different practitioners in the field may decide to create different lists of symbols with different definitions.

A motivation for the development of ontology as a discipline has been a common issue in software development, where the use of symbols in computer code by different programmers can change over time, causing unintended performance in a system. This issue motivated efforts to catalog, standardize and reuse concepts, recorded as a set of labels and definitions. Establishing an ontology helps to avoid concept drift (Magne 2017; Lu et al. 2019; Pancha 2016)[^magne-2017][^pancha-2016] and supports the interoperability of computer software systems.

## 1. Introduction

In information and computer science the study of ontology is about how to define or describe the things that *are* (including imagined or possible things) for the purpose of some process of computation on a computer. In philosophy, the field of ontology is often described as “the study of what there is” (see the entries on social ontology, logic ontology and natural language ontology). A philosophical ontology will thus purport to identify the fundamental constituents of reality, the categories they fall into, and the relations they stand in to one another. Ontology in computer and information science shares with philosophy that it includes a study of categories (see the entry on categories) but with a practical focus on recording an inventory of categories in a formal syntax and often with some formal semantics. Some individual information science ontologies are also concerned with a formal specification of the definitions of those categories. Ontology as a field in computer and information science is also reasonably characterized as the study of what there is, but not necessarily of what ultimately exists, rather of what is assumed to exist in some relevant domain for some computational purpose. A computer scientist is less concerned about the metaphysical status of categories – such as whether they actually exist or are just human constructs – than with their practical use in computation. In computer and information science, an ontology may also catalogue individuals and relationships, in addition to categories.

One popular description of an ontology in computer science is “a specification of a conceptualization” (Gruber 1993)[^gruber-1993]. But this requires an explanation of of what a specification is and what a conceptualization is. A conceptualization is a way to understand the structure of a particular concept by considering both its relationship to other concepts and the principles that may govern it. So a conceptualization includes a way to understand how a concept differentiates the objects falling under it (whether abstract or concrete), from other things. Historically, a way of understanding a concept would be expressible in a human language as an entry in a dictionary or encyclopedia. Concepts are often labeled using single words or phrases and since they are the meanings of those words and phrases, they are not part of the syntax. Different human languages use different symbols but can express the same concepts, although whether one can have truly exact translations is a subject of some debate (Levine & Lateef-Jan 2017)[^levine-2017]. Words are one method of *reference* (see the entry on reference). We hope that when we use a proper noun like “Mount Kilimanjaro” that the listener will have enough common information associated with the words that the desired information is communicated. But with more abstract concepts such as “object” or “beauty” this is more problematic. Once a concept is expressed in some way for communication then we can examine what it means to be a specification. If we do not rely on human intuition about the intended meaning of a word or words, or even on the process of human clarification dialogues, then we must have some other way of recording ideas or thoughts.

Since its adoption in the computer science community, the word ‘ontology’ has become broader in usage. Collections of words with natural language definitions have been labeled as an ontology, even though we could call them glossaries and not have to resort to adopting this new word for something that already has an older label. Other approaches to specifying an ontology include use of taxonomy languages (Dallwitz 1980)[^dallwitz-1980] or Unified Modeling Language (UML: Rumbaugh, Jacobson, & Booch 2004). Others have treated a graph of concept names and binary relationships to be sufficient for a specification, such as what is found in semantic networks (Woods 1975)[^woods-1975] or knowledge graphs (which might be stated in Resource Description Framework (RDF: see the link to RDF in Other Internet Resources below), or a graph database (Kaliyar 2015)[^kaliyar-2015]). Description logics (Baader, Calvanese, McGuinness, Nardi, & Patel-Schneider 2007) are a popular choice for specification of an ontology. At its most formal, a specification can be a set of formulas in an expressive mathematical logic such as first-order logic (Enderton 1972)[^enderton-1972], modal logic or higher-order logic (see the entries on modal logic and higher-order logic).

Two of the most important motivations for constructing an ontology are that (i) it can help to prevent concept drift and (ii) it supports the interoperability of systems. Regarding the first of these, a common issue in software development is that the use of strings of symbols in computer code by different programmers can change over time, causing unintended performance in a system. An ontology standardizes and reuses concepts, thereby preventing a concept expressed by a string within a given body of code at one time from drifting into use as another, different concept at a later time. Regarding interoperability, note first that the kind of ontology one creates will, at least in part, be driven by its intended uses. Broadly, there are three categories of use, ultimately leading to a computational implementation, which may all be present in some application: (1) communication among people, (2) communication among machines or between people and machines, and (3) computation.

In (1) the ontology is used to align the terminology and understanding of that terminology among developers of a computational system. There may be no exact transfer of the set of labels or definitions into any formal computational system. An ontology that exists to facilitate understanding among humans may rely on intuitions about concepts based on their names, as well as natural language definitions. Grounding the meaning of specialized terms in a glossary can help to eliminate some interpretations, for example, misunderstandings based on word polysemy.

In (2) the set of labels used in a computational system forms a standard that people and software systems adhere to. The people who develop the computational system agree on the set of symbols to be used and agree on some set of definitions which are at least partly given in natural language and require human intelligence to interpret.

In (3) there is a fully computational representation of a set of concepts, in which the intended meaning of a set of symbols is fully specified in a computational form, such as a computationally implemented mathematical logic. People may still have intuitions about concepts which are not fully captured in the logical language, but that would be considered a bug or omission to be rectified.

This classification of an ontology with respect to these three categories is a framework for understanding the usage of an ontology rather than a mutually exclusive and rigid set. One might for example have an ontology strictly implemented in a computational mathematical logic as a way for people to adjudicate disagreements about terminology, rather than to govern the behavior of a software system.

## 2. History

The conception of ontology adopted in information science has its roots in the history of philosophy and may be traced all the way back to the “Tree of Porphyry” (with reference to the 3rd-century Greek neoplatonist philosopher Porphyry of Tyre: Franklin 1986)[^franklin-1986]. The abstraction of a tree was used to show the relationships between concepts.

This abstraction would become a dominant way to depict ontological distinctions from the biological taxonomy of Linnaeus (1758) to the present day. Much writing about categories throughout the Middle Ages consists of commentary (see the entry on medieval categories) on Aristotle’s work. After the Middle Ages, efforts to catalog categories were more independent of Aristotle, and the advent of the scientific method led to interest in defining categories in the natural sciences, including in Linnaeus’ writings.

A less-well known effort of particular note, which predates Linnaeus, is John Wilkins’ monumental “An Essay Towards a Real Character and a Philosophical Language” of 1685 (Subbiondo 1992)[^subbiondo-1992]. It contains hundreds of pages of a single tree structure of concepts, each with a natural language definition. While much of the content, such as the categories for organisms, is only of historical interest, some innovations, such as a concept of ‘glove’ being viewed as a function that denotes clothing for a body part, point to modern uses of logical functions in ontological definitions. His work also is notable in that he presents the concepts not only in a taxonomy but also with a written and spoken language that uses the categories in a grammar in order to form a more perfect language (Eco 1995)[^eco-1995], free from ambiguity.

Before Frege and Peirce (see the entries on Frege and Peirce’s deductive logic) laid the foundations for modern mathematical logic, the concepts in an ontology were defined informally in natural language. Hence, until the development of modern computers, only humans were capable of working with an ontology.

Before the word ‘ontology’ was adopted in computer science there was a long history in Artificial Intelligence (AI) of using formal logic and logic-inspired systems such as Prolog (Clocksin & Mellish 2003)[^clocksin-2003] to define concepts. Collections of logical theories (Farquhar, Fikes, & Rice 1997) showed how many logical definitions of general concepts could be documented, but at that point the concepts were not integrated so that they could be combined and used together in a single consistent theory.

Another knowledge representation method used in some information science ontologies is that of Semantic Networks (Woods 1975; Lehmann 1992; see also the section “Representationalist Approaches” in the entry on computational linguistics)[^lehmann-1992][^woods-1975]. They are also called Knowledge Graphs and often implemented in graph databases (Robinson, Webber, & Eifrem 2015). They consist of a set of labeled nodes and arcs, arranged as a graph, that state relationships between entities. This approach was popular in AI in the 1970s and has again become popular in the 2020s.

Expert systems, prevalent in the 1970s and 1980s, were arguably the earliest systems that used a computational ontology, although they were not known by that label at that time. But if we consider a computational product that consists of a collection of symbols and some symbolic language that defines the concepts, such systems did include ontologies. Mycin (Buchanan & Shortliffe 1985)[^buchanan-1985], Prospector (Duda, Gaschnig, & Hart 1979) and many other expert systems were developed through the 1970s and 1980s.

Semantic networks and first-order logic were two of the earliest knowledge representation paradigms in Artificial Intelligence and also exemplars of the “neat” vs. “scruffy” debate (Crevier 1993; Poirier 2024; Gonçalves & Cozman 2021)[^crevier-1993][^gonçalves-2021][^poirier-2024] about whether knowledge representation required a formal mathematics. Some practitioners (“neats”) would advocate that a solid theoretical basis for reasoning is needed. Others (“scruffies”) argue that having a system that “just works” is enough, and that a system that accomplishes a task need not have a theoretical underpinning. This echoes a broader debate about the validity of *empiricism* (see the entry on logical empiricism). In the mid-1990s the value of a collection of named concepts as a resource, somewhat independent of its use, began to be recognized in computer science.

Another response to the difficulties in knowledge engineering for expert systems, which predated the use of “ontology” as a term in computer science, is the Cyc project (Lenat & Guha 1989)[^lenat-1989]. Cyc is a commercial endeavor conceived of as a repository of common-sense knowledge to support Artificial Intelligence applications. It is the largest effort to date to collect concepts and definitions in an expressive logic in a computational system. There was a recognition that an important area of study for ontology was the “upper ontology” (see section 3) – a set of concepts that are likely to be needed and held in common among many domains. Some of the first upper ontologies conceived with that description were the Suggested Upper Merged Ontology (SUMO: Niles & Pease 2001; Pease 2011)[^niles-2001][^pease-2011], the Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE: Gangemi, Guarino, Masolo, Oltramari, & Schneider 2002) and Basic Formal Ontology (BFO: Arp, Smith, & Spear 2015; Smith, Grenon, & Goldberg 2004). Many others followed (see the link to Upper Ontology in the Other Internet Resources section below). Ontology languages evolved in parallel with creation of new ontologies. Expert systems were implemented in Prolog (Clocksin & Mellish 2003)[^clocksin-2003] or expert system “shells” such as Clips (Riley, Culbert, Savely, & Lopez 1987) and OPS5 (Brownston, Farrell, Kant, & Martin 1985). Some ontologies are defined in languages that can be used in computation to answer questions or check their consistency. Theorem-proving languages for particular mathematical logics were developed with increasing expressiveness from first-order logic (Sutcliffe & Suttner 1998)[^sutcliffe-1998] to typed first-order logic (Sutcliffe, Schulz, Claessen, & Baumgartner 2012), modal (Raths & Otten 2012)[^raths-2012] and higher-order logic (Benzmüller, Rabe, & Sutcliffe 2008), and implemented in automated theorem-proving systems (Sutcliffe 2010)[^sutcliffe-2010]. Languages including Knowledge Interchange Format (KIF: Genesereth & Fikes 1992)[^genesereth-1992] and Description Logics such as the Ontology Web Language (OWL) family of languages (Bechhofer et al. 2004)[^bechhofer-2004] were developed explicitly to support ontologies.

## 3. Domain Ontology and Upper Ontology

An *upper ontology* is a collection of concepts that are not specific to any application domain. The determination of whether a concept belongs in an upper ontology or not is not an objective decision, except relative to other terms in the same ontology. Some upper ontologies aim to be minimal, containing only a small number of the most general concepts, and others include larger collections from the most general to the more specific. Many domain ontologies are created as extensions of upper ontologies. An upper ontology starts with a category of all things and then elaborates, adding categories (and sometimes, definitions) for physical and abstract things, relations and functions etc. But the boundary of where upper ontology becomes domain ontology is arbitrary. A domain ontology would not have a decomposition of categories starting from the class of all things, but many domain ontologies that do not extend an upper ontology still will require a few very general categories, such as the notion of a physical object or a process.

What counts as a domain is an issue of perspective, and is relative to the practitioner’s objectives. A particular application for preventing negative drug interactions (Zhao, Yin, Zhang, Zhang, & Chen 2023) might have few concepts relating to drug chemistry, while an application to support drug synthesis might have no concept of a drug interaction. However, a more general ontology about drugs might have both those concepts and more, but possibly a less extensive catalog of drugs.

There are vastly more domain ontologies in existence than upper ontologies (see the links to ontologies in the Other Internet Resources section below).

## 4. Ontological Commitment

What should an ontology commit to and what should it leave unspecified? If ontological commitment (see the entry on ontological commitment) is something to be minimized, then one might only commit to categories of Entity and Relation, with no other terms in the ontology. With such a minimal ontology of only two concepts there are virtually no commitments, but then also little utility is derived from such a theory in describing the world and assisting in creating a set of concepts and definitions that can be held in common by different entities. There is a clear tension between not wanting to make commitments that would limit the application of an ontology to only some narrow contexts, and with wanting to have as large a set of commitments as possible in order to facilitate common understandings.

But does creating and defining a concept in an ontology necessarily create a commitment? It depends on how such a definition is made. Let’s examine two cases consisting of a strong commitment and a weak commitment. If one states $\exists x \: \text{unicorn}(x)$ this has created what is likely a strong and unwise commitment. However if one states $\forall x \: (\text{unicorn}(x) \implies \exists y \: (\text{horn}(y) \land \text{part}(y,x)))$ a different, weak sort of commitment has been made that is likely not problematic. The latter formula only commits to the fact that *if* there were a unicorn in existence, it would have a horn. A commitment about how to define the characteristics of an imaginary entity, which isn’t necessarily presumed to exist, is quite a weak commitment. The practical issue of ontological commitment in the context of a computational ontology (as well as in philosophy more generally) hinges on whether a theory is not false – that is, not incompatible with modeling the world in useful software applications. One need not have an ontology that is capable of modeling all knowledge in the world for it to be practically useful. The question at hand then becomes the degree to which useful models of the world are excluded by a particular ontology, and the degree to which the ontology supports definition of various models. One could be concerned only with commitments that may rule out other reasonable commitments. An ontology that makes obviously poor modeling choices, such as requiring the Earth to be flat, makes an error of *commission* that excludes many of its possible uses. An ontology that has very few concepts or categories, or few definitions, has limited utility for modeling. It is an error of *omission* to avoid making commitments to concepts that are needed in modeling the world, such as omitting spatial or temporal relationships, or a way to model time or action. One can avoid being wrong by saying nothing at all. The challenge is to say as many things about the world as possible while not saying things that are false.

An illustration of choices in commitment (see the entry on identity over time) is that of Endurantism vs. Perdurantism: do objects have temporal parts and how are those parts related (Haslanger & Kurtz 2006)[^haslanger-2006]? But must one choose between alternatives for how we define a single notion of parthood or identity (see the entry relative identity)? One can have properties of an object that change while identity is maintained. A formal ontology creates not only a computationally useful product but also a laboratory for exploring how we see the world. One might suppose a conflict in views or theories, but absent a formal proof in the logic employed by a particular ontology, worries about a particular conflict in modeling choices are at best just unverified hypotheses. On the other hand if there is a proof of a logical contradiction, then there is a mathematical basis for asserting that a conflict in modeling choices actually exists, and working towards a harmonization of those choices. One might informally assume, for example, that identity must assume identicality (see the entry on identity of indiscernibles) ($\forall F(Fx \leftrightarrow Fy \implies x=y)$ for all properties $F$), but unless that ontological commitment is made axiomatically, in code that an automated theorem-prover or other inference system can execute, it is only a potential bad choice that has been avoided in practice.

An ontology that commits to every entity having a place in space and time has excluded timeless entities such as numbers. An ontology that commits to a notion of physical things (which have a place in space and time) and abstract things (which do not have a position in space or time) has merely created modeling facilities that may be employed, rather than a commitment that excludes an important aspect or view of the world.

A goal to minimize ontological commitments is related to a similar desire for an ontology that contains only a minimal set of primitives. How many concepts does one need? Is there a limit to the number of concepts that exist? If one takes human language as a guide, it would seem not: new words that express new concepts are created continually. The words “smartphone” and “selfie” were coined to express concepts that did not previously exist. While one could use existing words to express a similar thought, such as in “I took my – small computer that has a touchscreen and also functions as a phone – out of my pocket”, this would be a very inefficient form of discourse, which would still leave out the many connotations of the modern word of “smartphone”. One could conceivably define every concept during the course of communication, and avoid committing *a priori* to many words with associated definitions. Similarly, one might be able to build up a set of terms in an ontology from a small set of primitives, but it would be more efficient to archive each new term and definition as it appears to be needed.

One argument for a small set of ontological primitives is that it is easier to learn a smaller set than a larger one. One might look to modern software development for lessons learned in this case. While reusable software libraries were non-existent at the dawn of computing, now large libraries form an essential part of the modern software development process. It is inefficient to reinvent common abstractions. There are enough common abstractions that modern programming languages have tens of thousands of functions available for reuse. No programmer need learn all of them, and the ones that are unused in any given project cause no harm since unused library functions are not included by a compiler into a runnable program. Reusable components speed up development and increase compatibility among systems. An additional analogy is that an English dictionary that fits on a single page has vastly less utility for standardizing the meaning of words than a comprehensive collection such as Webster’s (Merriam-Webster 2003)[^merriam-webster-2003] or the OED (Oxford English Dictionary 2020)[^oxford-2020].

## 5. Ontology by Theory Elements

Ontologies that concern themselves with top-level or general categories (which are often called “upper ontologies”), as opposed to concepts specific to a domain (see section 3), have broadly similar inventories. One needs to have physical entities and abstract ones, substances and objects, processes, attributes, numbers of different sorts, and define these notions to organize the conceptual space and provide as much opportunity for abstraction as possible. The Tree of Porphyry (see section 2) also sets an example of providing *differentia* – an explanation of how each concept differs from the others. An undifferentiated concept is just a synonym of some others in an ontology. The first challenge for any ontologist is to learn how to create these descriptions, and reject any proposed concept for which no set of precise differentia can be given.

All the prominent upper ontologies have at least some version of the following concepts:

- Thing/Entity – The class of all things.
- Physical – The class of all things that have a position in space and time.
- Process/Action/Event – The class of things that *happen*.
- Object/PhysicalThing – The class of things that *are*. Tangible entities.
- Stuff/Mass – The class of things that may be subdivided and retain their identity (see the entry on mass expressions).
- PhysicalObject/CorpuscularObject – The class of things that may not be subdivided and retain their identity.
- Abstract/NonTangibleThing – The class of things that do not have a position in space and time.
- Relation – The class of relationships among entities.
- Property/Attribute.
- Function – The class of functional relationships: for every one element or unique combination of elements of the relation there is a unique other element.

Less common are catalogues of relationships. A few types of relationships such as the class of transitive relations are built into the Ontology Web Language (OWL) used in the semantic web community, rather than being defined in the ontology language, since the OWL language is not sufficient to express that property. Other common classes of relations are symmetric, reflexive, anti-symmetric etc.

Relationships found in common in some ontologies are:

- physical part/‘has a’ — one physical entity has another as a physical part, such as a door having a doorknob or a car having a wheel (see the entry on mereology).
- temporal part — an event or process has another event or process that is a part of the parent process (see the entry on temporal parts).
- physical location — something is located at a region or other object (see the entry on location and mereology)
- subclass/‘is a’ — one class of things is more specific than another class of things
- instance — an individual entity is a member of a class
- case roles (Fillmore 1968; Gisborne & Donaldson 2019)[^fillmore-1968][^gisborne-2019] such as agent, patient, instrument etc.
- temporal relationships among events (as in Allen 1984)[^allen-1984]: including before, meets, during, starts etc.

## 6. Ontology by Logical Language

While most things called ontologies are stated in some formal language, some ontologies do not employ a language with a formal (mathematical) semantics. A ontology that is essentially a glossary may collect words and natural language definitions. Humans must read such a product, resolve ambiguities in the language and reason about how they may apply to a specific problem. While a spelling or grammar checker can help with construction of such a document, machine or mathematical processes cannot be used to determine whether definitions are in conflict with one another. These shortcomings of natural language ontologies motivated the use of formal languages in the construction of ontologies.

The simplest formal languages used in ontologies are taxonomies and graphical languages. In a taxonomy, the only error that can be identified with automation is the presence of a cycle, where $A$ is a parent (possibly transitively) of $B$ and vice versa. The formal semantics for a taxonomy is that child nodes denote more specific concepts than their parent $\forall x : \text{child-class}(x) \implies \text{parent-class}(x)$.

The simplest graph language is one comprised of named nodes and arcs. Graphs do not have any inherent formal semantics other than that some relations hold. It may be as simple as that a graph G consists of vertices and edges $G = (V,E)$, although typically there will be some reusable set of edge labels (relations) $R$ and there should be no “orphan” nodes with no relationships – $G = (V,E,R)$ and:

$$\forall x \in V : \exists r,y: x r y \land r \in R \land y \in V.$$

Some meta-language may then be used to express a formal semantics for particular node and arc symbols, such as that a “PhysicalPart” arc is transitive. But many knowledge graphs and semantic networks do not have a formal specification, just an implementation in a software system. Note that an implementation in a software program is not a formal semantics. A semantics is a mathematical construct that exists outside any implementation. A program may enforce restrictions that are entailed by a mathematics, and several different programs might use different procedures to implement a single given body of semantics.

Description logic is a subset of first-order logic. It was created in order to provide a logical language with decidable inference, as in propositional logic, but with greater expressivity. First-order logic is only semi-decidable – while contradictions can be found in finite time, there is no guarantee that a theorem-prover will determine that no contradiction exists in finite time. The notion of finding contradictions is of critical importance since the most computationally efficient automated theorem-proving systems work by employing proof by refutation.

However, some variants of OWL go beyond description logic while also losing strict decidability but also not supporting all of standard first-order logic (Baader et al. 2007)[^baader-2007]. Considerable progress has also been made in first-order automated theorem-proving to avoid the worst case of undecidability (Geoff Sutcliffe & Desharnais 2024)[^sutcliffe-2024][^sutcliffe-2024-2]. Practitioners therefore differ in opinions about the choice of a particular logic to solve classes of problems.

Description logics such as the OWL family (Baader, Horrocks, & Sattler 2005) employ as part of the logic keywords that have definitions in a meta-language, since description logic is insufficient to describe their semantics. The OWL language must employ first-order logic in its language definition to state the semantics of some keywords that are part of the OWL language. In addition, OWL has the associated SWRL language (Horrocks, Patel-Schneider, Bechhofer, & Tsarkov 2005), in order to augment the description logic with a language capable of expressing rules. One implementation that preserves the semantics of SWRL uses a first-order-logic theorem-prover (Tsarkov, Riazanov, Bechhofer, & Horrocks 2004). Other implementations use the Drools rule engine (see the section Other Internet Resources) which is a production system rather than a logic (Shapiro 2001)[^shapiro-2001] and therefore loses some of the semantics of SWRL.

Relatively few ontologies are defined in more expressive languages such as first-order logic or beyond (notable exceptions are SUMO (Niles & Pease 2001; Pease 2011)[^niles-2001][^pease-2011] and Cyc (Lenat 1995)[^lenat-1995]). The more expressive the logic used, the more things that can be said about concepts, and therefore the more machine reasoning can be applied to answer questions with the ontology, or verify its consistency. For example, in a propositional logic one might have the propositional terms $S =$ “Socrates is a man” and $M =$ “Socrates is mortal” and state $S \implies M$. One would have to state that implication for all humans (and better yet, all organisms). In predicate calculus, one can state a more general rule just once:

$$\forall x \: \text{Organism}(x) \implies \text{Mortal}(x)$$

along with

$$\forall x \: \text{Man}(x) \implies \text{Organism}(x).$$

Going beyond first-order logic one might want to state the axiom of transitivity just once and have it hold for all instances of the type “TransitiveRelation”, rather than repeating that axiom for every such relation. The more expressive the logical language, the more efficient it is at encoding knowledge and creating generalizations, so any metrics about the size of an ontology must also take into account the logical expressiveness of the formulas counted.

Another issue in ontology languages and the reasoners that can process them is whether numbers and arithmetic are supported in the logical language. Measures and metric times are part of the world and yet very few ontologies employ a logic that can be paired with a reasoning system capable of reasoning with numbers. SNARK (Waldinger et al. 2004)[^waldinger-2004] is one such reasoner, which has its own language. TPTP Typed First-Order Form with Arithmetic (TFA: Sutcliffe, Schulz, Claessen, & Baumgartner 2012) is another language, implemented by a few theorem-provers including iProver (Korovin 2008)[^korovin-2008] and Vampire (Kovács & Voronkov 2013)[^kovács-2013].

Ontologies that are implemented in less expressive logical languages will leave more of their definitions to the intuitions and interpretations of humans. Such ontologies may be used for standardization of terminology among humans. Humans are then responsible for realization of those concepts in software. People must ensure that programs use those concepts correctly and embody their intended meaning. If the author of the ontology is also the author of the software, the realization is likely to be as intended. But there is a risk that others attempting to use the ontology to govern the behavior of their software may have a different understanding. This issue may become more prominent if the size of the system grows or if its use continues over a long period. Maintaining the same intuitions about the meaning of concepts will be more challenging without automation to ensure that interpretations remain consistent.

It is easy to conflate our own knowledge or interpretation with someone else’s. A good example of this is Newton1990, which shows how difficult it is for people to recognize a tune just by its rhythm, and how correspondingly challenging it is for a person providing a rhythm to realize that they haven’t provided enough information. An ontologist may believe that a label or natural language description is enough to constrain the interpretation of a symbol, but without detailed formal specification, it is all too easy for a different person to have a different interpretation. The more detailed and formal the specification, the more likely that different and conflicting interpretations can be avoided.

For those systems that do have an implementation of the ontology based on a taxonomy or graph language, developers may implement constraints on concepts in procedural code, such as the popular Java or Python programming languages, or may choose some auxilliary language that is more declarative, like Prolog, SWRL or Clips.

One advantage to using a less expressive logical language is greater computational efficiency. Description logics are decidable, and so queries are guaranteed to terminate. First-order logic is only semi-decidable and therefore queries may not terminate when there is not a proof showing how to satisfy the query. Higher-order logics have even fewer guarantees of performance. However, considerable progress (Sutcliffe & Desharnais 2023)[^sutcliffe-2023] has been made in avoiding theoretical worst-case scenarios for inference, and improving performance even on large theories (Pease, Sutcliffe, Siegel, & Trac 2010). Additionally, one can easily remove expressive formulas from an ontology for a given application in order to meet specific performance constraints, while retaining expressive formulas as a set of definition of the terms to align human understanding.

## 7. Assessment of an Ontology

Objective assessments of ontologies performed by disinterested third parties are rare, but Mascardi, Cordi, & Rosso 2007 is one, although it was done for upper ontologies rather than ontologies in general. Some objective measures include:

- whether a mathematical logic is used, and if so, which one. The choice of logical language will dictate what aspects of the definition of each concept are formally expressible, and what content has to be provided instead as an informal natural language comment.
- whether the logic has been implemented as a computational system, such as with an automated theorem-prover or inference engine. There are many logics with a formal semantics that have not been implemented for computation. If an ontology is defined in an unimplemented logic (and of non-trivial size) it will not be possible to validate that the ontology is free of contradictions, or to pose queries to it without using a human to calculate the result.
- which automated reasoner (if any) was used to validate the formulas and what are the limitations of the validation. A description-logic reasoner (such as FaCT++ (Tsarkov & Horrocks 2006)[^tsarkov-2006] or Pellet (Sirin, Parsia, Grau, Kalyanpur, & Katz 2007)) can guarantee that there are no type conflicts in an OWL ontology. A first-order reasoner can test an ontology in first-order logic in which more things can be stated than a description logic, but cannot guarantee to find all conflicts, due to first-order logic being semi-decidable. A first-order model-finder guarantees consistency if it finds a model, but the limitations of model-finders mean that it is only practical to attempt to analyze relatively small collections of formulas. A higher-order logic theorem-prover can attempt to validate yet more kinds of statements that are not expressible in less expressive logics, but performance of such systems is such that they are even less likely to find all contradictions that may exist.
- the number of concepts, which may be broken down further into instances, classes and relationships
- the number of formulas, and of which type, whether
- ground or not (the formula does not contain any variables)
- number of implications or disjunctions
- number of formulas containing a relation of a given arity (graphs and description logics are limited to binary relations)
- number of formulas requiring a given level of logical expressiveness, such as:
- propositional (no variables)
- description logic (classification/type reasoning)
- first-order logic (quantification over terms only)
- modal logic (and which particular modal-logic operators and supporting axioms)
- higher-order logic (quantification over formulas)
- number of formulas including numbers and/or arithmetic expressions

Some ontologies may have lexical mappings for their terms such as to WordNet (Fellbaum 1998)[^fellbaum-1998], in one or more human languages, so there could be a measurement of how many lexical mappings exist, and in how many languages.

For each of these measures, all others being equal, we may say that more is better.

Assessments may be also made as to non-technical characteristics, such as measurements of popularity, tool support, standards conformance, or licensing. Claims have often been made of the need to conform to some interpretation of an overarching philosophical principle, such as Realism (see the entry realism), Post-modernism and Relativism (see the entry on relativism), or Positivism (see the entries on logical empiricism and Auguste Comte).

## 8. Ontology and Large Language Models

Large Language Models (Jurafsky & Martin 2000)[^jurafsky-2000] are a model of language but not of the world (Bender, Gebru, McMillan-Major, & Shmitchell 2021). When LLMs generate text that is clearly at odds with what humans know about the world it has been called (rather anthropomorphically) “hallucination”. One method that has been proposed to address this issue is to combine LLMs and logical reasoning in a *neuro-symbolic* approach (Hitzler & Sarker 2021)[^hitzler-2021]. LLMs may be trained on symbolically-expressed knowledge (Chattopadhyay, Dandekar, & Roy 2025), and symbolic knowledge may be used in prompts (Lewis et al. 2020)[^lewis-2020]. LLMs may also be used to align terminological ontologies (Hertling & Paulheim 2023)[^hertling-2023].

Most work in this area has been with ontologies expressed as knowledge graphs. This potentially encourages LLMs to conform to facts such as taxonomic relationships, measures such as the cost or number of something, or expressions of simple relationships such as physical parthood. Using ontologies defined in expressive logics would allow LLMs to conform to the more complex relationships inherent in the world, but it remains to be seen how this can be implemented.

## 9. Applications of Ontologies

An ontology can be used solely as a tool for ensuring common understanding of concepts, or it can be used for reasoning (or both). Some surveys of ontology use include Qaswar et al. 2022; Poli, Healy, & Kameas 2010; Uschold & Jasper 1999. Many ontologies have been developed as an independent product that forms a standard for vocabulary, rather than as part of a running computational system. Many ontologies are used in application only by their authors, to illustrate their value, rather than being motivated by solving a particular application need.

Some uses of ontologies in applications are for search (Suomela & Kekäläinen 2005)[^suomela-2005], natural language processing (Bateman, Hois, Ross, & Tenbrink 2010; Behr, Völkenrath, & Kockmann 2023), Internet of Things applications (Qaswar et al. 2022)[^qaswar-2022] and engineering (Zheng et al. 2021)[^zheng-2021]. Biology is one application area that has seen considerable work on ontology development (Stevens & Lord 2009; Kramer & Beißbarth 2017)[^kramer-2017][^stevens-2009]. Implementations of such ontologies are often in the form of databases, and the positioning of such products as ontologies stems from the perspective of its authors rather than features of the product itself.

## 10. Future Directions

There is wide scope for further work in ontology, especially in developing ever larger and more formal theories for aspects of the world. Research at the most general levels of ontology in Computer Science is already starting to benefit from collaboration with what has been termed *computational metaphysics* (Kirchner, Benzmüller, & Zalta 2019; Fitelson & Zalta 2007)[^fitelson-2007]. Research on formally specifying aspects of the physical world, such as Casati & Varzi 1999 and Casati & Varzi 1994, illustrates comprehensive formal axiomatizations that could be implemented computationally.

One example of fundamental work on formalizing ontology of an aspect of the physical world, for which there does not yet appear to be a computational theory, is a theory of substances or substance-like actions that define what properties are true of parts of stuff that are true of the whole, at a given level of decomposition. For example, when does a temporal slice of walking cease to be walking and start being just a stepping or a motion? When does a part of a cake stop being a cake and start to be a sugar molecule? What relationships or concepts would allow for stating these limits of granularity and determine how properties of the whole are held by its parts? To what degree are the granularities of a class true of its subclasses?

The notion of competency questions points to a direction for evaluating the computational capabilities of ontologies (Wiśniewski, Potoniec, Ławrynowicz, & Keet 2019; Bezerra, Freitas, & Santana da Silva 2013). This area of study attempts to collect questions that may be asked of ontologies to evaluate their degree of knowledge. The challenge is to develop a corpus containing a wide range of questions, and determine how such a corpus can be tested without having an ontology simply be written for the test. One large project that took this approach, at least to an extent, was Cohen et al. 1998.

While description logics are the most widely used family of languages for ontologies, future work may increasingly use more expressive logics, and the OWL family of logics has grown to include incrementally more expressive languages. The automated theorem-proving community has been standardizing more expressive logics and implementing them in automated theorem-provers (Sutcliffe 2024)[^sutcliffe-2024][^sutcliffe-2024-2]. It is possible that increasing numbers of projects in ontology may take advantage of that work.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=ontology-is). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/ontology-is/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=ontology-is&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/ontology-is/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Upper Ontology](https://en.wikipedia.org/wiki/Upper_ontology), entry in Wikipedia
- [Ontologies](https://github.com/semantalytics/awesome-semantic-web?tab=readme-ov-file#ontologies), at GitHub.
- [Resource Description Framework](https://www.w3.org/RDF/), at www.w3.org
- [Drools rule engine](https://www.drools.org)

## Related Entries

logic: and ontology | ontological commitment | ontology, natural language

### Acknowledgments

The author thanks Stephan Schulz and the anonymous referees for thorough reviews that helped improve the entry. The editors would like to thank Chris Menzel for his constructive suggestions on earlier drafts.

[^allen-1984]: Allen, James, 1984, “Towards a General Theory of Action and Time,” *Artificial Intelligence*, 23: 123–154.

[^arp-2015]: Arp, Robert, Barry Smith, and Andrew D. Spear, 2015, *Building Ontologies with Basic Formal Ontology*, Cambridge, MA: MIT Press.

[^baader-2007]: Baader, Franz, Diego Calvanese, Deborah L. McGuinness, Daniele Nardi, and Peter F. Patel-Schneider (eds.), 2007, *The Description Logic Handbook*, 2nd edition, Cambridge: Cambridge University Press.

[^baader-2005]: Baader, Franz, Ian Horrocks, and Ulrike Sattler, 2005, “Description Logics as Ontology Languages for the Semantic Web,” in Dieter Hutter & Werner Stephan (eds.), *Mechanizing Mathematical Reasoning: Essays in Honor of Jörg H. Siekmann on the Occasion of his 60th Birthday*, pp. 228–248, Berlin, Heidelberg: Springer. doi:10.1007/978-3-540-32254-2_14

[^bateman-2010]: Bateman, John A., Joana Hois, Robert Ross, and Thora Tenbrink, 2010, “A Linguistic Ontology of Space for Natural Language Processing,” *Artificial Intelligence*, 174(14): 1027–1071. doi:10.1016/j.artint.2010.05.008

[^bechhofer-2004]: Bechhofer, Sean, Frank van Harmelen, Jim Hendler, Ian Horrocks, Deborah McGuinness, Peter Patel-Schneijder, and Lynn Andrea Stein, 2004, *OWL Web Ontology Language Reference* (W3C Recommendation), Mike Dean & Guus Schreijber (eds.), World Wide Web Consortium (W3C).

[^behr-2023]: Behr, Alexander S., Marc Völkenrath, and Norbert Kockmann, 2023, “Ontology Extension with NLP-Based Concept Extraction for Domain Experts in Catalytic Sciences,” *Knowledge and Information Systems*, 65(12): 5503–5522. doi:10.1007/s10115-023-01919-1

[^bender-2021]: Bender, Emily M., Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell, 2021, “On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?” in *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, pp. 610–623, New York: Association for Computing Machinery. doi:10.1145/3442188.3445922

[^benzmüller-2008]: Benzmüller, Christoph, Florian Rabe, and Geoff Sutcliffe, 2008, “THF0 – the Core of the TPTP Language for Higher-Order Logic,” in Alessandro Armando, Peter Baumgartner, & Gilles Dowek (eds.), *Automated Reasoning*, pp. 491–506, Berlin, Heidelberg: Springer.

[^bezerra-2013]: Bezerra, Camila, Fred Freitas, and Filipe Santana da Silva, 2013, “Evaluating Ontologies with Competency Questions,” in *2013 IEEE/WIC/ACM International Joint Conferences on Web Intelligence (WI) and Intelligent Agent Technologies (IAT)*, pp. 284–285. doi:10.1109/WI-IAT.2013.199

[^brownston-1985]: Brownston, Lee, Robert Farrell, Elaine Kant, and Nancy Martin, 1985, *Programming Expert Systems in OPS5: An Introduction to Rule-Based Programming*, Reading, MA: Addison-Wesley.

[^buchanan-1985]: Buchanan, Bruce G., and Edward H. Shortliffe (eds.), 1985, *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project*, Reading, MA: Addison-Wesley.

[^casati-1994]: Casati, Roberto, and Achille C. Varzi, 1994, *Holes and Other Superficialities*, Cambridge, MA: MIT Press.

[^casati-1999]: –––, 1999, *Parts and Places: The Structures of Spatial Representation*, Cambridge, MA: MIT Press.

[^chattopadhyay-2025]: Chattopadhyay, Aniruddha, Raj Dandekar, and Kaushik Roy, 2025, “Learning and Reasoning with Model-Grounded Symbolic Artificial Intelligence Systems,” in Leilani H. Gilpin, Eleonora Giunchiglia, Pascal Hitzler, & Emile van Krieken (eds.), *Proceedings of the 19th International Conference on Neurosymbolic Learning and Reasoning*, Vol. 284, pp. 957–976, PMLR. [[Chattopadhyay et al. 2025 available online](https://proceedings.mlr.press/v284/chattopadhyay25a.html)]

[^clocksin-2003]: Clocksin, William F., and Christopher S. Mellish, 2003, *Programming in Prolog*, 5th edition, Berlin, Heidelberg: Springer. doi:10.1007/978-3-642-55481-0

[^cohen-1998]: Cohen, Paul, Robert Schrag, Eric Jones, Adam Pease, Albert Lin, Barbara Starr, David Gunning, Murray Burke, 1998, “The DARPA High Performance Knowledge Bases Project,” *AI Magazine*, 19(4).

[^crevier-1993]: Crevier, Daniel, 1993, *AI: The Tumultuous History of the Search for Artificial Intelligence*, New York: Basic Books, Inc.

[^dallwitz-1980]: Dallwitz, M. J., 1980, “A General System for Coding Taxonomic Descriptions,” *Taxon*, 29(1): 41–46.

[^duda-1979]: Duda, R. O., J. Gaschnig, and P. E. Hart, 1979, “Model Design in the PROSPECTOR Consultant Program for Mineral Exploration,” in D. Michie (ed.), *Expert Systems in the Microelectronic Age*, pp. 153–167, Edinburgh: Edinburgh University Press.

[^eco-1995]: Eco, Umberto, 1995, *The Search for the Perfect Language [Ricerca della lingua perfetta nella cultura europea]*, Oxford: Blackwell.

[^enderton-1972]: Enderton, Herbert Bruce, 1972, *A Mathematical Introduction to Logic*, New York: Academic Press.

[^farquhar-1997]: Farquhar, Adam, Richard Fikes, and James Rice, 1997, “The Ontolingua Server: A Tool for Collaborative Ontology Construction,” *International Journal of Human-Computer Studies*, 46(6): 707–727. doi:10.1006/ijhc.1996.0121

[^fellbaum-1998]: Fellbaum, Christiane (ed.), 1998, *WordNet: An Electronic Lexical Database*, Cambridge, MA: MIT Press.

[^fillmore-1968]: Fillmore, Charles J., 1968, “The Case for Case,” in Emmon Bach & Robert T. Harms (eds.), *Universals in Linguistic Theory*, pp. 0–88, New York: Holt, Rinehart, & Winston.

[^fitelson-2007]: Fitelson, Branden, and Edward N. Zalta, 2007, “Steps Toward a Computational Metaphysics,” *Journal of Philosophical Logic*, 36(2): 227–247. doi:10.1007/s10992-006-9038-7

[^franklin-1986]: Franklin, James, 1986, “Aristotle on Species Variation,” *Philosophy*, 61(236): 245–252.

[^gangemi-2002]: Gangemi, Aldo, Nicola Guarino, Claudio Masolo, Alessandro Oltramari, and Luc Schneider, 2002, “Sweetening Ontologies with DOLCE,” in Asunción Gómez-Pérez & V. Richard Benjamins (eds.), *Knowledge Engineering and Knowledge Management: Ontologies and the Semantic Web: 13th International Conference, EKAW 2002 Sigüenza, Spain, October 1–4, 2002 Proceedings*, pp. 166–181, Berlin, Heidelberg: Springer. doi:10.1007/3-540-45810-7_18

[^genesereth-1992]: Genesereth, M. R., and R. E. Fikes, 1992, *Knowledge Interchange Format, Version 3.0 Reference Manual* (No. Logic-92-1), Stanford, CA: Stanford University. [[Genensereth & Fikes 1992 available online](http://logic.stanford.edu/publications/genesereth/kif.pdf)]

[^gisborne-2019]: Gisborne, Nikolas, and James Donaldson, 2019, “Thematic Roles and Events,” in Robert Truswell (ed.), *The Oxford Handbook of Event Structure*, pp. 236–264, Oxford: Oxford University Press.

[^gonçalves-2021]: Gonçalves, Bernardo, and Fabio Gagliardi Cozman, 2021, “The Future of AI: Neat or Scruffy?” in *Intelligent Systems: 10th Brazilian Conference, BRACIS 2021, Virtual Event, November 29 – December 3, 2021, Proceedings, Part II*, pp. 177–192, Berlin, Heidelberg: Springer. doi:10.1007/978-3-030-91699-2_13

[^gruber-1993]: Gruber, Thomas R., 1993, “A Translation Approach to Portable Ontology Specifications,” *Knowledge Acquisition*, 5(2): 199–220. doi:10.1006/knac.1993.1008

[^haslanger-2006]: Haslanger, Sally Anne, and Roxanne Marie Kurtz (eds.), 2006, *Persistence: Contemporary Readings*, Cambridge, MA: MIT Press.

[^hertling-2023]: Hertling, Sven, and Heiko Paulheim, 2023, “OLaLa: Ontology Matching with Large Language Models,” in *Proceedings of the 12th Knowledge Capture Conference 2023*, pp. 131–139, New York, NY: Association for Computing Machinery. doi:10.1145/3587259.3627571

[^hitzler-2021]: Hitzler, Pascal, and Md. Kamruzzaman Sarker, 2021, “Neuro-Symbolic Artificial Intelligence: The State of the Art,” in *Neuro-Symbolic Artificial Intelligence*, Thousand Oaks, CA: Sage. [[Hitzler & Sarker 2021 available online](https://www.gbv.de/dms/tib-ub-hannover/1786636506.pdf)]

[^horrocks-2005]: Horrocks, Ian, Peter F. Patel-Schneider, Sean Bechhofer, and Dmitry Tsarkov, 2005, “OWL Rules: A Proposal and Prototype Implementation,” *Journal of Web Semantics*, 3(1): 23–40. doi:10.1016/j.websem.2005.05.003

[^jurafsky-2000]: Jurafsky, Daniel, and James H. Martin, 2000, *Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition*, 1st edition, Upper Saddle River, PA: Prentice Hall.

[^kaliyar-2015]: Kaliyar, Rohit Kumar, 2015, “Graph Databases: A Survey,” in Abhishek Swaroop & Vishnu Sharma (eds.), *International Conference on Computing, Communication and Automation (ICCCA-2015)*, pp. 785–790, Curran Assoc. doi:10.1109/CCAA.2015.7148480

[^kirchner-2019]: Kirchner, Daniel, Christoph Benzmüller, and Edward N. Zalta, 2019, “Computer Science and Metaphysics: A Cross-Fertilization,” *Open Philosophy*, 2(1): 230–251. doi:doi:10.1515/opphil-2019-0015

[^korovin-2008]: Korovin, Konstantin, 2008, “iProver – an Instantiation-Based Theorem Prover for First-Order Logic (System Description),” in Alessandro Armando, Peter Baumgartner, & Gilles Dowek (eds.), *Automated Reasoning*, pp. 292–298, Berlin, Heidelberg: Springer.

[^kovács-2013]: Kovács, Laura, and Andrei Voronkov, 2013, “First-Order Theorem Proving and Vampire,” in *Proceedings of the 25th International Conference on Computer Aided Verification*, Vol. 8044, pp. 1–35, New York, NY: Springer. doi:10.1007/978-3-642-39799-8_1

[^kramer-2017]: Kramer, Frank, and Tim Beißbarth, 2017, “Working with Ontologies,” in *Methods in Molecular Biology*, 1525: 123–135, Berlin, Heidelberg: Springer. doi:10.1007/978-1-4939-6622-6_6

[^lehmann-1992]: Lehmann, F., 1992, *Semantic Networks in Artificial Intelligence*, Amsterdam: Elsevier Science Inc.

[^lenat-1995]: Lenat, D., 1995, “Cyc: A Large-Scale Investment in Knowledge Infrastructure,” *Comm. ACM*, 38(11).

[^lenat-1989]: Lenat, Douglas B., and R. V. Guha, 1989, *Building Large Knowledge-Based Systems; Representation and Inference in the Cyc Project*, 1st edition, USA: Reading, MA: Addison-Wesley.

[^levine-2017]: Levine, S. J., and K. Lateef-Jan, 2017, *Untranslatability Goes Global*, Abingdon: Routledge.

[^lewis-2020]: Lewis, Patrick, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, and Douwe Kiela, 2020, “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks,” in H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, & H. Lin (eds.), *Advances in Neural Information Processing Systems*, Vol. 33, pp. 9459–9474, Red Hook, NY: Curran Associates, Inc. [[Lewis et al. 2020 available online](https://proceedings.neurips.cc/paper_files/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf)]

[^linnaeus-1758]: Linnaeus, Carl von, 1758, *Systema naturae per regna tria naturae: secundum classes, ordines, genera, species, cum characteribus, differentiis, synonymis, locis*, Vol. V.1, Stockholm: Salvius. [[Linnaeus 1758 available online](https://archive.org/details/mobot31753000798865/page/n1/mode/2up)]

[^lu-2019]: Lu, Jie, Anjin Liu, Fan Dong, Feng Gu, João Gama, and Guangquan Zhang, 2019, “Learning Under Concept Drift: A Review,” *IEEE Transactions on Knowledge and Data Engineering*, 31(12): 2346–2363. doi:10.1109/TKDE.2018.2876857

[^magne-2017]: Magne, Matthew, 2017, “Data Drift Happens: 7 Pesky Problems with People Data,” *InformationWeek*, July 19. [[Magne 2017 available online](https://www.informationweek.com/data-management/data-drift-happens-7-pesky-problems-with-people-data)]

[^mascardi-2007]: Mascardi, V., V. Cordi, and P. Rosso, 2007, “A Comparison of Upper Ontologies,” in Matteo Baldoni, Antonio Boccalatte, Flavio De Paoli, Maurizio Martelli, & Viviana Mascardi (eds.), *Proceedings of WOA 2007*, pp. 55–64, Torino: Seneca.

[^merriam-webster-2003]: Merriam-Webster, 2003, *Merriam-Webster’s Collegiate Dictionary*, 11th edition, Springfield, MA: Merriam-Webster.

[^newton-1990]: Newton, L., 1990, *Overconfidence in the Communication of Intent: Heard and Unheard Melodies*, Ph.D. Thesis, Stanford, CA: Stanford University.

[^niles-2001]: Niles, Ian, and Adam Pease, 2001, “Toward a Standard Upper Ontology,” in Chris Welty & Barry Smith (eds.), *Proceedings of the 2nd International Conference on Formal Ontology in Information Systems (FOIS-2001)*, pp. 2–9, New York: Association for Computing Machinery.

[^oxford-2020]: Oxford English Dictionary, 2020, *OED Online*, Oxford: Oxford University Press. [[OED available online](https://www.oed.com/)]

[^pancha-2016]: Pancha, Girish, 2016, “Big Data’s Hidden Scourge: Data Drift,” *CMSWire*, April 8. [[Pancha 2016 available online](https://www.cmswire.com/big-data/big-datas-hidden-scourge-data-drift/)]

[^pease-2011]: Pease, Adam, 2011, *Ontology: A Practical Guide*, Angwin, CA: Articulate Software Press.

[^pease-2010]: Pease, Adam, Geoff Sutcliffe, Nick Siegel, and Steven Trac, 2010, “Large Theory Reasoning with SUMO at CASC,” *AI Communications, Special Issue on Practical Aspects of Automated Reasoning*, 23(2–3): 137–144.

[^poirier-2024]: Poirier, Lindsay, 2024, “Neat vs. Scruffy: How Early AI Researchers Classified Epistemic Cultures of Knowledge Representation,” *IEEE Annals of the History of Computing*, PP(99): 1–29. doi:10.1109/MAHC.2024.3498692

[^poli-2010]: Poli, Roberto, Michael Healy, and Achilles Kameas, 2010, *Theory and Applications of Ontology: Computer Applications*, Berlin, Heidelberg: Springer.

[^qaswar-2022]: Qaswar, Fahad, M. Rahmah, Muhammad Ahsan Raza, A. Noraziah, Basem Alkazemi, Z. Fauziah, Mohd. Khairul Azmi Hassan, and Ahmed Sharaf, 2022, “Applications of Ontology in the Internet of Things: A Systematic Analysis,” *Electronics*, 12(1), 111. doi:10.3390/electronics12010111

[^raths-2012]: Raths, Thomas, and Jens Otten, 2012, “The QMLTP Problem Library for First-Order Modal Logics,” in Bernhard Gramlich, Dale Miller, & Uli Sattler (eds.), *Automated Reasoning*, pp. 454–461, Berlin, Heidelberg: Springer.

[^riley-1987]: Riley, Gary, Chris Culbert, Robert T. Savely, and Frank Lopez, 1987, “CLIPS: An Expert System Tool for Delivery and Training,” in J. S. Denton, M. S. Freeman, & M. Vereen (ed.), *Third Conference on Artificial Intelligence for Space Applications – Part I*, pp. 53–57, NASA. [[Riley et al. 1987 available online](https://ntrs.nasa.gov/api/citations/19880006986/downloads/19880006986.pdf)]

[^robinson-2015]: Robinson, Ian, Jim Webber, and Emil Eifrem, 2015, *Graph Databases*, 2nd edition, Beijing: O’Reilly.

[^rumbaugh-2004]: Rumbaugh, James, Ivar Jacobson, and Grady Booch, 2004, *Unified Modeling Language Reference Manual*, 2nd edition, Pearson Higher Education.

[^shapiro-2001]: Shapiro, Stuart C., 2001, “Review of ”Knowledge Representation: Logical, Philosophical, and Computational Foundations“ by John F. Sowa,” *Computational Linguistics – COLI*.

[^sirin-2007]: Sirin, Evren, Bijan Parsia, Bernardo Cuenca Grau, Aditya Kalyanpur, and Yarden Katz, 2007, “Pellet: A Practical OWL-DL Reasoner,” *Web Semant.*, 5(2): 51–53. doi:10.1016/j.websem.2007.03.004

[^smith-2004]: Smith, Barry, Pierre Grenon, and Louis Goldberg, 2004, “Biodynamic Ontology: Applying Bfo in the Biomedical Domain,” *Studies in Health and Technology Informatics*, 102: 20–38.

[^stevens-2009]: Stevens, Robert, and Phillip Lord, 2009, “Application of Ontologies in Bioinformatics,” in Steffen Staab & Rudi Studer (eds.), *Handbook on Ontologies*, pp. 735–756, Berlin, Heidelberg: Springer.

[^subbiondo-1992]: Subbiondo, Joseph L. (ed.), 1992, *John Wilkins and 17th-Century British Linguistics*, Amsterdam: John Benjamins.

[^suomela-2005]: Suomela, Sari, and Jaana Kekäläinen, 2005, “Ontology as a Search-Tool: A Study of Real Users’ Query Formulation With and Without Conceptual Support,” in David E. Losada & Juan M. Fernández-Luna (eds.), *Advances in Information Retrieval*, pp. 315–329, Berlin, Heidelberg: Springer.

[^sutcliffe-2010]: Sutcliffe, Geoff, 2010, “The TPTP World – Infrastructure for Automated Reasoning,” in Edmund M. Clarke & Andrei Voronkov (eds.), *Logic for Programming, Artificial Intelligence, and Reasoning*, pp. 1–12, Berlin, Heidelberg: Springer.

[^sutcliffe-2024]: –––, 2024, “Stepping Stones in the TPTP World,” in C. Benzmüller, M. Heule, & R. Schmidt (eds.), *Proceedings of the 12th International Joint Conference on Automated Reasoning*, pp. 30–50, Berlin, Heidelberg: Springer.

[^sutcliffe-2023]: Sutcliffe, Geoff, and Martin Desharnais, 2023, “The 11th IJCAR Automated Theorem Proving System Competition – CASC-J11,” *AI Communications*, 36(2): 73–91.

[^sutcliffe-2024-2]: –––, 2024, “The CADE-29 Automated Theorem Proving System Competition – CASC-29,” *AI Communications*, 37(4): 485–503. doi:10.3233/AIC-230325

[^sutcliffe-2012]: Sutcliffe, Geoff, Stephan Schulz, Koen Claessen, and Peter Baumgartner, 2012, “The TPTP Typed First-Order Form with Arithmetic,” in Nikolaj Bjørner & Andrei Voronkov (eds.), *Logic for Programming, Artificial Intelligence, and Reasoning* (LPAR 2012), pp. 406–419, Berlin, Heidelberg: Springer.

[^sutcliffe-1998]: Sutcliffe, Geoff, and Christian Suttner, 1998, “The TPTP Problem Library,” *J. Autom. Reason.*, 21: 177–203, Berlin, Heidelberg: Springer. doi:10.1023/A:1005806324129

[^tsarkov-2006]: Tsarkov, Dmitry, and Ian Horrocks, 2006, “FaCT++ Description Logic Reasoner: System Description,” in *Proceedings of the Third International Joint Conference on Automated Reasoning*, pp. 292–297, Berlin, Heidelberg: Springer. doi:10.1007/11814771_26

[^tsarkov-2004]: Tsarkov, Dmitry, Alexandre Riazano, Sean Bechhofer, and Ian Horrocks, 2004, “Using Vampire to Reason with OWL,” in Sheila A. McIlraith, Dimitris Plexousakis, & Frank van Harmelen (eds.), *The Semantic Web – ISWC 2004*, pp. 471–485, Berlin, Heidelberg: Springer.

[^uschold-1999]: Uschold, Mike, and Jasper, Robert, 1999, “A Framework for Understanding and Classifying Ontology Applications,” in Richard Benjamins (ed.) *Proceedings of the IJCAI-99 Workshop on Ontologies and Problem-Solving Methods (KRR5)*, Vol. 2, Amsterdam: CEUR.

[^waldinger-2004]: Waldinger, Richard, Douglas E. Appelt, John Fry, David Israel, Peter Jarvis, David Martin, Susanne Riehemann, Mark E. Stickel, Mabry Tyson, Jerry Hobbs, and Jennifer Dungan, 2004, “Deductive Question Answering from Multiple Resources,” in Mark Maybury (ed.), *New Directions in Question Answering*, pp. 253–262, Berlin, Heidelberg: Springer.

[^wiśniewski-2019]: Wiśniewski, Dawid, Jedrzej Potoniec, Agnieszka Ławrynowicz, and C. Maria Keet, 2019, “Analysis of Ontology Competency Questions and Their Formalizations in SPARQL-OWL,” *Journal of Web Semantics*, 59 (100534). doi:10.1016/j.websem.2019.100534

[^woods-1975]: Woods, W. A., 1975, “What’s in a Link: Foundations for Semantic Networks,” in D. G. Bobrow & A. M. Collins (eds.), *Representation and Understanding: Studies in Cognitive Science*, pp. 35–82, New York: Academic Press.

[^zhao-2023]: Zhao, Yan, Jun Yin, Li Zhang, Yong Zhang, and Xing Chen, 2023, “Drug–Drug Interaction Prediction: Databases, Web Servers and Computational Models,” *Briefings in Bioinformatics*, 25(1): bbad445. doi:10.1093/bib/bbad445

[^zheng-2021]: Zheng, Xiaochen, Jinzhi Lu, Rebeca Arista, Xiaodu Hu, Joachim Lentes, Fernando Ubis, Jyri Sorvari, and Dimitris Kiritsis, 2021, “Development of an Application Ontology for Knowledge Management to Support Aircraft Assembly System Design,” in Emilio M. Sanfilippo, Oliver Kutz, Nicolas Troquard, et al. (eds.), *JOWO*, Volume 2969, CEUR-WS.org. [[Zheng et al. 2021 available online](https://ceur-ws.org/Vol-2969/paper21-FOMI.pdf)]
