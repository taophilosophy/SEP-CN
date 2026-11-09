# Two-Dimensional Semantics
**First published Mon Dec 13, 2010; substantive revision Mon Aug 23, 2021**

*Schroeter, Laura*

Two-dimensional (2D) semantics is a formal framework that is used to characterize the meaning of certain linguistic expressions and the entailment relations among sentences containing them. Two-dimensional semantics has also been applied to thought contents. In contrast with standard possible worlds semantics, 2D semantics assigns extensions and truth-values to expressions relative to two possible world parameters, rather than just one. So a 2D semantic framework provides finer-grained semantic values than those available within standard possible world semantics, while using the same basic model-theoretic resources. The 2D framework itself is just a formal tool. To develop a semantic theory for someone’s language, a proponent of 2D semantics must do three things: (i) explain what exactly the two possible world parameters represent, (ii) explain the rules for assigning 2D semantic values to a person’s words and sentences, and (iii) explain how 2D semantic values help in understanding the meanings of the person’s words and sentences.

The two-dimensional framework has been interpreted in different ways for different explanatory purposes. The two most widely accepted applications of two-dimensional semantics target restricted classes of expressions. David Kaplan’s 2D semantic framework for indexicals is widely used to explain conventional semantic rules governing context-dependent expressions like ‘I’, ‘that’, or ‘here’, which pick out different things depending on the context in which the expression is used. And logicians working on tense and modal logic use 2D semantics to characterize the logical implications of operators like ‘now’, ‘actually’, and ‘necessarily’. Such restricted applications of 2D semantics are intended to systematize and explain uncontroversial aspects of linguistic understanding.

Two-dimensional semantics has also been used for more ambitious philosophical purposes. Influential theorists like David Lewis, Frank Jackson and David Chalmers argue that a generalized 2D semantic framework can be used to isolate an apriori aspect of meaning. Roughly, the idea is that speakers always have apriori access to the truth-conditions associated with their own sentences. On the face of it, this apriority claim seems to conflict with the observation that certain necessary truths, such as ‘water = H₂O’, can be known only on the basis of empirical inquiry. But proponents of generalized 2D semantics argue that the 2D framework undercuts this objection, by showing how such aposteriori necessities are consistent with apriori access to truth-conditions. The positive reasons to accept generalized 2D semantics, however, are bound up with larger (and partly disjoint) explanatory projects. As a consequence, debates over the merits of generalized 2D semantics touch on broader controversies about apriority, modality, semantic theory and philosophical methodology.

The two-dimensional framework can also figure in a theory of *ad hoc* language use, instead of a theory of literal meanings. Robert Stalnaker’s influential 2D account of assertion falls in this category. His “metasemantic” interpretation of the 2D framework is intended to characterize what is communicated when conversational partners are partially ignorant or mistaken about the literal meaning of their own words. Although it is formally similar to generalized 2D semantics, Stalnaker’s use of the 2D framework avoids apriori accessible truth-conditions of the sort posited by generalized 2D semantics.

## 1. Restricted 2D Semantics

Two-dimensional semantics was introduced to model the semantics of context-sensitive expressions in natural language, like indexicals and demonstratives. A similar 2D framework was developed to model important aspects of tense and modal logic.

### 1.1 Indexicals

#### 1.1.1 The need for a 2D framework

Semantic theories explain how the truth or falsity of whole sentences depends on the meanings of their parts by stating rules governing the interpretation of subsentential expressions and their modes of combination. A semantic framework provides a standard formalism for stating such rules. The simplest (0-dimensional) semantic frameworks work by assigning *extensions* as the semantic values of particular expressions. Intuitively, the extension includes those things in the actual world to which the expression applies: e.g., the extension of the name ‘Barack Obama’ is the man Obama, the extension of the predicate ‘is cool’ is the set of all the actual cool things, and the extension of a two-place predicate ‘is cooler than’ is the set of pairs of actually existing things the first of which is cooler than the second. A whole sentence is assigned a truth-value (True or False) as its extension, which is computed on the basis of the extensions of the component expressions: e.g., the sentence, ‘Barack Obama is cool’, will have the semantic value True just in case Obama is a member of the set of actual cool things. A two-dimensional semantic framework is the result of enriching this simple extensional framework in two distinct ways.

The first enrichment, *standard possible worlds semantics*, is introduced to explain the meaning of modal operators like ‘possible’ and ‘necessary’ and to distinguish the intuitive subject matter represented by particular subsentential expressions. Consider the expressions ‘Roger Federer’, ‘the greatest tennis player of all time’, and ‘the most famous Swiss citizen in 2020’. Let’s assume all three expressions happen to have exactly the same extension: a particular individual RF. So a simple extensional semantics will assign exactly the same semantic value to all three expressions. But clearly they differ in meaning: if events had unfolded only slightly differently than they actually did, the three expressions would pick out different people. In general, definite descriptions like ‘the greatest tennis player’ or ‘the most famous Swiss citizen’ pick out different individuals depending on who happens to have the relevant properties in counterfactual situations; whereas proper names like ‘Roger Federer’ *rigidly* pick out the very same individual in every possible situation.[^note-1] [See entry on rigid designators.] Moreover, such differences in what expressions pick out in counterfactual situations affect the truth of modal claims: e.g., ‘Federer is necessarily Federer’ is true, but ‘Federer is necessarily the greatest tennis player’ is false. So there is an aspect of meaning that is not captured in simple extensional semantics. The basic idea behind possible world semantics is to map out such differences in meaning by specifying what an expression picks out *relative to every possible way the world could be* (every “possible world”).

In standard (1-dimensional) possible worlds semantics, the semantic value of an expression is an *intension*, a function that assigns an extension to the expression “at” every possible world. For instance, the semantic value of a definite description like ‘the best known Swiss citizen’ is a function that takes as input a possible world and yields as output whoever happens to satisfy that description in that world, and the semantic value of a proper name like ‘Roger Federer’ is a constant function that maps every possible world to the very same individual, RF. Such intensions reflect commonsense intuitions about the “modal profile” of the objects, kinds, or properties picked out by our words – i.e. different possible ways those features could be instantiated.[^note-2] This framework is also used to explain the meaning of modal operators like ‘necessarily’ and ‘possibly’: a sentence is necessarily true just in case it is true at every possible world, and it is possibly true just in case it is true at some possible world. [See the entries on intensional logic and modal logic.]

The second enrichment of the basic extensional semantic framework—the one that is distinctive of two-dimensional semantics—requires us to take possible worlds into account in a different way. To see why this might be necessary for an adequate account of meaning, let’s focus on context-sensitive expressions like ‘I’, ‘here’ or ‘this’. In one respect, these terms function like names, picking out the very same thing in every possible world. For instance, if Hillary Clinton says ‘I could have been president’, her word ‘I’ refers rigidly to the same woman, HC, in every possible world and her claim is true just in case there is a possible way the world could be in which HC is president. In standard possible worlds semantics, then, the intension o of ‘I’ is exactly the same as the intension of the name ‘Hillary Clinton’: a function that yields the individual HC for every possible world. But clearly the English word ‘I’ is not synonymous with the name ‘Hillary Clinton’—for John McCain might utter the sentence ‘I could have been president’ and in his mouth the word ‘I’ would refer rigidly to a different person, JM, in every possible world. What’s distinctive of context-sensitive expressions like ‘I’ or ‘this’ is that they represent different things depending on the context in which they are used. David Kaplan (1989a)[^note-3] first brought widespread attention to this phenomenon of context-dependence by proposing his influential two-dimensional semantic theory to clarify the rules governing such expressions.

Kaplan distinguishes two different aspects of the meaning of expressions in a public language. The first aspect, *content*, reflects the modal profile of the object, kind or property represented. This is the aspect of meaning that is modeled by standard possible world semantics. The second aspect of meaning, *character*, reflects semantic rules governing how the content of an expression may vary from one context of use to the next. A context-invariant expression like ‘Hillary Clinton’ has a constant character, picking out the very same object in every context in which it’s used, whereas indexical expressions like ‘I’ or ‘this’ have variable character, picking out different things in different contexts of use.

Formally, character is defined as a function that maps possible contexts of use to contents, and content is defined as a function mapping possible worlds to extensions. Thus, a character is a function that takes as input a context and yields as output a function from possible worlds to extensions. This is a *two-dimensional intension*, since there are two distinct roles that possibilities play here: as a context of use, and as a circumstance of evaluation (a possible situation relative to which we evaluate whether the relevant object exists or property is instantiated). Contexts of use can be thought of as “centered” worlds: possible worlds with a designated agent and time within that world, which serve to locate a particular situation in which the expression is used. We can then represent a context as an ordered triple, $\langle w,a,t\rangle$ , of a possible world w, an agent a within that world, and a time t when the agent exists in that world.[^note-4] So possible worlds play two distinct roles in Kaplan’s formalism: contexts of use determine which content is expressed and circumstances of evaluation reflect the modal profile of that content. The conventional semantic rules governing an expression like ‘I’ can be easily represented using Kaplan’s 2D framework: in any possible context, $\langle w,a,t\rangle$, an utterance of ‘I’ *rigidly designates* the agent of that context, *a*, in all possible circumstances of evaluation. [See the entry on indexicals for a more detailed discussion].

#### 1.1.2 Introducing 2D matrices

A useful way of visualizing the dual role played by possible worlds in a 2D framework is to construct *a two-dimensional matrix* (Stalnaker 1978)[^stalnaker-1978]. To represent Kaplan’s theory of indexicals, we array possible circumstances of evaluation along the horizontal axis and possible contexts of utterance along the vertical axis. Each horizontal row of the matrix represents the *content* the target expression would have if used in the context specified for that row. This content is (partially) represented by recording the extension of the term at each possible circumstance arrayed along the horizontal axis. This procedure is then repeated for each context listed along the vertical axis.

For instance, consider a particular utterance of ‘I’ made by Barack Obama during his inaugural presidential address. This context of use can be represented as the world $w_1$, centered on the man BO, at time $t_0$. We can (partially) represent the content of ‘I’ in this centered world thus:

*Obama’s use of ‘I’ in his inaugural address:*

|   | $w_1$ | $w_2$ | $w_3$ |
| --- | --- | --- | --- |
| $\langle w_1, \BO, t_0\rangle$ | BO | BO | BO |

This simple one-dimensional matrix reflects the fact that, when used in this context, ‘I’ refers rigidly to Obama at every possible circumstance of evaluation—even at the counterfactual worlds $w_2$ and $w_3$, in which John McCain or Hillary Rodham Clinton won the 2008 presidential election. The context-dependence of the expression ‘I’ is revealed when we evaluate the use of ‘I’ with respect to different possible contexts of use. Let’s consider two other contexts: $\langle w_2, \JM, t_0\rangle$ is a world in which McCain won the election, centered on him at his inaugural address; and $\langle w_3, \HC, t_0\rangle$ is a world in which Clinton won, centered on her at her inaugural address. We then rely on our implicit understanding of the semantic rules governing ‘I’ to generate two more rows for our matrix:

*Kaplanian character of ‘I’:*

|   | $w_1$ | $w_2$ | $w_3$ |
| --- | --- | --- | --- |
| $\langle w_1, \BO, t_0\rangle$ | BO | BO | BO |
| $\langle w_2, \JM, t_0\rangle$ | JM | JM | JM |
| $\langle w_3, \HC, t_0\rangle$ | HC | HC | HC |

What the matrix reveals is that the expression ‘I’ rigidly designates different individuals, depending on the context in which it is used. Thus the 2D matrix provides a graphic illustration of how content of the expression ‘I’ varies, depending on the context in which it is used.

Such 2D matrices can be used to represent the differences between the semantic rules governing indexicals, definite descriptions, and names. For instance, the definite description ‘the inaugural speaker in 2009’ will generate the following Kaplanian matrix:

*Kaplanian character of ‘the inaugural speaker in 2009’:*

|   | $w_1$ | $w_2$ | $w_3$ |
| --- | --- | --- | --- |
| $\langle w_1, \BO, t_0\rangle$ | BO | JM | HC |
| $\langle w_2, \JM, t_0\rangle$ | BO | JM | HC |
| $\langle w_3, \HC, t_0\rangle$ | BO | JM | HC |

Unlike the matrix for ‘I’, the horizontal rows of this 2D matrix are all exactly the same. This reflects the fact that the expression ‘the inaugural speaker in 2009’ is not context-sensitive: it always represents the very same property irrespective of the context in which it is used—namely, the property of being the person who delivers the inaugural US presidential address in 2009. This property is exemplified by different individuals at different possible worlds: the person who is the inaugural speaker at $w_1$ is Obama, at $w_2$ it’s McCain, and at $w_3$ it’s Clinton. In general, the sequence arrayed along the rows of this matrix reflects the variety of different individuals who could instantiate the property represented by ‘the inaugural speaker’ in different circumstances. Of course, no finite matrix can fully capture the range of variation, but it can give a useful partial representation of the property in question.

The matrix for a proper name like ‘Barack Obama’ reveals another very different pattern:

*Kaplanian character of ‘Barack Obama’:*

|   | $w_1$ | $w_2$ | $w_3$ |
| --- | --- | --- | --- |
| $\langle w_1, \BO, t_0\rangle$ | BO | BO | BO |
| $\langle w_2, \JM, t_0\rangle$ | BO | BO | BO |
| $\langle w_3, \HC, t_0\rangle$ | BO | BO | BO |

According to Kaplan, proper names are context-invariant: they always have the very same content irrespective of the context in which they are used. Proper names are also rigid designators: they pick out a single individual at every possible world. The upshot is that the 2D matrix for a proper name will be completely uniform: the very same individual appears in every cell of the matrix. This reflects the idea that the semantic function of a name in a public language is simply to pick out a particular individual, not to convey any information about how to identify the individual in question. [For a different account of proper names, see §2.2 below.]

#### 1.1.3 The logic of indexicals and diagonal intensions

Kaplan’s semantic rules for indexicals guarantee that certain sentences will be true whenever they are uttered, and certain inferences will be truth preserving. This account paved the way for Kaplan’s formal logic of indexicals (Kaplan 1989a)[^kaplan-1989a]. In this system, logical validity is defined in terms of different possible contexts of use: a sentence is valid iff it is true in every possible context of use; and an inference is valid iff the truth of the premises ensures the truth of the conclusion in every possible context of use.

On Kaplan’s account, sentences can be logically valid, even if they express contingent propositions. For instance, the semantic rules governing indexicals ensures that the sentence ‘I am here’ will be true in any context of use. But the content expressed is normally contingent: I could easily *not* have been here right now, but at the beach instead.

To illustrate, we can construct a partial 2D matrix for the sentence using our previous example. Suppose ‘I am here now’ is uttered by the new president at the inauguration (*t₀*) in $w_1$ where Obama won, $w_2$, where McCain won, and $w_3$ where Clinton won. Let’s assume Obama would attend the inaugural address of McCain but not of Clinton, McCain would avoid the inauguration of anyone who defeated him, and Clinton would attend Obama’s inauguration but not McCain’s. This yields the following 2D matrix:

*Kaplanian character of ‘I am here’*

|   | $w_1$ | $w_2$ | $w_3$ |
| --- | --- | --- | --- |
| $\langle w_1, \BO, t_0\rangle$ | **T** | T | F |
| $\langle w_2, \JM, t_0\rangle$ | F | **T** | F |
| $\langle w_3, \HC, t_0\rangle$ | T | F | **T** |

The horizontal rows of the matrix represent the different propositions expressed by the sentence in each context of use. Each utterance expresses a different contingent proposition, as can be seen by the fact that each contains both ‘T’s and ‘F’s, and that the patterns differ. The 2D matrix also graphically represents the fact that the sentence is guaranteed to be true whenever uttered. Notice the diagonal of the matrix running from the top left corner to the bottom right, which contains all ‘T’s. This reflects the fact that the sentence is guaranteed to be true whenever uttered. With a nod to Stalnaker (1978), we can call this the *diagonal intension* of the sentence. In Kaplan’s semantic framework, a necessary diagonal intension indicates that a sentence is *logically valid* and *analytic*.[^note-5]

### 1.2 Modal Operators

At around the same time that Kaplan began developing his account of indexicals, logicians working on tense and modal logic had begun using 2D semantic frameworks to explain the behavior of sentential operators like ‘now’ and ‘actually’ (Åqvist 1973; Kamp 1971; Segerberg 1973; Vlach 1973)[^åqvist-1973][^kamp-1971][^segerberg-1973][^vlach-1973]. Unlike Kaplan, these logicians were not primarily concerned with the semantic rules governing natural languages. In particular, modal logicians were not focused on how the context in which an expression is used can affect its reference. Rather, they were interested in developing formal systems for representing valid inferences about time and possibility. It turns out that tense and modal logic are formally very similar and that both require double-indexing for expressive adequacy. Thus, to fully capture reasoning about what’s necessary and possible, we need to move from standard possible worlds semantics to a 2D semantic framework.

#### 1.2.1 ‘Actually’ and ‘Necessarily’

Consider the following sentence:

**(1)**

It is possible for everything that is actually red to be shiny.

Standard possible worlds semantics lacks the expressive power to capture what is said by this sentence (Crossley and Humberstone 1977; Hazen 1976, 1978)[^crossley-1977][^hazen-1976]. The claim is not that there is a possible world such that all the things that are red in that world are also shiny in that world (they’re supposed to be red in the *actual* world, not the counterfactual one). Nor is the claim that for each object that is red, there is a possible world in which it is shiny (the objects are all supposed to be shiny *together* within a single possible world). So here is a relation among objects in possible worlds that cannot be expressed in standard possible world semantics. To capture the relation, we need to introduce an extra element into the formal framework: we simply designate one world within the model (the set of possible worlds) to play the role of the actual world. We can then introduce a sentential operator ‘$\mathcal{A}$’ (read as ‘Actually’), which requires us to *evaluate any claim within its scope at the designated world*, even when the operator is embedded within the scope of other modal operators. Using this enriched possible worlds framework, we can represent the truth-conditions of our sample sentence in a straightforward way:

**$(1')$**

$\Diamond \forall x(\mathcal{A}\Red(x) \rightarrow \Shiny(x))$

This sentence is true just in case there is some possible world, w, in which everything that is red in the designated world, $w_@$, is shiny in w.

One awkward consequence of this 2D semantic account of ‘Actually’ is the way this operator interacts with the standard modal operator ‘Necessarily’. Intuitively, what the actual world is like seems logically and metaphysically contingent. But according to the proposed semantics for ‘Actually’, any true sentence S will yield a *necessary* *truth* when embedded within the scope of the operator ‘$\mathcal{A}$’. For instance, consider the following sentence:

**(2)**

Obama actually won the 2008 election.

If Obama won in the designated world of our model, then it’s true at every possible world in that model that Obama won at its designated world. So on the proposed 2D semantics, the sentence is *necessarily true*. (When we embed (2) within the necessity operator ‘$\Box$’ we get a truth; and any claim of the form $\mathcal{A}S \rightarrow \Box \mathcal{A}S$ will be logically valid.) But intuitively it’s a *contingent* matter how the 2008 elections turned out. To mitigate this counterintuitive consequence, Crossley and Humberstone introduce a new logical operator, ‘Fixedly’ (‘$\mathcal{F}$’) in such a way that the complex operator ‘Fixedly Actually’ (‘$\mathcal{F}\mathcal{A}$’), captures the sense of necessity we have in mind when we deny that (2) is necessary. A sentence is fixedly actually true just in case it is *true no matter which world is designated as actual*.[^note-6]

#### 1.2.2 A 2D model

Once again, 2D matrices can be used to graphically depict how the semantic theory works. Let’s take our universe of possible worlds to contain just three worlds: $w_1$ is a world where Obama won, $w_2$ a world where McCain won, and $w_3$ a world where Clinton won. To explain the ‘Fixedly Actually’ operator, we need to consider possible worlds playing two different roles: the standard role as a circumstance of evaluation and the special role of being designated as the actual world. To construct a 2D matrix, we array possible worlds playing the standard role along the horizontal axis, and along the vertical axis we array the same worlds playing the role of being designated as actual. Each horizontal row of this matrix represents a different model with a particular world designated as actual.[^note-7] On this account, the truth of a sentence embedded within the ‘Actually’ operator depends entirely on what’s true in the world designated as actual in a given model. So we can fill in the 2D matrix as follows:

*C&H matrix for ‘Obama actually won.’*

|   | $w_1$ | $w_2$ | $w_3$ |
| --- | --- | --- | --- |
| $w_1$ as actual | **T** | T | T |
| $w_2$ as actual | F | **F** | F |
| $w_3$ as actual | F | F | **F** |

In any world in a model (a row in the matrix), ‘Actually S’ is always evaluated by looking at the designated world of that model. So such sentences are either necessarily true (True at every world in the model) or necessarily false (False at every world in the model). This is the sense of necessity that corresponds to the standard modal operator ‘$\Box$’. On this understanding of necessity, the target sentence is necessarily true (since $w_1$ represents the *actual* actual world). But intuitively there is a sense in which the sentence seems contingent, since a different world could have been actual: if $w_2$ or $w_3$ had been actual, the sentence ‘Obama actually won’ would have been false. This fact is reflected in the 2D matrix by the diagonal intension, where the sentence comes out true with respect to $\langle w_1, w_1\rangle$, but false with respect to $\langle w_2, w_2\rangle$ and $\langle w_3, w_3\rangle$. The ‘Fixedly Actually’ operator is sensitive to the necessity or contingency of the diagonal intension. The sense in which the target sentence (2) is not necessary is that it’s not fixedly actually true.

While this double-indexing model has become standard in the literature, as (Rabern 2012b)[^rabern-2012b] points out, the same expressive adequacy considerations Crossley and Humberstone (1977) used to support two indices for modal and temporal operators also support *multiple-indexing* for those operators. For instance, consider the following sentence:

**(3)**

If the Titanic had not hit an iceberge on its maiden voyage, it would still have been possible for everyone would then have survived the maiden voyage to die on the maiden voyage. (Rabern 2012b: 119)[^rabern-2012b]

To generate the correct analysis, we need to invoke three distinct worlds: the actual world $w_1$, where the Titanic hit an iceberg, a counterfactual world $w_2$ where it did not, and another counterfactual world $w_3$ where all survivors of the voyage in $w_2$ died. So double-indexing and 2D matrices cannot fully capture the compositional semantics of modal sentences: we will need an infinite sequence of possible world indices. For further work on multiple-indexed semantics, see (Ninan 2010; Yalcin 2015)[^yalcin-2015].

#### 1.2.3 Philosophical applications

An influential paper by Martin Davies and Lloyd Humberstone (1980) brought the formal tools developed in 2D modal logic to bear on philosophical puzzles about modality. Following Gareth Evans (1979), Davies and Humberstone suggest that there are two notions of metaphysical necessity involved in ordinary modal thinking: deep and superficial necessity. They argue that the two logical operators, ‘$\mathcal{F}\mathcal{A}$’ and ‘$\Box$’, respectively, provide a clear formal elucidation of these two notions.

These two notions of necessity, they argue, help explain some of Saul Kripke’s (1980) puzzling examples in which necessity and apriority come apart. Using 2D modal logic, it’s easy to construct necessary aposteriori truths. The semantic rules governing the modal operator ‘$\mathcal{A}$’ guarantee that every claim of the form $\mathcal{A}S$ will be either necessarily true or necessarily false in the sense of ‘$\Box$’. But when the embedded sentence S is an ordinary empirical truth like ‘Obama won’, $\mathcal{A}S$ will be knowable only aposteriori: so $\mathcal{A}S$ will be a necessary aposteriori truth. The ‘Actually’ operator can also be used to construct contingent apriori truths. Any claim of the form $(\mathcal{A}S \rightarrow S)$ is guaranteed by the semantic rules governing ‘Actually’ to be true at the designated world no matter which world is designated as actual (i.e., it’s fixedly actually true). But when S is an ordinary empirical truth, the complex claim is not necessary in the sense of ‘$\Box$’: there will be some worlds in the model where S is false while $\mathcal{A}S$ is true. In such cases, the complex sentence will be a contingent apriori truth.

Davies and Humberstone also suggest that the 2D modal operator ‘Actually’ might help analyze certain referring expressions in natural language. In particular, they focus on Evans’ (1982) notion of a ‘descriptive name’ (a name whose reference is fixed by a description) and on natural kind terms. Suppose the following definitions capture the semantic rules governing the relevant expressions in natural language:

1. Julius $=_{df}$ the actual inventor of the zip.
2. Water $=_{df}$ the actual chemical kind to which that liquid belongs which falls from clouds, flows in rivers, is drinkable, colorless, odorless, etc.

If such analyses are correct, then the semantics for ‘actually’ will allow us to explain why ‘Julius invented the zip’ is contingent and apriori and ‘water = H₂O’ is necessary aposteriori.[^note-8] [See the entries on names and descriptions. For a survey of other philosophical applications of the 2D framework in modal logic see (Humberstone 2004)[^humberstone-2004].]

Davies and Humberstone themselves express reservations about the adequacy of analyses using ‘actually’ for natural language expressions, particularly in the case of proper names (1980, 17–21). As a consequence, they did not take 2D modal logic to provide a complete response to Kripke’s puzzles about necessary aposteriori and contingent apriori truths. However, the use of the 2D framework to explain these puzzles was subsequently taken up and refined by proponents of generalized 2D semantics.

## 2. Generalized 2D Semantics

### 2.1 Vindicating the traditional approach to meaning

In the previous sections, we considered applications of the 2D framework that seek to explain the meaning of specific types of expression: indexicals and modal operators. In contrast, proponents of generalized 2D semantics (G2D) believe that the 2D framework can be used to explain an important aspect of the meaning of *all* expressions. In particular, G2D is meant to vindicate the traditional idea that we have apriori access to our own meanings through armchair reflection.

According to the philosophical tradition, to know the meaning of a subsentential expression like ‘bachelor’ is to implicitly grasp a criterion that determines exactly which individuals count as bachelors in any possible situation. (Accounts of meaning broadly along these lines were advanced by Plato, Descartes, Locke, Hume, Frege, Russell, Carnap, and many others.) On the traditional account, speakers’ implicit grasp of a criterion plays two key theoretical roles:

1. Semantic competence: Two speakers (or one speaker on two occasions) share the same meaning just in case they associate the very same criterion with their expressions.
2. Reference determination: The criterion a speaker currently associates with an expression determines which things fall into its extension in every possible situation.

The first claim requires that speakers who share the same meaning must share a criterion for identifying the reference; while the second requires that this criterion be veridical. If this traditional account of meaning is correct, then one can make one’s own meanings explicit by engaging in *apriori conceptual analysis*. Such conceptual analysis allows you to determine what exactly it takes to count as a bachelor in any possible world; and it allows you to specify what exactly someone must be prepared to accept in order to genuinely agree or disagree about bachelors.

G2D is a strategy for defending a variant of this traditional view of meaning against a series of influential objections. In the 1970s and 80s, semantic externalists used a variety of persuasive examples to argue that the traditional account of meaning yields an unrealistic picture of (i) semantic competence, (ii) reference determination, and (iii) epistemic access to modal facts. Proper names and natural kind terms seem especially problematic for the traditional account.[^note-9] By commonsense standards, you don’t need to know a specific rule for identifying Gödel in any possible world in order to count as competent with the name ‘Gödel’; and no such knowledge seems required for your use of the name to pick out the relevant man in every possible world (Donnellan 1970; Kripke 1980)[^donnellan-1970][^kripke-1980].[^note-10] Similarly, you don’t need to know precisely what it takes for something to count as water in any possible world to be competent with the word ‘water’ or for your word to pick out the chemical substance H₂O in every possible world (Kripke 1980; Putnam 1970, 1972)[^kripke-1980][^putnam-1970]. Indeed, making room for the possibility of ignorance and error about reference-conditions seems crucial to explaining empirical inquiry into the nature of familiar things, and to vindicating the commonsense realist idea that we can refer to things whose nature we don’t fully understand (Burge 1979, 1986; Putnam 1972, 1973)[^burge-1979][^putnam-1972]. If these critics are right, then the traditional account of meaning is untenable. Implicit knowledge of reference-conditions is *not* required either for linguistic competence or for determinate reference. And apriori conceptual analysis cannot be trusted to reveal what’s genuinely possible—at best, it reveals one’s current fallible assumptions about the topic in question. [See the entry on externalism about mental content.]

Proponents of G2D believe this pessimistic conclusion is unwarranted. What critics’ examples really show, they argue, is that the traditional view of meaning should be refined, not junked. Moreover, the 2D semantics developed for indexicals and modal operators suggests a promising strategy for accommodating putative externalist counterexamples within a broadly traditional account of meaning. In the case of indexicals and rigidified definite descriptions, competent speakers grasp a *reference-fixing criterion* without grasping *the modal profile* of the object, kind, or property picked out by the expression. For instance, you can know that ‘I’ always refers to the speaker whenever it is uttered without knowing the nature of the person who is actually picked (e.g., what it takes to be Barack Obama in any possible world). Perhaps our understanding of names and natural kind terms is structured in a similar way: competent speakers always have apriori access to the reference-fixing criterion for their own use of the name ‘Barack Obama’, but they have only aposteriori access to the associated modal profile. If this suggestion is on the right track, then a G2D framework could be used to clarify the nature of this semantic understanding. Moreover we may be able to explain certain epistemic operators, like ‘it is conceptually possible that’ or ‘it is apriori that’, as operating on such 2D semantic values.

The basic philosophical idea behind G2D—that subjects have apriori access to reference-fixing criteria for their words but not to the modal profile of the subject matter picked out—has been suggested by a number of theorists. David Lewis, in particular, was a powerful champion of the idea that we can give apriori definitions for terms whose precise reference we do not understand. Lewis articulated the ‘analytic functionalist’ approach to specifying the meaning of mental predicates and of theoretical terms in science (1966; 1970; 1972; 1979; 1980; 1994); and he was also an early advocate of a generalized 2D approach to semantics (1981; 1994). Other influential proponents of the idea that we can have implicit knowledge of reference-fixing criteria without knowing the modal profile of the reference include Michael Dummett (1973; 1981), Gareth Evans (1982), and John Searle (1983). Early proponents of an explicitly two-dimensional semantics for names and natural kind terms include Harry Deutsch (1990, 1993), Ulrike Haas-Spohn (1995), and Kai-Yee Wong (1996). However, it is two later theorists—Frank Jackson (1994; 1998a; 1998b; 2004) and David Chalmers (1996; 2002b; 2002c; 2004; 2006a)—who have most systematically developed and defended G2D as a way of reconciling the lessons of semantic externalism with the traditional apriori approach to meaning and modality.

It’s worth noting that G2D has been motivated primarily by epistemic, metasemantic, and metaphysical concerns, rather than by issues in compositional semantics. In particular, G2D seeks to vindicate the traditional idea that we can know the truth-conditions of our own sentences via armchair reasoning about hypothetical cases. The approach promises to explain why certain necessary truths can only be known aposteriori by appealing to the structure of our implicit semantic understanding. Proponents of G2D make claims about how the two types of intension may interact with modal and epistemic operators. However, working out the details of the compositional semantics has been a relatively recent concern of proponents of G2D (e.g. Chalmers 2011a, c; Chalmers and Rabern 2014; Johannesson and Packalén 2016; Kipper 2017)[^chalmers-2011a][^chalmers-2014][^johannesson-2016][^kipper-2017].

The 2D semantic frameworks proposed by Jackson and Chalmers are very similar in their broad aims and formal structure, and commentators often treat the two versions as interchangeable. However, the two frameworks are developed in the service of two quite different philosophical projects, emphasizing different aspects of the traditional approach to meaning. Jackson takes up the traditional empiricist project of explaining empirical facts about language use and communication, while Chalmers pursues a broadly rationalist project of explaining key structural interconnections between meaning, apriority, and possibility. This difference in explanatory aims leads to different interpretations of the 2D framework.

### 2.2 The empiricist project

#### 2.2.1 Linguistic understanding and coordination

An empiricist account of meaning is a high-level causal explanation of uncontroversial facts about language use. In particular, the empiricist seeks to characterize the psychological states that guide individuals’ application of an expression to particular cases, and to explain how linguistic coordination within a linguistic community is achieved.

Clearly individual speakers must have some implicit assumptions about the reference of a word that guide their verdicts about whether it applies to particular cases (Jackson 1998a, 29–42)[^jackson-1998a]. Your judgments about whether a particular Gettier case counts as knowledge, for instance, are guided by your prior understanding of the term ‘knowledge’, and your answer is only justified insofar as it reflects that prior understanding. An empiricist seeks to explain these facts by positing a stable internal psychological state—something like an *internal reference-fixing template*—that guides your verdicts no matter what the actual world turns out to be like.

It’s equally clear that members of the same linguistic community generally manage to use words to reliably coordinate their beliefs and actions (Jackson 1998b, 2004)[^jackson-1998b]. When I ask you to pass the salt, you know roughly which white granular substance I’m asking for—you know, for instance, that it would be inappropriate to pass the sugar bowl or the pepper grinder. This sort of everyday coordination requires speakers to have similar dispositions to classify things as falling into the extension of words, and it requires that these similarities in classificatory dispositions be mutually obvious to all concerned: for it to make sense for me to say ‘please pass the salt’ in order to get salt, it must be common knowledge between us that we’re inclined to classify roughly the same things as ‘salt’. An empiricist explains this common knowledge by positing *implicit conventions* that require everyone to associate the very same reference-fixing template with a given word (Jackson 1998b; Lewis 1969)[^jackson-1998b][^lewis-1969].

An empiricist use of the 2D framework is intended to show that this core explanatory project is not undermined by the intuitions about names and natural kind terms highlighted by semantic externalists (Jackson 1998a; 1998b)[^jackson-1998a].[^note-11]

#### 2.2.2 The role of the 2D framework

Externalists argue that ordinary speakers are often ignorant or mistaken about the precise nature (modal profile) of the objects, kinds or properties their words pick out. But linguistic conventions don’t always fix the reference by specifying the nature of the reference. Perhaps the conventions governing names and natural kind terms are structured in a similar way to indexicals. For instance, we might have an implicit semantic rule requiring us to take ‘water’ to pick out whatever chemical kind *actually* explains a certain suite of superficial observable properties: e.g., being a clear, potable, odorless liquid that fills lakes and streams around here (Jackson 1998a, 1998b)[^jackson-1998a]. On this analysis, ‘water’ just is an implicitly indexical expression, picking out different chemical kinds depending on which world is actual. If this rule is what one must accept to count as competent with the meaning of the expression type ‘water’, then it is no surprise that competent speakers often fail to realize that water = H₂O.

Of course, it is an empirical question whether names and natural kind terms are in fact governed by indirect reference-fixing rules of this sort. But according to Jackson, you can test whether your implicit understanding of ‘water’ is structured in this way by considering possible situations in two different roles: as *your actual environment* or as *a mere counterfactual possibility* (Jackson 1998a, ch. 2)[^jackson-1998a]. Consider two different possible worlds based on Putnam’s Twin Earth thought experiment (Putnam 1972)[^putnam-1972]. In the first world, Earth, the clear potable stuff that fills lakes and streams and is habitually called ‘water’ by English speakers is H₂O. The second world, Twin Earth, is exactly the same except that the stuff that has these properties is the complex chemical kind, XYZ. If your commonsense understanding of ‘water’ is governed by the proposed reference-fixing convention, it would lead you to identify different chemical substances as water depending on what your actual environment is like: if your actual environment is Earth, then water is H₂O; but if your actual environment is Twin Earth, then water is XYZ. If you assume that water is *actually* H₂O, moreover, you will judge that water is *essentially* H₂O in all counterfactual circumstances. And if you assume water is *actually* XYZ, then you’ll judge water is *essentially* XYZ.

This pattern of dispositions to apply the term ‘water’ can be depicted on a 2D matrix as follows:

*Empiricist 2D matrix for ‘water’:*

|   | Earth | Twin Earth |
| --- | --- | --- |
| $\langle$Earth, $a, t\rangle$ | **H₂O** | H₂O |
| $\langle$Twin Earth, $a, t\rangle$ | XYZ | **XYZ** |

Along the vertical axis are ranged centered possible worlds (a possible world, with a designated agent a and time t within that world) representing different ways your actual environment could be like; and the same worlds are ranged along the horizontal axis representing different counterfactual circumstances of evaluation. This matrix reflects your commonsense dispositions to apply the term ‘water’ to different chemical kinds on the basis of whether it actually plays certain superficial roles described in other commonsense terms (‘clear’, ‘potable’, ‘liquid’, etc).[^note-12]

Semantic externalists take these sorts of judgments about Twin Earth to militate against a traditional account of meaning—for they suggest that your understanding does not fully determine the nature of the reference. But according to Jackson, the only conclusion that is warranted is that the meaning of your term is more complex than the tradition suggests: your verdicts about possible worlds considered as actual reflect your *naïve reference-fixing criterion*, and your verdicts about possible worlds considered as counterfactual reflect the *theoretical criterion* you would accept after you learned all the relevant empirical facts about your actual environment. These two types of criterion can be modeled in possible world semantics as intensions: an A-intension (for ‘Actual’) is a function from worlds considered as actual to extensions, while a C-intension (for ‘Counterfactual’) is a function from worlds considered as counterfactual to extensions (Jackson 1998a, ch.2)[^jackson-1998a]. The diagonal of our matrix corresponds to the A-intension you associate with ‘water’; and the first horizontal row corresponds to the C-intension of your term ‘water’ (assuming that $\langle$Earth, $a, t\rangle$ represents your real-world environment).

Semantic externalists acknowledge only the C-intension as modeling an expression’s semantic content, but 2D empiricists insist that both A- and C-intensions reflect important aspects of a competent English speaker’s understanding of a word like ‘water’. In particular, they take A-intensions to reflect what is understood and communicated by minimally competent English speakers and what guides their everyday classifications. The suggestion, then, is that A-intensions capture the shared, conventionally entrenched understanding of reference-fixing conditions posited by the empiricist approach to meaning.

By itself, this 2D framework offers no guarantee that the hypothetical judgments recorded by an A-intension are produced by a stable reference-fixing criterion. Nor does it guarantee that the very same A-intension will be generated for all competent speakers in your linguistic community. However, according to Jackson, we have solid empirical reasons to think these conditions are satisfied in the case of names and natural kind terms. First, the widespread acceptance of the externalist thought experiments demonstrates that we do in fact share similar reference-fixing criteria for terms like ‘water’ and ‘Gödel’ (Jackson 1998a, 38–39)[^jackson-1998a]. Second, the empiricist model of meaning provides the best psychological explanation of how such linguistic coordination is achieved (Jackson 1998b)[^jackson-1998b].[^note-13]

#### 2.2.3 Apriori conceptual analysis

In addition to clarifying the structure of our semantic understanding, the 2D framework can help justify specific conceptual analyses. The criteria that implicitly guide our everyday use of a term are often embodied in recognitional or inferential dispositions rather than in consciously accessible rules. Indeed, Jackson likens grasp of reference-fixing criteria for particular expressions to our ability to recognize the grammaticality of sentences in one’s own language (2000). Just as linguists can construct a grammar for your language on the basis of your judgments about the acceptability of particular sentences, you can construct an analysis of the meaning you associate with an expression on the basis of your application of a term to hypothetical cases. The correct analysis must capture the full range of your confident judgments involving the target expression, while abstracting away from performance errors and other interfering factors (Jackson 1998a, 31–37)[^jackson-1998a].

This psychological model helps explain how you can come to know the correct analysis of your term ‘water’ by noting which properties you treat as “obvious and central” when filling in a 2D matrix like the one above (Jackson 1998a, 31)[^jackson-1998a]. The 2D framework prompts you to consider possible cases in two different ways–as actual or as counterfactual. This allows you to know whether the content of your term varies depending on what your actual environment is like (e.g. ‘water’) or whether it is stable (e.g. ‘bachelor’). Moreover, careful attention to your reactions to these suppositions will allow you to make explicit which superficial properties implicitly guide your application of the term. For instance, you may discover that your implicit criterion for applying ‘water’ is that water $=_{df}$ the actual chemical kind in your environment that is a clear, potable, odorless liquid that falls as rain and fills lakes and streams. Alternatively, your use of the term ‘water’ may be guided by the types of causal relations invoked in causal theories of reference: water $=_{df}$ the actual natural kind that has been the dominant cause of your community’s past use of the term ‘water’. Indeed, Jackson suggests that standard causal theories of reference are based on this method of conceptual analysis (1998a, 37–41). [See the entry on causal theories of mental content.]

The conceptual analyses produced by this method count as apriori, according to the 2D empiricist, because you can know them to be correct “independently of knowing what the actual world is like” (Jackson 1998a, 51)[^jackson-1998a]. The evidence that supports such analyses consists in purely hypothetical judgments: judgments about how to classify cases *on the supposition* that your environment is like X, or like Y. Since such hypothetical judgments don’t require you to determine what your *real* environment is like, your justification for accepting an analysis is not based on empirical knowledge. And to change your judgment about a purely hypothetical case would be to change the meaning of your term (Jackson 1998a, 44–46)[^jackson-1998a].

#### 2.2.4 The role of conceptual analysis in metaphysics

Jackson claims that apriori conceptual analysis plays a crucial role in metaphysics (Jackson 1994; 1998a)[^jackson-1994]. Metaphysical reductions provide a constitutive account of some target domain (e.g., beliefs, free will, water, moral rightness) in terms of more basic features of the world (e.g., the properties postulated by an idealized physics, ideas in the mind of God, the mosaic of sense data). A physicalist about mental states, for instance, is committed to there being specific facts about the microphysical structure of the world that suffice for the existence of beliefs, desires and sensory experiences. The physicalist is thus committed to metaphysically necessary “entailments” connecting claims about the two domains: it’s metaphysically necessary that if such-and-such physical facts obtain, then such-and-such mental facts obtain. This metaphysical entailment relation can arguably be cashed out in terms of global supervenience (Jackson 1998a, 6–14)[^jackson-1998a]. [See the entry on supervenience.]

The role of conceptual analysis is to show that a putative reduction respects the original meaning of the target expression (Jackson 1998a, 28)[^jackson-1998a]. A physicalist won’t succeed in accounting for free will if she identifies free will with having a temperature of 37.4º C – such a “reduction” would simply change the subject under discussion. A successful reduction must be answerable to our original shared understanding of the target expression—and elucidating this original understanding just is what conceptual analysis does. So if conceptual analyses are knowable apriori, it follows that metaphysical reductions must always be backed by apriori entailments between the base-level claim (such as a physical description of the world) and the target claim (such as the claim that humans have free will).

On this empiricist account, conceptual analysis plays a modest metaphysical role. Conceptual analysis captures apriori entailment relations among your ideas; but it cannot tell you whether there *are* any objects, kinds, or properties that satisfy your current reference-fixing assumptions (Jackson 1998a, 42–4)[^jackson-1998a]. Moreover, the meaning you currently associate with a term may be pragmatically deficient: e.g., it may not be determinate enough to settle certain hard cases or it may not allow you to draw useful distinctions in your actual environment. In such cases, you would have good pragmatic reasons to change the meaning of your term (Jackson 1998a, 44–6, 53–4)[^jackson-1998a]. What the empiricist denies is that changing your current criteria for applying a term can ever get you closer to the truth about what you meant all along.

### 2.3 The rationalist project

#### 2.3.1 Connecting meaning, apriority, and possibility

For an empiricist, an expression’s meaning reflects the causal mechanisms guiding everyday classification and communication. For a rationalist, in contrast, an expression’s meaning reflects what is apriori accessible to the speaker on the basis of ideal reflection. The empiricist is primarily concerned with causal explanation of linguistic facts, while the rationalist is primarily concerned with idealized apriori rationality and insights into objective possibility. This difference in emphasis can have significant ramifications for G2D.

David Chalmers has developed a detailed and influential rationalist interpretation of the 2D framework. This semantic project is situated within a broadly rationalist tradition that posits a “golden triangle” of necessary constitutive relations between meaning, apriority, and possibility (2004; 2006a; 2012).

Following Frege (1892), Chalmers is interested in capturing a notion of meaning that is finer-grained than reference. Frege pointed out that sentences containing co-referential expressions like ‘Hesperus’ and ‘Phosphorus’ can differ in *cognitive significance*: someone who is competent with these two names may not realize they are co-referential and may therefore use them differently in making and justifying claims. Frege took sameness of cognitive significance to be the mark of sameness of meaning. According to a 2D rationalist, sameness of cognitive significance can in most cases be elucidated in terms of *apriori equivalence*: two expressions are associated with the same meaning iff one can know that they pick out the very same things on the basis of apriori reflection alone (Chalmers 2002b)[^chalmers-2002b].[^note-14] This constitutive link between meaning and apriority constitutes the first side of the “golden triangle”.

The second side of the “golden triangle” connects meaning with possibility. Following Carnap (1947), Chalmers suggests that we can use possible worlds semantics to individuate particular meanings in terms of their representational properties. In standard possible world semantics, the meaning of ‘doctor’ is identified with an *intension* that maps possible worlds to extensions. An expression’s intension reflects the modal profile of the object, kind, or property picked out. Identifying meanings with intensions therefore establishes an important constitutive connection between meanings and modal claims. If ‘doctor’ and ‘physician’ are associated with the same meaning, then it’s *true in all possible worlds* that all doctors are physicians and all physicians are doctors. And conversely if two expressions are *co-extensive in all possible worlds*, then they have the same meaning.

The third side of the “golden triangle” connects possibility with apriority. Following Kant (1787), a rationalist about modality holds that what is necessary is always knowable apriori and what is knowable apriori is always necessary. Thus ideal apriori reflection can be trusted to reveal the space of possibility.

This “golden triangle” of constitutive relations generates a distinctive rationalist account of meaning. To be competent with an expression’s meaning is to be in an internal cognitive state that puts one in a position to identify its extension in any possible world on the basis of apriori reflection alone. Apriori reflection will also suffice to determine whether two expressions are associated with the same or different meanings. This rationalist approach to meaning contrasts with the empiricist one: whereas the empiricist uses *causally efficacious cognitive mechanisms* to isolate the reference-fixing criteria currently associated with an expression, the rationalist uses the subject’s *ideally rational judgments* to isolate the complex cognitive states that would ground those reflective judgments. As a consequence, the aspect of understanding that corresponds to a rationalist meaning may turn out to be more heterogeneous and less stable than the shared, causally efficacious ‘templates’ postulated by the empiricist. The “golden triangle” also involves a distinctive rationalist account of modal epistemology, according to which ideal apriori conceivability is a fail-safe guide to metaphysical possibility. This modal rationalism affords a simple and attractive account of our access to modal facts (Chalmers 1996, 136–8; 1999, 488–91; 2002a)[^chalmers-1996].[^note-15]

This simple rationalist picture of meaning and modality, however, was undermined by externalist thought experiments. Kripke’s (1980) observation that certain necessary truths, like ‘Hesperus = Phosphorus’, are only knowable aposteriori threatens both the idea that linguistic competence affords apriori access to the truth- and applicability-conditions of one’s words and the idea that necessary truths are always apriori knowable. The guiding idea behind 2D rationalism is that a rationalist can accommodate Kripke’s examples by moving to a 2D semantic framework. In particular, the 2D framework can be used to isolate an aspect of meaning that satisfies the “golden triangle” of constitutive relations among meaning, apriority and modality.

Roughly, the idea is that ‘Hesperus = Phosphorus’ is aposteriori because we associate distinct reference-fixing criteria with the two names: e.g., being the brightest star visible in the evening and the brightest star visible the morning. According to the 2D rationalist, these reference-fixing criteria are (i) an aspect of meaning, (ii) which can be known apriori via conceptual analysis, and (iii) which suffices to fix the applicability conditions for every possible world considered as one’s actual environment. If the 2D framework can be used to isolate such an aspect of meaning for all expressions, we will have vindicated the rationalist’s “golden triangle” connecting meaning, apriority and possibility.

Vindicating this “golden triangle” constitutes a primary theoretical constraint for a rationalist interpretation of 2D semantics. A 2D semantics that meets this constraint would play a wide-ranging role in philosophy. It would account for core semantic roles associated with the Fregean notion of sense (Chalmers 2002b)[^chalmers-2002b] and the traditional notion of a proposition (Chalmers 2011a)[^chalmers-2011a]. In addition, rationalist 2D semantics promises to define a versatile notion of narrow thought content suited to playing key explanatory and evaluative roles in commonsense psychology (Chalmers 2002c)[^chalmers-2002c]. Furthermore, the rationalist approach to meaning and modality underwrites a distinctive form of apriori reasoning about the nature of the actual world:

> There is a long tradition in philosophy of using apriori methods to draw conclusions about what is possible and what is necessary, and often in turn to draw conclusions about matters of substantive metaphysics. Arguments like this typically have three steps: first an epistemic claim (about what can be known or conceived), from there to a modal claim (about what is possible or necessary), and from there to a metaphysical claim (about the nature of things in the world). (Chalmers 2002a, 145)[^chalmers-2002a]

Chalmers has developed an influential anti-physicalist argument along these lines, which relies on a rationalist 2D semantic framework to establish that facts about phenomenal consciousness cannot be reduced to physical or functional facts about the brain (1996; 2009). See the supplementary document:

*[The 2D argument against materialism](two-dimensional-semantics.supplement.md).*

#### 2.3.2 The epistemic interpretation of the 2D framework

Any interpretation of the 2D framework must answer the following two questions:

1. What is the nature of the worlds to be considered as actual?
2. What is the principle for determining an expression’s extension relative to worlds considered as actual?

But the rationalist project imposes specific constraints on how these questions are answered. To vindicate the “golden triangle”, the rationalist must identify a way of mapping an individual speaker’s understanding of particular expressions onto possible worlds that affords apriori access to the entire space of possibility. This is not a trivial requirement: standard ways of interpreting the 2D framework cannot vindicate the rationalist project. However Chalmers has developed a distinctive “epistemic” interpretation of the 2D framework that he believes can establish the relevant constitutive links between meaning, apriority and possibility (2004, 2006a).

A rationalist 2D semantics must vindicate the following principle:

Core Thesis: For any sentence $S,$ $S$ is apriori iff $S$ has a necessary 1-intension. (Chalmers 2004, 165)[^chalmers-2004]

A sentence’s 1-intension is an intension that corresponds to the diagonal of a 2D matrix. So the Core Thesis affirms that a token sentence is apriori (for a subject at a particular time) just in case there is no possible way the world might be that, if it actually obtained, would make S false. In effect, the Core Thesis sums up the “golden triangle” of constitutive connections the rationalist hopes to establish between meaning, apriority, and possibility: (i) it postulates a possible way the world could be for every apriori coherent hypothesis, and vice versa; and (ii) this tight connection between apriority and possibility is reflected in an aspect of linguistic meaning, the 1-intension.[^note-16]

The major obstacle to vindicating the Core Thesis for standard interpretations of the 2D framework is the assignment principle—the way 2D theories assign extensions relative to “worlds considered as actual”. A natural way of understanding the injunction to consider a possible world as actual is to simply imagine a possible world, locate a person in it at a time, and then rely on ordinary interpretive methods to decide what exactly that person in those empirical circumstances is referring to when using a given expression. Chalmers calls this strategy for assigning 1-intensions to expressions a “contextualist” interpretation of the 2D framework. What’s distinctive of a contextualist approach is (i) that a token of the target expression must be located within the world considered as actual, and (ii) that the expression is assigned an extension on the basis of how it’s used in that world. On this approach, a 1-intension will be *undefined* for possible worlds that do not contain a token of the target expression: no extension can be assigned for such worlds, not even an empty extension.

This contextualist approach to assigning 1-intensions is incompatible with the Core Thesis (Chalmers 2004, 167­–176)[^chalmers-2004]. Consider sentences like ‘Language exists’ or ‘A sentient being exists’: the meaning of these sentences seems to guarantee that they will be true in every possible context in which they are used. So on the contextualist approach, these sentences should be assigned necessary 1-intensions, mapping every possible context of use to the truth-value True. But contrary to the Core Thesis, these sentences are *not* apriori truths knowable independently of any empirical evidence. There’s no contradiction in the very idea of a world without language or thought and we can easily imagine what such a world would be like; it’s just that our everyday experience allows us to immediately rule out the possibility that our actual environment is like that. The problem is that contextualist 1-intensions are undefined for worlds without thought or language, even though they are both apriori coherent and metaphysically possible. So a necessary contextual 1-intension does not track apriority or metaphysical necessity. Contextualist 1-intensions, therefore, cannot satisfy the rationalist’s Core Thesis.[^note-17]

This difficulty can be avoided, Chalmers argues, if we rely on a notion of *epistemic possibility*—what *seems* possible after ideal rational reflection—to interpret the 2D framework. More specifically, he focuses on the notion of apriori coherence: claims that could be true for all one can tell on the basis of idealized apriori reasoning.[^note-18] This notion of apriori coherence is used to answer the two interpretive questions highlighted above: (i) apriori coherence is used to characterize the possibilities relative to which 1-intensions are defined, and (ii) apriori coherence is invoked to assign 1-intensions to a speaker’s expressions.

First consider the possibilities that define 1-intensions. On the epistemic interpretation, the possibilities are not metaphysically possible contexts of use, but epistemically possible “scenarios”: maximally specific hypotheses about what one’s actual environment might be like that cannot be ruled out through apriori reasoning alone. Scenarios provide a complete characterization of the entire history of a universe, down to the last microphysical detail. They also provide perspectival information—a notional “center”—that indicates the location from which the hypothetical universe is to be considered. The crucial point is that scenarios are defined by their epistemic role: they represent ways we can conceive of the actual world, within which we can try to identify familiar objects, kinds or properties.[^note-19]

The second distinctive element of the epistemic interpretation of 2D semantics is the procedure for assigning 1-intensions to a speaker’s expressions. On the epistemic approach, 1-intensions reflect relations of apriori coherence between descriptions of possible scenarios and ordinary language sentences:

> The epistemic 1-intension for a sentence S is True at a scenario W iff $(W$ & not$-S)$ is apriori incoherent. (Chalmers 2004, 180–4)[^chalmers-2004]

This principle for assigning 1-intensions relies on the speaker’s ordinary ability to engage in object-level reasoning about combinations of hypotheses: given the assumption that the scenario description W is true, you’re asked to decide whether S must be true as well. If it’s incoherent to accept $(W$ & not$-S)$, your epistemic intension for S maps W to True, otherwise W is mapped to False. This epistemic assignment principle contrasts sharply with the contextualist principle. The contextualist approach requires us to engage in explicit meta-linguistic reasoning to interpret the expression ‘S’ *as it’s used* within the possible world W. On the epistemic approach, in contrast, an extension is assigned to ‘S’ on the basis of the subject’s own object-level reasoning using the expressions ‘W’ and ‘S’.

Unlike the contextualist approach, therefore, the epistemic assignment principle does not explicitly require that a scenario contain a token of the relevant expression type in order to assign an extension relative to that scenario. As a consequence, sentences like ‘Language exists’ seem to pose no special problem for satisfying the Core Thesis. The sentence ‘Language exists’ will have a contingent epistemic 1-intension, because there are possible scenarios that are apriori consistent with both the truth and falsity of that sentence. For instance, consider a scenario in which the only object is a giant lump of salt. To test whether your sentence ‘Language exists’ is true at this scenario considered as actual, you ask whether there is any incoherence in combining the claim ‘The only object that exists is a lump of salt’ with the claim ‘It’s not the case that language exists’. Intuitively, this combination is coherent: there is no language in the salt world. So the epistemic 1-intension for your sentence ‘Language exists’ yields the value False for that scenario. Since there are other scenarios relative to which the sentence ‘Language exists’ will have the value True, your sentence will have a contingent epistemic 1-intension. This contingent epistemic intension for your sentence ‘Language exists’ reflects the fact that it’s not apriori true that language exists. So it seems the epistemic assignment principle will allow apriority and necessity of the 1-intension to go hand in hand, as required by the Core Thesis.

#### 2.3.3 Defining the E2D framework

There is further work to do in spelling out Chalmers’ E2D framework in such a way as to vindicate his rationalist project. One way to think about the rationalist project is as a combination of the following theses:

1. Semantic foundationalism holds that there is a canonical level of description that affords transparent epistemic access to an objective space of apriori possibilities – i.e. ways the world might be for all that can be known independently of all experience.
2. Meaning rationalism holds that implicit conceptual competence puts one in a position to conclusively know the applicability conditions of one’s words relative to every such scenario considered as actual.
3. Modal rationalism holds that the space of apriori epistemic possibility is a failsafe guide to the space of metaphysical possibility: there are no modal illusions when scenarios or worlds are described in canonical terms

Together, 1 and 2 constitute a sort of semantic reductionism: the meaning of any ordinary language expression is reduced to the meanings of the base vocabulary via the epistemic exercise of considering scenarios as actual and worlds as counterfactual. And 3 ensures that this epistemic exercise is an accurate guide to metaphysical possibility. Chalmers’ Core Thesis is meant to capture this tight relationship between grasp of meaning, apriori reflection, and metaphysical possibility.

However, simply rejecting C2D in favor of E2D does not yet provide any positive account of what it is to entertain an epistemic scenario W, and how we should update our beliefs in the light of the supposition that W is actual. Without these details, it’s impossible to determine whether the Core Thesis is true. Perhaps it’s impossible to consider a scenario as actual without presupposing one’s own existence, or perhaps our best epistemic methods for updating our beliefs presupposes the existence of those very beliefs; or perhaps there is no way of thinking about the world that doesn’t rely on some further empirical assumptions about the world.

Chalmers has entered into these interpretive questions in considerable detail over many publications. The starting point for his approach is outlined in (Chalmers and Jackson 2001)[^chalmers-2001], where he suggests that scenarios can be understood as PQTI sentences: where P states microphysical truths, Q states phenomenal truths, T is a ‘that’s all’ clause indicating that P and Q provide a complete description of a possible universe, and I indicates the subject’s notional location within that universe. P and Q employ a canonical vocabulary that fully specifies the essential nature of the fundamental properties upon which all other properties in a possible world supervene. Thus, PQTI sentences provide an epistemically transparent access to the space of epistemic and metaphysical possibility (simply removing the self-locating information from a PQTI sentence yields a complete description of a corresponding possible world, PQT). The 1-intensions of one’s ordinary language expressions are then determined by the individual subject’s ideally reflective dispositions to judge sentences true, assuming the truth of different PQTI-sentences. And 2-intensions are fixed by one’s reasoning about PQT sentences considered as counterfactual (given assumptions about PQTI). (Chalmers 2006, 2011b) further articulates how the space of epistemic possibility can be understood, how scenarios are related to possible worlds, and how 1- and 2-intensions are assigned to token representations.

More recently, in Constructing the World (2012), Chalmers has focused squarely on the epistemic ‘scrutability’ relation that connects our understanding of ordinary language expressions to base-level descriptions of scenarios.

Apriori Scrutability: There is a compact class of basic truths D such that for any truth S, one can conclusively know ‘D $\supset$ S’ apriori.

Chalmers still takes PQTI sentences to be a promising candidate for specifying a scrutability base D, but he is open to the possibility that the descriptive vocabulary in PQTI may need to be supplemented in order to capture some truths, such as truths about causal relations or quiddities. But while he can afford to be flexible about the exact nature of the scrutability base, Chalmers’ rationalist program depends on vindicating Apriori Scrutability for any sentence that is evaluable as possibly true or false (169–71). A good deal thus hangs on whether he is right that ideal epistemic procedures allow for apriori justification, given an exhaustive base-level description of a scenario. Chalmers offers arguments to support the plausibility of this view in (2012, ch. 4.).

According to the ‘frontloading’ argument, we can have conclusive apriori knowledge of material conditionals of the form (PQTI $\supset$ S). Chalmers argues that all empirical information relevant to justifying a verdict about S can be ‘frontloaded’ into the antecedent of the conditional, so information about one’s real-world environment, E, cannot play any essential role in justifying verdicts about the conditional. If E is itself apriori entailed by PQTI, it is not needed to justify a verdict about the conditional. And if E is not apriori entailed by PQTI, E will be irrelevant to justifying a verdict about the conditional. So our justification for the application conditionals that ground 1-intensions is wholly apriori, and immune to empirical defeat.[^note-20]

#### 2.3.4 Rationalist semantic values

Epistemic 2D semantics differs in important respects from traditional accounts of meaning. Semantic theories normally describe general semantic rules governing expression *types*, whereas epistemic 2D semantics is based on a single individual’s current understanding of a *token* expression. Kaplan and Jackson, for instance, use the 2D framework to characterize the implicit conventions governing syntactically individuated expressions like ‘I’ or ‘water’ in our linguistic community. In contrast, Chalmers uses the 2D framework to characterize your potentially idiosyncratic understanding of a particular use of an expression on a given occasion—e.g., the way you understood Al Gore’s fifth use of ‘water’ during a speech on climate change. Moreover, on this account 2D semantic values depend on the upshot of ideal rational reflection about apriori coherence relations. Just what is involved in ideal rational reflection is an open question. But it’s plausible that it may depend on substantive constructive theorizing about the empirical scenario in question and on various non-obvious and idiosyncratic aspects of the subject’s initial cognitive state. In that case, identifying the precise epistemic 1-intension associated with your understanding of ‘water’ will be a highly non-trivial matter, and it may be far from obvious when your understanding of the term shifts so that two tokens no longer share the same epistemic 1-intension. This is why, in contrast with 2D empiricists like Jackson, a rationalist like Chalmers denies that epistemic 1-intensions reflect the subject’s “implicit knowledge” of a reference-fixing criterion (e.g., Chalmers 2002a, 185; 2006b, §5)[^chalmers-2002a].

Of course, it’s possible that some epistemic intensions will reflect stable reference-fixing rules that are entrenched by implicit linguistic conventions. But it’s also possible that some epistemic intensions will reflect highly abstract, heterogeneous, unstable, and idiosyncratic aspects of a speaker’s understanding at a given time. As a consequence, epistemic intensions are not guaranteed to line up with conventional linguistic meanings (Chalmers 2002b)[^chalmers-2002b]. Given this divergence from standard semantic theories, one may wonder whether epistemic intensions deserve to be considered a kind of *meaning*.

However, according to the 2D rationalist, epistemic intensions play the core semantic roles associated with Fregean senses (Chalmers 2002b)[^chalmers-2002b]. Like Fregean senses, epistemic 1-intensions lend themselves to a compositional semantic theory: the epistemic intension of a sentence is determined by the epistemic intensions of the component expressions. Moreover, epistemic 1-intensions, like Fregean senses, reflect the speaker’s own rational perspective on what her words represent. Two token names ‘A’ and ‘B’ have the same Fregean senses iff the identity ‘*A = B*’ would strike the speaker as *trivially true*. Similarly, a subject associates two token expressions with the same epistemic intension iff they are *apriori equivalent*.[^note-21] Finally, epistemic intensions may play a role similar to that of Fregean senses in the semantics of attitude reports (Chalmers 2011a)[^chalmers-2011a]. Overall, then, epistemic intensions seem to provide an attractive theoretical refinement of the Fregean notion of sense.

In addition, epistemic intensions arguably carve out a well-defined notion of narrow content suited to playing key roles in commonsense psychology (Chalmers 2002c)[^chalmers-2002c]. Epistemic intensions reflect rational relations among token mental states. Epistemic intensions can then be used to specify representational state types that are relevant to assessing a person’s rationality and to explaining rational thought processes.

It’s important to note that epistemic 1-intensions are intended to explain only *one aspect* of meaning. The 2D semantic framework also posits 2-intensions (“counterfactual” or “subjunctive” intensions), which reflect the modal profile of the object, kind or property picked out by an expression. But Chalmers emphasizes that his E2D does not exclude positing further aspects of meaning:

> Two-dimensionalism is naturally combined with a *semantic pluralism*, according to which expressions and utterances can be associated with many different semantic (or quasi-semantic) values, by many different semantic (or quasi-semantic) relations. On this view there should be no question about whether the primary intension or the secondary intension is *the* content of an utterance. Both can be systematically associated with utterances, and both can play some of the roles that we want contents to play. Furthermore, there will certainly be explanatory roles that neither of them play, so two-dimensionalism should not be seen as offering an exhaustive account of the content of an utterance. Rather it is characterizing some aspects of utterance content, aspects that can play a useful role in the epistemic and modal domains. (Chalmers 2006a, §3.5)[^chalmers-2006a]

In sum, Chalmers’ highly idealized E2D framework is intended to earn its semantic keep by defining a kind of meaning capable of forging traditional rationalist connections between meaning, rationality and possibility. But he is happy to allow that there may be other types of semantic values or structures that are needed to play other semantic roles. [See entry on propositions, and structured propositions.]

### 2.4 Objections to generalized 2D semantics

The G2D framework has attracted a wide variety of criticisms, targeting its commitment to apriori conceptual analysis, its claim that 1-intentions capture a type of meaning, and its internalist approach to assigning contents. The specific rationalist and empiricist applications of the G2D framework have also been criticized. For a survey of these lines of criticism: see the supplementary document:

> *[Objections to generalized 2D semantics](two-dimensional-semantics.objections-2d.md)*

## 3. The Metasemantic Interpretation

### 3.1 2D semantics for externalists

Generalized 2D semantics seeks to vindicate a traditional internalist conception of meaning: it posits an extra aspect of meaning for all expressions (the intension corresponding to the diagonal of a 2D matrix) that is fully determined by a subject’s internal states, and which in turn determines objective truth-conditions for their sentences. By enriching compositional semantics in this way, G2D promises a straightforward explanation of a variety of epistemic properties of sentences: e.g., why a necessary sentence like ‘Hesperus is Phosphorus’ is not apriori knowable, what the subject learns by accepting the sentence, or how the subject uses the sentence in reasoning.

But using the 2D framework to characterize the subject’s epistemic perspective is not beholden to this internalist project. Semantic externalists reject the traditional view that our purely internal states afford apriori access to reference-fixing conditions for our words and thoughts. According to externalists, the basic assignments in a compositional semantics relate the subject’s words and thoughts to objective features of her environment—objects, kinds and properties whose nature is captured by standard (1D) possible world semantics. Even externalists, however, can define 2D matrices that reflect the subject’s epistemic perspective on the reference of her words and thoughts. For the externalist, however, these 2D matrices will not represent *meanings*—a specific aspect of understanding that is required for linguistic or conceptual competence and which figures in a compositional semantic theory that determines truth-conditions for sentences. On an externalist interpretation, 2D matrices merely reflect one aspect of a subject’s *partial semantic understanding* of what her words and thoughts represent. Because externalist 2D matrices don’t represent meanings, moreover, the externalist is free to use the 2D framework strategically to focus on different aspects of the subject’s understanding for different explanatory purposes.

Robert Stalnaker has articulated such an externalist interpretation of the 2D framework in a series of influential papers spanning some thirty years. He was the first to introduce 2D matrices to specify what is communicated in situations where conversational partners are partly ignorant or mistaken about the nature of the objects, kinds or properties their words pick out (1978), and he later extended his 2D framework to characterize the content of certain thoughts and attitude attributions (1981; 1987; 1988). In both cases, the 2D framework is used to define “diagonal” intensions that reflect the subject’s partial understanding of which objects, kinds or properties her words and thoughts represent. These diagonal intensions are not meanings or semantic values, since they do not figure in a compositional semantic theory and they do not reflect conditions for conceptual or linguistic competence. The only meaning of an expression on this account is its ordinary “horizontal” intension. In effect, Stalnaker’s 2D matrices represent different meanings that an expression *could have had* if it had occurred in different empirical circumstances. This “metasemantic” interpretation of the 2D framework contrasts sharply the “semantic” interpretations favored by G2D theorists like Jackson and Chalmers (Stalnaker 2001, 2004)[^stalnaker-2001].

Proponents of G2D were influenced by Stalnaker’s early papers developing the 2D framework, and their views are often presented as continuous in motivation and form. But there are important theoretical consequences that flow from the choice between 2D metasemantics and generalized 2D semantics. Indeed, Stalnaker himself is a vocal critic of generalized 2D semantics, rejecting its commitment to the semantic status of 2D matrices, its commitment to apriori conceptual analysis, and its internalist approach to reference determination.

### 3.2 A 2D account of assertoric content

The metasemantic interpretation of the 2D framework was originally developed as a way of explaining how the propositions conveyed by the assertion of a sentence can vary depending on the conversational context (Stalnaker 1978)[^stalnaker-1978]. In this seminal paper, Stalnaker proposes an attractive theoretical account of the role of assertion in a conversation, which is then used to explain how the assertoric use of a necessary sentence like ‘Hesperus = Phosphorus’, can convey a specific empirical proposition within a given conversation. In particular, Stalnaker argues that our commitment to construing such sentences as making felicitous and informative assertions will lead us to *reinterpret* their content in ways that can be modeled using the 2D framework.

The guiding idea is that in making an assertion the speaker is trying to get the audience to rule out certain possibilities. In asserting ‘It’s cold today’, for instance, I may be trying to get you to rule out possibilities in which today’s temperature in Melbourne is over 10° C. We can model what my assertion conveys, then, as a function that maps possible worlds in which today’s temperature is under 10° C to True and all other worlds to False. However, the precise truth-conditions communicated by an assertoric use of a sentence depend in part on the conversational context in which it takes place. Just which temperatures count as cold, for instance, depends on shared background assumptions in a particular conversational context: what’s cold in Melbourne is mild in Manitoba.

A second guiding idea is that the proposition actually conveyed by the assertion of a particular sentence depends on *presuppositions* shared by the participants in the conversation—including presuppositions about what particular words represent and presuppositions about actual empirical circumstances. If you’re a Chinese speaker who doesn’t understand anything at all about what the term ‘cold’ represents in English, then I cannot use ‘It’s cold today‘ to convey facts about Melbourne’s weather. And if you’re a Canadian who doesn’t understand anything about Australian weather conditions, you won’t understand precisely what I am saying to my fellow Melburnians when I assert that sentence. Stalnaker calls the set of presuppositions that conversational partners treat as common knowledge that they can rely on to get their point across the “context set”—which he models as the set of possible worlds that satisfy all of these mutual presuppositions. The context set will encode shared assumptions about the meaning of words, about general empirical facts, about the what’s happened so far in the conversation, and so on.

The goal of assertion, Stalnaker suggests, is to shrink the context set. In making an assertion, the speaker tries to get the audience to accept a new proposition as one of their shared presuppositions, thereby shrinking the set of possible worlds that are considered live options. For instance, in asserting ‘It’ll be very cold today’ to a group of Melburnians, I exploit background knowledge of local weather conditions in June to get my audience to accept that the temperature outside is somewhere between 5–10° C, ruling out live possibilities that it might be in the 15–20° C range. If all goes well, further planning will proceed on the basis of a smaller and more accurate range of possibilities. In contrast, if I were to assert ‘It’s cold’ to the monolingual Chinese speaker or to the parochial Canadian, my assertion would be defective, since my audience wouldn’t be able to figure out which temperatures are ruled out by my assertion.

Identity claims, however, do not seem to fit this simple model of assertion. As Kripke (1980) argued, identities are either necessarily true or necessarily false. So accepting an identity will either leave the context set unchanged or it will eliminate it altogether. Either way, asserting an identity would be pointless. But clearly it is not. Asserting an identity such as ‘Lloyd is I.L. Humberstone’ can be genuinely informative, ruling out empirical possibilities previously taken to be live options. According to the metasemantic account, (i) the goal of assertion can explain why the assertion of a necessary sentence will lead to a reinterpretation of the content of the asserted sentence, and (ii) the 2D framework helps to specify just which proposition will be conveyed by the sentence within a given conversation.

In general, an identity claim is appropriate when one of the parties to a conversation is (partially) ignorant about which object is picked out by a name like ‘Lloyd’. For an externalist like Stalnaker, this is a case of *semantic ignorance*. If O’Leary doesn’t know that ‘Lloyd’ is co-referential with ‘I.L. Humberstone’, then he does not fully understand the semantic rules governing these names: i.e., that both names are associated with a constant function from any possible world to a specific individual. But O’Leary isn’t utterly incompetent with the meaning of these terms: he implicitly understands both names as rigid designators, and he has some substantive understanding of the object each name picks out. For instance, he may understand that ‘Lloyd’ refers to the person to whom he’s just been introduced and that ‘I.L. Humberstone’ refers to the author of ‘Direction of Fit’. O’Leary’s semantic deficiency—his failure to fully understand the meaning of these names in a contextually appropriate way—is grounded in his ignorance of the ordinary empirical fact that the man to whom he has been introduced is the author of ‘Direction of Fit’.

2D matrices can be used to represent this sort of partial semantic understanding. O’Leary knows that $if$ the man in front of him is the author of the famous article, then ‘Lloyd = I.L. Humberstone’ expresses a necessary truth; and he knows that $if$ the man in front of him isn’t the author, the sentence expresses a necessary falsehood. What O’Leary doesn’t know is which of these two possibilities corresponds to his actual situation. Call the first possibility i and the second j. O’Leary’s epistemic situation can then be summed up in a 2D matrix:

O’Leary: ‘Lloyd = I.L. Humberstone’

|   | i | j |
| --- | --- | --- |
| i | T | T |
| j | F | F |

The matrix is defined only with respect to a specific set of relevant alternative possibilities, i and j, chosen in such a way as to reflect the subjects’ semantic understanding and our own explanatory interests. The vertical axis represents these possible worlds in their role as *contexts of use*, which determine the literal semantic content of the expressions used in them. The horizontal axis represents those same possible worlds as *circumstances of evaluation*, relative to which we evaluate the truth or falsity of the proposition expressed. Each row of the matrix thus represents a different proposition that might be literally expressed by the sentence. Stalnaker calls such matrices *propositional concepts*, since they reflect the subject’s current imperfect conception of the meaning of the sentence.[^note-22] This particular matrix reflects the fact that O’Leary’s current epistemic state is compatible with the identity sentence expressing either a necessary truth or a necessary falsehood, depending on empirical facts about the actual context of use.

What does O’Leary learn when he comes to accept Daniels’ assertion of ‘Lloyd is I.L. Humberstone’? Since the actual world is like i, the literal semantic content of the asserted sentence is a necessary truth. But necessary truths rule out no empirical possibilities whatsoever, so this cannot be the informative proposition that is conveyed by Daniels’ assertion. Moreover, O’Leary is not in a position to recognize that this is the literal semantic content of the sentence, since he doesn’t know whether the actual world is like i or j. The natural suggestion is that the information conveyed by Daniels’ assertion is that the real world is like i and not j. When O’Leary accepts ‘Lloyd is I.L. Humberstone’, he will no longer treat the possibility that the man in front of him is *not* the author of the famous article as a live option: this empirical possibility will be eliminated from his context set. Thus, the proposition that seems to be conveyed by Daniels’ assertion corresponds to the diagonal intension determined by our 2D matrix for that assertion. Moreover, this observation generalizes: when subjects are partially ignorant of the semantic values of their words, the diagonal proposition determined by the propositional concept can capture the empirical information conveyed by the assertion.

But why is this so? To explain why assertions sometimes express the diagonal proposition, the metasemantic account appeals to rational maxims governing conversational cooperation. The following maxim seems to govern the practice of assertion:

> The very same proposition should be expressed relative to every possible world in the context set. (Stalnaker 1978, 88)[^stalnaker-1978]

Speakers should conform to this maxim, because assertion involves an intention to get one’s audience to eliminate worlds from the context set in accordance with the proposition expressed—and in order for this intention to succeed the audience must be in a position to figure out just which worlds they are being asked to eliminate. When this sort of rational maxim governing the communication of information is flouted, the audience will look for a non-standard interpretation of the utterance that would bring it back into conformity with the maxims (Grice 1989)[^grice-1989]. [See the entries on pragmatics and on implicature.]

According to Stalnaker, this is precisely what is going on in the case of identity claims like the one we have been considering. Daniels’ assertion of ‘Lloyd is I.L. Humberstone’ clearly flouts the proposed maxim. We can assume that Daniels is aware that O’Leary doesn’t know whether he is in a world like i, where the man to whom he’s been introduced is the famous author, or a world like j where they are distinct. Yet Daniels utters a sentence that expresses a different proposition depending on whether the actual world is like i or like j. In such circumstances, the audience should look for an alternative interpretation of the assertion. Daniels’ assertion can be brought back into conformity with the maxim by re-interpreting it as conveying the proposition expressed by the diagonal of the matrix. At a rough intuitive level, we can say that Daniels is trying to get O’Leary to accept that the sentence ‘Lloyd is I.L. Humberstone’ expresses a truth. But the 2D framework also allows us to specify more precisely just what empirical information is conveyed within a given conversational context. Given O’Leary’s and Daniels’ common presuppositions about what the two names represent, Daniels’ assertion also expresses the proposition *that the man to whom O’Leary has just been introduced is the author of ‘Direction of Fit’*.

It’s worth emphasizing, however, that the very same sentence asserted in a different conversational context could express an entirely different empirical proposition: just which proposition is expressed, on this metasemantic account, depends on what the individual parties to the conversation are currently presupposing about the meanings of the expressions used.

In recent work, Stalnaker has enriched his notion of a context. In addition to a sets of possible worlds, he introduces (i) multiple centers within those worlds representing the participants in a conversation, and (ii) accessibility relations among the centers representing interlocutors’ ways of identifying each other (Stalnaker 2008, 2014)[^stalnaker-2008]. This added structure is intended to capture self-locating presuppositions that can help explain what’s communicated by indexical expressions like ‘I’, ‘you’ and ‘now’. For a helpful overview of the motivation for such an approach, see (Ninan 2010a)[^ninan-2010a] and for further development of multi-centered accounts of propositional content see (Torre 2010, Ninan 2013)[^ninan-2013][^torre-2010].

### 3.3 Propositional attitudes

The metasemantic 2D framework was originally developed to explain communication, but the framework can also be used to specify the content of certain beliefs and the content of assertions that attribute beliefs.

Stalnaker (1984) defends a coarse-grained account of belief contents, which individuates particular belief states in terms of a set of possible worlds that would make them true. If this project is to succeed, it must be possible to fully specify beliefs without invoking anything like Fregean senses or conceptual structure. But there is an important class of beliefs that seem to pose insuperable problems for a simple possible worlds account of their content: beliefs in necessary truths. The problem for a standard possible worlds analysis is that all necessary truths have precisely the same content (the function mapping every world to True). So the belief *that Hesperus = Phosphorus* will have exactly the same content as a belief *that Hesperus = Hesperus & Fermat’s last theorem is true*. But these are clearly distinct belief states. Beliefs in identities have been particularly important in motivating theories of finer-grained thought contents.

But fine-grained Fregean senses or conceptual structures are not strictly required to distinguish beliefs in identities. Stalnaker (1981; 1987) argues that the metasemantic 2D framework he developed to explain what is communicated by an *assertion* of an identity sentence can also explain the content of the *belief states* attributed using an identity sentence to specify its content. If O’Leary were to notice the pole star and think to himself *that’s Mars*, for instance, the truth-conditions of his thought can be captured by a judiciously defined diagonal proposition (Stalnaker 1987, 125)[^stalnaker-1987]. In this case, the worlds we include in the context set may involve facts about which object is the target of O’Leary’s visual attention and facts about salient empirical properties he associates with the name ‘Mars’. On the metasemantic approach, then, the proposition we attribute in saying O’Leary believes that *that is Mars* is the proposition that the visually salient object is the object that has those Martian properties.

A further complication arises in specifying the content of attitude attributions. On the metasemantic account of assertion, the content conveyed by a sentence depends on the shared presuppositions of the speaker and audience. But sometimes the parties to a discussion are better informed than the person they are describing. In philosophical discussions, for instance, it is standardly presupposed that ‘Hesperus’ and ‘Phosphorus’ are co-referential. So the diagonal intension associated with the sentence ‘Hesperus $\ne$ Phosphorus’ will be *necessarily false* when it’s asserted in philosophical contexts (i.e., it will be false when uttered in any situation compatible with what is being presupposed in the philosophical conversation). And yet when a philosopher says that O’Leary doesn’t know that Hesperus is Phosphorus, she still manages to communicate that O’Leary fails to grasp some contingent empirical proposition. On the face of it, the metasemantic account of assertion cannot explain how this is possible, since every cell of the metasemantic matrix for the identity claim in this philosophical conversation will be assigned the value True.

Stalnaker’s response to this problem is to suggest that the context set for a belief report must be expanded so as to include worlds that correspond to the way that the believer himself (i.e. O’Leary) takes things to be. The diagonal proposition of the philosopher’s sentence is thus determined by considering what she would be saying if her sentence were asserted in contexts compatible with O’Leary’s beliefs (1987; 1988). However, there is no general rule for choosing which worlds are the relevant ones:

> The procedure I am proposing for extending propositional concepts so that the diagonalization strategy can be applied to problematic belief attributions takes examples case by case. It is not, as yet, very satisfactory if we are looking for a systematic way to explain why the complements of belief attributions denote the propositions that they seem to denote. But if, using this procedure, we can find a possible worlds proposition that is a plausible candidate to be the object of belief being attributed in the various problematic examples, then […] it will not be completely mysterious how these propositions can be expressed by the sentences that seem to express them. (Stalnaker 1987, 129)[^stalnaker-1987]

Thus, the metasemantic 2D framework provides adequate descriptive resources for characterizing mental states and our discourse about them, without invoking fine-grained Fregean senses, concepts, or syntactic structures. However, the metasemantic theory used to construct the relevant 2D matrices relies on unsystematic norms of charitable interpretation to identify the precise contents of particular attitudes and attitude reports (Stalnaker 1999b, 18–19)[^stalnaker-1999b].[^note-23]

### 3.4 Metasemantic vs. semantic

The semantic vs. metasemantic distinction was first drawn by Kaplan (1989b, 573–6). A semantic theory for a language assigns semantic values (meanings) to particular expressions in the language. In contrast, a metasemantic theory explains *why* expressions have those semantic values: i.e., what facts about an expression make it the case that it has a certain meaning. A semantic theory, for instance, might tell us that the semantic value for ‘Barack Obama’ is a 1D intension that maps any possible world to a specific individual, while the semantic value for ‘I’ is a 2D intension that maps contexts of use (centered worlds) to a constant function from any possible world to the individual who is the speaker in the context. A metasemantic theory will tell us what makes it the case that these are the correct interpretations of their meaning: e.g., the metasemantic theory might appeal to the speaker’s dispositions and history, how she is causally connected to her social or physical context, the linguistic conventions of the local linguistic community, details about the conversational context, and so on.

A *semantic interpretation* of the 2D framework takes the 2D framework to specify a semantic value of an expression. Kaplan’s theory of indexicals is a semantic interpretation of the framework, as are Jackson’s and Chalmers’ generalized 2D semantics. Stalnaker calls his own interpretation of the 2D framework a *metasemantic* one because his 2D matrices reflect general principles for assigning semantic values (horizontal intensions) to expressions on the basis of empirical facts about their use. Stalnaker’s 2D matrices thus reflect metasemantic facts about interpretation, not semantic facts about the meanings of specific expressions.

The metasemantic interpretation of the 2D framework is structurally different from semantic interpretations like Jackson’s and Chalmers’ in a number of important respects. First, on the metasemantic approach, 2D matrices are defined in terms of a restricted set of possible worlds. Metasemantic 2D matrices are defined only with respect to those worlds that are consistent with some relevant set of the subject’s background assumptions. On a semantic interpretation, in contrast, 2D matrices are defined on the set of *all* centered possible worlds.

Second, just which set of possible worlds is used to construct a metasemantic 2D matrix depends in part on the *theorist’s* contingent explanatory interests. For instance, Daniels’ current internal state of understanding the expression ‘Mars’ may be associated with different 2D matrices, depending on whether we are interested in characterizing his conversation with O’Leary or in characterizing his thought identifying a speck visible in the night sky as Mars. In many contexts, moreover, we can characterize the content associated with Daniels’ internal state without resorting to the 2D apparatus at all: e.g., when Daniels asserts ‘Mars is a planet’ we can usually model what he says and thinks in terms of a simple horizontal intension. Semantic interpretations of the 2D framework treat the intension corresponding to the diagonal of a 2D matrix as fully determined by the subject’s internal states, whereas on a metasemantic approach which diagonal intension is assigned—or whether a diagonal intension is invoked at all—depends on the explanatory interests of an interpreter.[^note-24]

Third, the assignment principle used to fill in a metasemantic 2D matrix for a subject’s words is not beholden to an internalist account of reference-fixing. On a semantic interpretation, 2D matrices are filled in on the basis of the subject’s idealized judgments about hypothetical scenarios. But the metasemantic approach is not committed to relying on the subject’s epistemic judgments to fill in 2D matrices: it’s the *theorist* who must be able to assign horizontal intensions to a subject’s words and thoughts on the basis of the totality of empirical facts about that subject. Nor should we think of reference-fixing as somehow determined by the internal states of the theorist, since even theorists are prone to mistakes on externalist accounts of reference-fixing.

Fourth, on the metasemantic approach, the basic semantic assignments are always horizontal intensions, which reflect the nature of the objects, kinds and properties the subject is thinking and talking about. On a metasemantic account, diagonal intensions represent *ad hoc reinterpretations* that we resort to when the normal horizontal intension for a subject’s sentences or thoughts is necessarily true or necessarily false, and hence makes no substantive claim about the empirical world. Such diagonal intensions, moreover, are theoretical abstractions *derived* from a set of horizontal intensions that are compatible with the subject’s partial ignorance about nature of the objects, kinds, and properties she is representing (i.e., her partial ignorance of the horizontal intensions for her words and thoughts). Semantic interpretations of the 2D framework, in contrast, treat the intensions picked out by the diagonal of a 2D matrix as basic semantic values in their own right.

As a consequence of these structural features of the metasemantic interpretation, metasemantic diagonal intensions play none of the basic explanatory roles attributed to 1-intensions by proponents of generalized 2D semantics. In particular, (i) diagonal intensions do not figure in a compositional semantic theory, (ii) they do not reflect stable aspects of linguistic or conceptual competence, and (iii) they do not represent apriori accessible reference-fixing conditions for the subject’s words or thoughts (Stalnaker 1999b, 2004 , 2007)[^stalnaker-1999b].

The metasemantic interpretation use of the 2D framework has come in for criticism on a number of fronts. For a brief survey, see the supplementary document:

> *[Objections to the metasemantic interpretation](two-dimensional-semantics.objections-meta.md)*

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=two-dimensional-semantics). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/two-dimensional-semantics/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=two-dimensional-semantics&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/two-dimensional-semantics/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [“Two-Dimensional Semantics”](https://iep.utm.edu/2d-seman/), 2018, Jens Kipper, *Internet Encyclopedia of Philosophy*, includes an annotated bibliography.
- [“Two-Dimensional Semantics”](http://consc.net/papers/twodim.pdf), 2006, David Chalmers (manuscript version of Chalmers 2006b)[^chalmers-2006b]: compares the most influential interpretations of two-dimensionalism, and outlines and defends the epistemic interpretation.
- [“Two-Dimensional Semantics—the Basics”](https://uni-bielefeld.com/fakultaeten/philosophie/personen/nimtz/papers/pbu03_Nimtz_2007_2dSemanticsLong.pdf), 2007, Christian Nimtz: a concise overview that compares Kripke, Kaplan, Stalnaker and Chalmers.
- [“Varieties of Two-Dimensionalism”](http://www.jimpryor.net/research/notes/Varieties2D.pdf), 2003, Jim Pryor: a somewhat more technical discussion explores different ways of interpreting 2D matrices.

## Related Entries

*a priori* justification and knowledge | descriptions | experimental philosophy | externalism about the mind | hyperintensionality | indexicals | logic: intensional | logic: modal | meaning, theories of | meaning: of words | mental content: causal theories of | mental content: narrow | modality: epistemology of | modality: varieties of | multi-modal logic, philosophical aspects of | names | physicalism | possible worlds | pragmatics | propositional attitude reports | propositions | propositions: singular | propositions: structured | rationalism vs. empiricism | reference | rigid designators | situations: in natural language semantics | supervenience | zombies

### Acknowledgments

Many thanks to David Chalmers, Lloyd Humberstone, Frank Jackson, Robert Stalnaker and an anonymous referee for very helpful feedback on this entry.

## Notes（原文脚注）

## Notes to Two-Dimensional Semantics

[^note-1]: There are two standard ways of interpreting rigid designation, both of which are consistent with Saul Kripke’s original introduction of the term (1970 lectures, published 1980). On the first interpretation, a name rigidly designates a given object *at every world in which that object exists*, and it fails to designate anything at worlds in which the object does not exist. On the second interpretation, a name rigidly designates a given object at every world *regardless of whether the object exists in that world*. For present expository purposes, we’ll rely on the latter interpretation.

[^note-2]: An object’s *modal profile* or *nature*, in this sense, should be distinguished from its essential properties. A modal profile (or nature) captures all the possible combinations of properties the object might instantiate in different possible worlds. In contrast, the object’s essential properties are the specific subset of properties (if any) that the object must have in every world in which it exists. Standard possible world semantics can be used to capture the modal profile associated with ‘Roger Federer’ by first assigning an intension to the name which maps every possible world onto a particular individual, RF, and then providing the resources for determining, of any given predicate, ‘P’, whether there is a possible situation in which RF exemplifies the property picked out by that predicate. The complete modal profile of RF can be made explicit by surveying all the different combinations of properties RF exhibits in the possible worlds in which he exists.

[^note-3]: Kaplan’s essay is based on a series of lectures delivered in 1971.

[^note-4]: This way of representing possible contexts presupposes that the agent exists at the designated time. This is known as a “proper context”, and it reflects the empirical facts available for interpreting actual utterances. But some theorists work with a weaker notion of context, which allows for arbitrary combinations of agents, spatio-temporal locations, and worlds. This weaker notion of context can help represent how we interpret indexical utterances, like a recording of ‘I am not here now’ on an answering machine, when the agent is not located at the time and place of the utterances (Predelli 1998)[^predelli-1998].

[^note-5]: The sentence counts as a logical truth in Kaplan’s 2D framework because logical validity is defined only on *proper* contexts, in which the designated agent is located at designated time and place in the world of the context (1989a, 544: clause 10, 547: remark 3).

[^note-6]: What is the semantic role of the logical operator, ‘Fixedly’ (‘$\mathcal{F}$’), considered on its own? Borrowing formalism introduced by (Davies and Humberstone 1980)[^davies-1980], we can say that a sentence is always evaluated with respect to an ordered pair of possible worlds, $\langle w_x, w_y\rangle$, where the first member of the pair represents the world designated as actual and the second represents a circumstance of evaluation. A sentence S is *fixedly true at $w_n$*, iff S is true with respect to every ordered pair $\langle w_x, w_n\rangle$, where we allow the $w_x$ to vary arbitrarily. (Graphically, a sentence S will be Fixedly true at $w_n$ just in case the entire (vertical) column corresponding to $w_n$ in a 2D matrix contains ‘True’ all the way down.) In effect, the Fixedly operator tells us about what must be true with respect to a specific world considered as counterfactual, no matter which world is designated as actual. When we combine the operators ‘Fixedly’ and ‘Actually’ (‘$\mathcal{F}\mathcal{A}$’), the complex operator behaves like a *necessity operator ranging over possible worlds playing the actual world role*. A sentence is fixedly actually true just in case it is *true at the designated world* no matter which world is so designated. So a sentence is fixedly actually true iff it is true with respect to every ordered pair $\langle w_x,w_x\rangle$, where the value of $w_x$ is allowed to vary arbitrarily. (Graphically, S will be fixedly actually true iff the diagonal of the 2D matrix contains ‘True’ all the way down.)

[^note-7]: Notice that, unlike Kaplan, Crossley and Humberstone do not think of the possible worlds ranged along the vertical axis of the 2D matrix as *possible contexts of use*. On their 2D framework, the worlds “considered as actual” are just *arbitrarily designated* as the reference of the term ‘actually’ for the purposes of modeling the behavior of ‘actually’ within the scope of operators like ‘necessarily’ or ‘possibly’. Thus, their 2D semantics does not explain how the significance of the natural language expression ‘actually’ is affected by the context in which it’s used, only how the term interacts with other modal operators.

[^note-8]: The semantic rules governing ‘actually’ allow us to know the definitions given in (i) and (ii) are true no matter which world is actual (i.e. they are fixedly actually true). According to (i), *whoever* invented the zip (whether it was Mary Anne Evans or Whitcomb Judson), that person is Julius. Since you know that (i) is true no matter which world is actual, you can know that it’s true on the basis of apriori reasoning alone. But still, (i) does not reflect the modal profile of Julius: Whitcomb Judson (the real inventor of the zip) could have died in infancy. So the definition in (i) does not ensure that the claim is necessary in the sense of the standard modal operator, ‘$\Box$’. In contrast, the true identity claim ‘Julius = Whitcomb Judson’ is necessary in this sense, since both names rigidly designate the same individual in all possible worlds. But the semantic rule in (i) does not allow us to know this identity is true: we need to conduct some empirical investigation to find out who the inventor was. Similar observations follow from the definition of ‘water’ in (ii).

[^note-9]: Some theorists push the argument further, arguing that the potential for ignorance and error highlighted by externalist examples generalizes to other types of expression, such as artifact terms (‘pencil’, ‘sofa’), conventional kinds (‘arthritis’, ‘fortnight’), or even logical expressions (‘not’, ‘every’) (Putnam 1972; Burge 1979; Williamson 2007)[^burge-1979][^putnam-1972][^williamson-2007].

[^note-10]: Kripke’s book is based on a series of lectures delivered in 1970.

[^note-11]: Jackson emphasizes that his account of meaning is *not* intended to explain thought contents (1998b; 2004). The reason for this is simple: the account posits implicit conventions that require individual speakers to associate a word with specific reference-fixing assumptions about the object, kind or property in question. The account thus presupposes an independent explanation of the content of these thoughts. Moreover, it’s hard to see how anything like linguistic conventions could apply to thought contents directly: since we don’t seem to have any way of focusing on our own mental representations independently of our understanding of their contents, it’s implausible that we could establish conventions requiring thinkers to associate some pattern of understanding with a given mental representation.

[^note-12]: It’s worth noting that Jackson is not committed to any particular interpretation of the possible worlds that define his 2D framework. Jackson’s 2D framework is just a tool for testing one’s current understanding of how two different vocabularies relate to each other, and cataloguing the resulting information in a perspicuous way. The goal is to identify conditions, specified in some base vocabulary, that one takes to suffice for the applicability of a given target expression. For these purposes, *any* vocabulary can be used to describe hypothetical cases, as long as it provides enough information for the speaker to be confident in applying the target expression. The fact that Jackson sometimes takes the commitments of a sophisticated proponent of physicalism as his primary example may obscure this point, suggesting that the possibilities that define the 2D framework should always be couched in the language of idealized physics. But it’s important to keep in mind that the empiricist theory of meaning is supposed to characterize actual linguistic competence—a psychological and social phenomenon—not to characterize the nature of reality. So, in contrast to the rationalist project, the empiricist project needn’t posit an idealized vocabulary that can exhaustively specify all possible worlds.

[^note-13]: It’s worth noting that indirect reference-fixing is also possible when the nature of the reference can be discovered through apriori reflection—and in such cases the difference between reference-fixing criteria and theoretical criteria will not correspond to different A- and C-intentions. Jackson and Pettit’s ‘moral functionalism’ is a case in point: the reference of moral terms is allegedly fixed by a variety of superficial properties (e.g. killing is normally wrong, people are normally motivated to do what they judge right, etc), but these properties do not constitute the ultimate theoretical characterization of the properties picked out by moral terms. The fact that you don’t realize that your term ‘morally right’ picks out a rule-utilitarian property (let’s say) may be due to a failure of apriori reflection rather than lack of empirical knowledge of your environment (Jackson 1998a, ch. 5 & 6; Jackson and Pettit 1995)[^jackson-1998a][^jackson-1995].

[^note-14]: N.B., the rationalist is not committed to the idea that a 2D semantic framework accounts for *all* aspects of meaning: in particular, further aspects of meaning may be required to account for differences in content between apriori equivalent claims. See the discussion of semantic pluralism in 2.3.3 below.

[^note-15]: According to a modal rationalist like Chalmers, the primary job of modal notions like *possibility* and *necessity* is to keep track of apriori consistency relations among semantic contents. To fulfill this explanatory role, the rationalist posits a “logically possible world” for every apriori conceivable way the world might be. Chalmers thinks that critics of modal rationalism should concede (i) that this notion of logical possibility is an important and useful one for keeping track of consistency among thought contents and (ii) that *at least some* logical possibilities represent genuine metaphysical possibilities. The debate over the truth of modal rationalism would then hinge on whether *every* logically possible world is also metaphysically possible. Put graphically: is the space of metaphysically possible worlds a proper subset of the space of logically possible worlds? Chalmers argues that any way of demarcating metaphysical from logical possibilities would constitute “an *ad hoc* proliferation of modalities” which posited a second “brute and inexplicable” modal primitive. So we should accept a single space of possibility, in which every apriori coherent hypothesis represents a genuine metaphysical possibility (1996, 136­-8; 1999, 488–91).

[^note-16]: Chalmers introduces the term ‘1-intension’ as a way of talking about the various different kinds of intension that correspond to the diagonal of a 2D framework. Strictly speaking, therefore, it makes no sense to talk about *the* 1-intension of a particular expression without further ado, since the notion of a 1-intension is defined purely in terms of the formalism. To obtain a specific 1-intension for an expression, we need to *interpret* the 2D framework by specifying the possibilities relative to which extensions are assigned and explaining the principles for assigning extensions. Chalmers’ Core Thesis doesn’t appeal to any specific interpretation of the 2D formalism, instead it is intended as a constraint on how the framework should be interpreted if it is to vindicate the rationalist conception of meaning. (Similarly, Chalmers introduces the term ‘2-intension’ to pick out *the first horizontal row* of a 2D matrix, regardless of how exactly the 2D formalism is interpreted. In any 2D framework, the first row assigns an intension relative to the actual world considered as actual. So an expression’s 2-intension will correspond to the kind of intension posited by standard possible world semantics.)

[^note-17]: Chalmers notes a further dialectical problem in appealing to contextualist 2D semantics to vindicate rationalism (2004, 2006a). In order to generate a 1-intension, a contextualist must specify which properties of an utterance are held fixed in every possible context of use. Very different contextual 1-intensions will be generated for your term ‘I’, for instance, depending on whether we require that the target utterance of ‘I’ be *spelled* a certain way in every context or if we instead require that it be *understood* a certain way by the agent of the context. A contextualist 1-intension based on spelling will not capture any interesting notion of meaning: depending on how it’s used and understood in a context, the string ‘I’ may pick out apples, Antarctica, arguments, or anything else. So if contextualist 1-intensions are to capture a kind of meaning, we will need some independent way of identifying those properties of an expression that, if held fixed, guarantee sameness of meaning. In the case of indexicals like ‘I’ this requirement is not too onerous, since there are conventional linguistic rules for identifying the extension in a context that all competent speakers readily acknowledge. But in the case of names or natural kind terms, it is highly controversial whether there are any conventional linguistic rules, except the aposteriori rules that link these expressions directly to their 2-intensions. So contextualist 2D semantics by itself does nothing to allay skepticism about the existence of rationalist meanings for expressions like names and natural kind terms.

[^note-18]: Chalmers leaves the door open for weaker ways of understanding epistemic possibility. For instance, he suggests that one might define epistemic possibilities in terms of whether a sentence (or set of sentences) seems coherent after a specified amount of “cognitive work”. However, Chalmers takes the notion of ideal apriori coherence to be the most principled sense of epistemic possibility, and the one that underwrites our access to metaphysical modality (2002b).

[^note-19]: Chalmers is neutral about a more substantive analysis of scenarios. He sketches three different approaches: (i) scenarios might be identified with centered possible worlds, (ii) scenarios might be identified with sets of apriori coherent sentences in an idealized language, or (iii) scenarios might be taken as epistemic primitives. As a modal rationalist, he takes these analyses to be extensionally equivalent, but he argues that the different options have important consequences for how the 2D framework is elaborated (2004, 2006a).

[^note-20]: It’s worth noting that there are other ways of interpreting an E2D framework defined on epistemic and metaphysical possibilities, which do not support Chalmers’ rationalist program. Some advocates of E2D have suggested that we have *defeasible*, rather than *conclusive* apriori access to application conditionals (Kipper 2012, 39–40; Biggs and Wilson 2020, 69)[^biggs-2020][^kipper-2012]. But as Wittmer (2013) points out, defeasible judgments will not suffice to fix the semantic facts about 1-intensions. So these interpretations must be construed as accounts of our epistemic access to independently determined semantic facts. Other theorists take scenarios to be a space of objective metaphysical possibilities, which need not be epistemically transparent to individuals. Wolfgang Spohn, for instance, likens scenarios to concrete universes, and he takes counterfactual metaphysical possibilities to be constructed from descriptions of such universes (Spohn 2016). The result is a pragmatist approach to G2D that is ill suited to Chalmers’ rationalist E2D project.

[^note-21]: The Fregean triviality test is not exactly the same as apriori equivalence: cognitive significance marks what’s obvious to a subject at a given time, whereas apriori equivalence is often far from obvious. Mathematical identities like ‘$12^3 = 1728$’ are a clear case where the two notions come apart. Still, Chalmers argues that apriori equivalence is a well-behaved theoretical refinement of the Fregean notion. He also suggests that the 2D framework might capture something close to the Fregean notion of triviality if we substitute a weaker epistemic relation for ‘apriori coherence’ in defining the epistemic framework (Chalmers 2002b)[^chalmers-2002b].

[^note-22]: The word ‘concept’ here is not meant to imply that these matrices reflect stable semantic units of thought—it is merely meant to suggest that they reflect some aspect of the subject’s current understanding. Stalnaker rejects concepts as theoretical entities that reflect stable units of cognitive significance in thought (1984).

[^note-23]: On Stalnaker’s account, to determine just which proposition is ascribed by a particular belief report, we must answer three questions. First, how should we characterize the possible worlds that define propositional concepts: which objects, kinds, or properties should we invoke in describing the different ways the world might be? Second, which possible worlds so characterized should we treat as members of the context set for the belief ascription? Third, which aspects of the *attributor’s* understanding should we hold constant in evaluating her report in those different worlds considered as contexts of use? These factors determine the content of the diagonal proposition attributed to the believer.

[^note-24]: There is a further way in which the interests of an interpreter are taken into account on Stalnaker’s approach. Whereas a rationalist 2D theorist like Chalmers will invoke a single space of apriori possible scenarios to define 2D matrices, Stalnaker’s externalist commitments lead him to deny that we can exhaustively characterize the space of metaphysical possibility in a descriptive vocabulary that’s devoid of any empirical presuppositions. Since there is no privileged way of describing the space of possibility, the explanatory interests and presuppositions of the theorist will affect just what objects, kinds or properties she uses to individuate the possible worlds that define 2D matrices:

> It might be nice if we had a neutral language with an internally grounded semantics, a language that required no factual assumptions for its interpretation and that could provide a complete description of the world, and of all possible worlds. It might be nice if there were a pure epistemic space to which we had apriori access and in terms of which we could locate our disagreements about what the actual world is like. But I don’t think these things are possible. The only way we can describe the world is to use the materials that the actual world offers us—the things, properties and relations that we find there. (Stalnaker 2004, 319)[^stalnaker-2004]

### Notes to [The 2D Argument Against Materialism](two-dimensional-semantics.supplement.md)

[^note-25]: 25. Chalmers argues that establishing the stability of phenomenal terms like ‘pain’ is not really essential to establishing his anti-materialist conclusion (1996, 2009). His idea is that the *epistemic 1-intension* for ‘pain’ itself corresponds to a property—call it ‘diagonal pain’—that does not supervene on the physical properties of the actual world. Diagonal pain $is$ instantiated in the actual world and it is *not* instantiated in the scenario that, if actual, would make $(P \amp \neg Q)$ true. Given that there is a metaphysically possible world for every coherent scenario (premise 4), there will be a possible world just like ours physically but without diagonal pain. Since the actual world has a property—diagonal pain—that doesn’t supervene on the physical, it follows that materialism is false.

[^note-26]: 26. Chalmers in fact believes that phenomenal terms are stable, but he is less confident of the semantic stability of microphysical predicates like ‘is a quark’: perhaps different intrinsic properties are picked out depending on what the actual world is like. To allow for this possibility, Chalmers weakens the conclusion of his argument: either materialism is false or phenomenal properties are determined by the intrinsic nature of basic physical properties (Chalmers 2009)[^chalmers-2009]. As Chalmers emphasizes, most materialists will reject even this weaker conclusion, since it denies that phenomenal properties can be explained by the structural and causal properties studied by the physical sciences.

[^note-27]: 27. Chalmers (2009, §5) replies that the criticism misfires because it targets the apriori coherence of an explicitly modal claim, $\Diamond(P \amp \neg Q)$, rather than the apriori coherence of $(P \amp \neg Q)$.

### Notes to [Objections to Generalized 2D Semantics](two-dimensional-semantics.objections-2d.md)

[^note-28]: 28. It’s worth noting that a 2D empiricist is *not* committed to the rationalist’s Core Thesis. The empiricist project is to explain how speakers manage to coordinate their reference-fixing criteria through implicit conventions. For these purposes, there is no need to insist that 1-intensions must be defined for worlds with no thought or language: we may have no interest in deciding how to apply terms in situations in which we ourselves don’t exist. It is the rationalist project of linking meaning to the space of apriori coherent scenarios that gives rise to the Core Thesis.

### Notes to [Objections to the Metasemantic Interpretation](two-dimensional-semantics.objections-meta.md)

[^note-29]: 29. Stalnaker’s initial response to proponents of finer-grained propositional structure is to insist that possible world semantics provides a *minimal* kind of content that all theorists should accept (1984, 1999b). Stalnaker’s context-sensitive use of the 2D framework is intended to provide a flexible framework for explaining commonsense intuitions about logical equivalence and *de re* thought. And self-locating aspects of thought, according to Stalnaker, should not be considered an aspect of propositional contents, but rather part of one’s epistemic *relation* to a propositional content (Stalnaker 2006)[^stalnaker-2006].

[^åqvist-1973]: Åqvist, L., 1973, “Modal Logic with Subjunctive Conditionals and Dispositional Predicates”, *Journal of Philosophical Logic*, 1: 1–76.

[^ball-2014]: Ball, D., 2014, “Two-Dimensionalism and the Social Character of Meaning”, *Erkenntnis*, 79: 567–595.

[^bealer-2002]: Bealer, G., 2002, “Modal Epistemology and the Rationalist Renaissance”, in *Conceivability and Possibility*, T. Gendler and J. Hawthorne (eds.), Oxford: Oxford University Press, pp. 71–125.

[^biggs-2020]: Biggs, S. and J. Wilson, 2020, “Abductive Two-Dimensionalism: A New Route to the A Priori Identification of Necessary Truths”, *Synthese* 197: 59–70.

[^bjerring-2014]: Bjerring, J.C., 2014, “Problems in Epistemic Space”, *Journal of Philosophical Logic*, 43: 153–70.

[^block-1999]: Block, N. and R. Stalnaker, 1999, “Conceptual Analysis, Dualism, and the Explanatory Gap”, *Philosophical Review*, 108: 1–46.

[^boghossian-2011]: Boghossian, P., 2011, “Williamson on the A Priori and the Analytic”, *Philosophy and Phenomenological Research*, 82: 488–497.

[^braddon-mitchell-2004]: Braddon-Mitchell, D., 2004, “Masters of Our Meanings”, *Philosophical Studies*, 118: 133–152.

[^braddon-mitchell-2015]: –––, 2015, “A Priori Analysis and the Methodological A Posteriori”, in *The Palgrave Handbook of Philosophical Methods*, C. Daly (ed.), Basingstoke: Palgrave MacMillan, pp. 33–50.

[^brehany-2006]: Brehany, R., 2006, “Pragmatic Analyses of Anaphoric Pronouns: Do Things Look Better in 2-D?” in *Two-Dimensional Semantics*, M. Garcia-Carpintero and J. Macia (eds.), Oxford: Oxford University Press, pp. 22–37.

[^burge-1979]: Burge, T., 1979, “Individualism and the Mental”, *Midwest Studies in Philosophy*, 5: 73–122.

[^burge-1986]: –––, 1986, “Intellectual Norms and Foundations of Mind”, *Journal of Philosophy*, 83: 697–720.

[^burge-1989]: –––, 1989, “Wherein is Language Social?” in *Reflections on Chomsky*, A. George (ed.), Oxford: Blackwell, pp. 175–191.

[^byrne-1999]: Byrne, A., 1999, “Cosmic Hermeneutics”, *Philosophical Perspectives*, 13: 347–384.

[^byrne-2001]: –––, 2001, “Chalmers on Epistemic Content”, *SOFIA conference on Metaphysics of Mind*: URL $= \lt$http://web.mit.edu/abyrne/www/Epistemic.pdf$\gt$.

[^byrne-2006]: Byrne, A. and J. Pryor, 2006, “Bad Intensions”, in *Two-Dimensional Semantics: Foundations and Applications*, M. Garcia-Carpintero and J. Macia (eds.), Oxford: Oxford University Press, pp. 38–54.

[^camp-2017]: Camp, E., 2017, “Pragmatic Force in Semantic Context”, *Philosophical Studies*, 174: 1617–1627.

[^carnap-1947]: Carnap, R., 1947, *Meaning and Necessity*, Chicago: University of Chicago Press.

[^carnap-1950]: –––, 1950, “Empiricism, Semantics, and Ontology”, *Revue Internationale de Philosophie*, 11: 20–40.

[^chalmers-1996]: Chalmers, D., 1996, *The Conscious Mind*, New York: Oxford University Press.

[^chalmers-1999]: –––, 1999, “Materialism and the Metaphysics of Modality”, *Philosophy and Phenomenological Research*, 59: 473–496.

[^chalmers-2002a]: –––, 2002a, “Does Conceivability Entail Possibility?” in *Conceivability and Possibility*, T. Gendler and J. Hawthorne (eds.), Oxford: Oxford University Press, pp. 145–200.

[^chalmers-2002b]: –––, 2002b, “On Sense and Intension”, *Philosophical Perspectives*, 16: 135–82.

[^chalmers-2002c]: –––, 2002c, “The Components of Content”, in *Philosophy of Mind: Classical and Contemporary Readings*, D. Chalmers (ed.), Oxford: Oxford University Press, pp. 608–33.

[^chalmers-2004]: –––, 2004, “Epistemic Two-Dimensional Semantics”, *Philosophical Studies*, 118: 153–226.

[^chalmers-2006a]: –––, 2006a, “The Foundations of Two-Dimensional Semantics”, in *Two-Dimensional Semantics: Foundations and Applications*, M. Garcia-Carpintero and J. Macia (eds.), Oxford: Oxford University Press, pp. 55–140.

[^chalmers-2006b]: –––, 2006b, “Two-Dimensional Semantics”, in *Oxford Handbook of Philosophy of Language*, E. Lepore and B. Smith (eds.), Oxford: Oxford University Press, pp. 575–606.

[^chalmers-2009]: –––, 2009, “The Two-Dimensional Argument Against Materialism”, in *Oxford Handbook of Philosophy of Mind*, B. McLaughlin (ed.), Oxford: Oxford University Press, pp. 313–335.

[^chalmers-2011a]: –––, 2011a, “Propositions and Attitude Reports: A Fregean Account”, *Noûs*, 45: 595–639.

[^chalmers-2011b]: –––, 2011b, “The Nature of Epistemic Space”, in *Epistemic Modality*, A. Egan and B. Weatherson (eds.), Oxford: Oxford University Press.

[^chalmers-2012]: –––, 2012, *Constructing the World*, Oxford: Oxford University Press.

[^chalmers-2014a]: –––, 2014a, “Frontloading and Fregean sense: Reply to Neta, Schroeter and Stanley”, *Analysis*, 74: 676–697.

[^chalmers-2014b]: –––, 2014b, “Intensions and Indeterminacy: Reply to Soames, Turner, and Wilson”, *Philosophy and Phenomenological Research*, 89: 249–269.

[^chalmers-2001]: Chalmers, D. and F. Jackson, 2001, “Conceptual Analysis and Reductive Explanation”, *Philosophical Review*, 110: 315–61.

[^chalmers-2014]: Chalmers, D., and B. Rabern, 2014, “Two-dimensional semantics and the nesting problem”, *Analysis*, 74: 210–224.

[^crimmins-1992]: Crimmins, M., 1992, *Talk About Beliefs*, Cambridge MA: MIT Press.

[^crossley-1977]: Crossley, J. N. and I. L. Humberstone, 1977, “The Logic of ‘Actually’”, *Reports on Mathematical Logic*, 8: 11–29.

[^davies-1980]: Davies, M. and I. L. Humberstone, 1980, “Two Notions of Necessity”, *Philosophical Studies*, 38: 1–30.

[^diaz-leon-2011]: Diaz-Leon, E., 2011, “Reductive explanation, concepts and a priori entailment”, *Philosophical Studies*, 155: 99–116.

[^descartes-1641]: Descartes, R., 1641, *Meditations on First Philosophy*, ed. J. Cottingham, 1996, Cambridge: Cambridge University Press.

[^dennett-1988]: Dennett, D., 1988, “Quining Qualia”, in *Consciousness in Modern Science*, A. Marcel and E. Bisiach (eds.), Oxford: Oxford University Press, pp. 44–77.

[^deutsch-1993]: Deutsch, Harry, 1993, “Semantics for Natural Kind Terms”, *Canadian Journal of Philosophy*, 23: 389–411.

[^deutsch-1990]: –––, 1990, “Contingency and Modal Logic”, *Philosophical Studies*, 60: 89–92.

[^dever-2007]: Dever, J., 2007, “Low-Grade Two-Dimensionalism”, *Philosophical Books*, 48: 1–16.

[^donnellan-1970]: Donnellan, K., 1970, “Proper Names and Identifying Descriptions”, *Synthese*, 21: 335–358.

[^dowell-2008]: Dowell, J. L., 2008, “Empirical Metaphysics: the role of intuitions about possible cases in philosophy”, *Philosophical Studies*, 140: 19–46.

[^dummett-1973]: Dummett, 1973, *Frege: Philosophy of Language*, Cambridge, MA: Harvard University Press.

[^dummett-1981]: –––, 1981, *The Interpretation of Frege’s Philosophy*, London: Duckworth.

[^ebbs-2014]: Ebbs, G., 2014, “Conditionalization and Conceptual Change: Chalmers in Defense of a Dogma”, *Journal of Philosophy*, 111: 689–703.

[^elliott-2013]: Elliott, E., K. McQueen, and C. Weber, 2013, “Epistemic Two-Dimensionalism and the Argument from Epistemic Misclassification”, *Australasian Journal of Philosophy*, 91: 375–389.

[^evans-1979]: Evans, G., 1979, “Reference and Contingency”, *Monist*, 62: 161–189.

[^evans-1982]: –––, 1982, *The Varieties of Reference*, Oxford: Oxford University Press.

[^fine-2007]: Fine, K., 2007, *Semantic Relationism*, Oxford: Blackwell.

[^forbes-2011]: Forbes, G., 2011, “The problem of factives for sense theories”, *Analysis*, 71: 654–662.

[^frege-1892]: Frege, G., 1892, “On *Sinn* and *Bedeutung*”, in *The Frege Reader*, M. Beany (ed.), Oxford: Blackwell (1997), pp. 151–71.

[^fritz-2013]: Fritz, P., 2013, “A logic for epistemic two-dimensional semantics”, *Synthese*, 190: 1753–1770.

[^gertler-2002]: Gertler, B., 2002, “Explanatory Reduction, Conceptual Analysis, and Conceivability Arguments about the Mind”, *Noûs*, 36: 22–49.

[^greene-2017]: Greene, M., 2017, “Conversation and Common Ground”, *Philosophical Studies*, 174: 1589–1604

[^grice-1989]: Grice, P., 1989, *Studies in the Ways of Words*, Cambridge MA: Harvard University Press.

[^haas-spohn-1995]: Haas-Spohn, U., 1995, *Versteckte Indexikalität und subjektive Bedeutung*, Berlin: Akademie-Verlag; English translation, [Hidden Indexicality and Subjective Meaning](http://www.uni-konstanz.de/philosophie/files/haas-spohn_-versteckte_indexikalitaet_und_subjektive_bedeutung.pdf).

[^hazen-1976]: Hazen, A. 1976, “Expressive Completeness in Modal Logic”, *Journal of Philosophical Logic*, 5: 25–46.

[^hazen-1978]: –––, 1978, “Eliminability of the Actuality Operator in Propositional Modal Logic”, *Notre Dame Journal of Formal Logic*, 19: 617–622.

[^heck-2018]: Heck, R., 2018, “The Frontloading Argument”, *Philosophical Studies*, 175: 2582–2608.

[^hill-1999]: Hill, C. and B. McLaughlin, 1999, “There are Fewer Things in Reality than are Dreamt of in Chalmers’s Philosophy”, *Philosophy and Phenomenological Research*, 49: 445–454.

[^humberstone-2004]: Humberstone, L., 2004, “Two-Dimensional Adventures”, *Philosophical Studies*, 118: 17–65.

[^jackson-1994]: Jackson, F., 1994, “Armchair Metaphysics”, in *Meaning in Mind*, M. Michael and J. O’Leary-Hawthorne (eds.), Dordrecht: Kluwer Academic Publishers, pp. 23–42.

[^jackson-1998a]: –––, 1998a, *From Metaphysics to Ethics: A Defence of Conceptual Analysis*, Oxford: Oxford University Press.

[^jackson-1998b]: –––, 1998b, “Reference and Description Revisited”, *Philosophical Perspectives*, 12: 201–218.

[^jackson-2000]: –––, 2000, “Reply to Yablo: What do we communicate when we use ethical terms?” *Philosophical Books*, 48: 24–29.

[^jackson-2004]: –––, 2004, “Why We Need A-Intensions”, *Philosophical Studies*, 118: 257–277.

[^jackson-2006]: –––, 2006, “The Story of ‘Fred’”, in *Content and Modality: Themes from the Philosophy of Robert Stalnaker*, J. Thomson and A. Byrne (eds.), Oxford: Clarendon Press, pp. 191–203.

[^jackson-2007]: –––, 2007, “Reference and Description from the Descriptivists’ Corner”, *Philosophical Books*, 48: 17–26.

[^jackson-1995]: Jackson, F. and P. Pettit, 1995, “Moral Functionalism and Moral Motivation”, *Philosophical Quarterly*, 45: 20–40.

[^jago-2009]: Jago, M., 2009, “Logical Information and Epistemic Space”, *Synthese*, 167: 327–341.

[^jago-2014]: –––, 2014, *The Impossible: An Essay on Hyperintensionality*, Oxford: Oxford University Press.

[^jenkins-2008]: Jenkins, C., 2008, *Grounding Concepts: An Empirical Basis for Arithmetical Knowledge*, Oxford: Oxford University Press.

[^jenkins-2012]: –––, 2012, “A Priori Knowledge: The Conceptual Approach”, in *The Continuum Companion to Epistemology*, A Cullison (ed.), 180–98. London: Continuum Press.

[^johannesson-2016]: Johannesson, E., and S. Packalén, 2016, “The A Priori-Operator and the Nesting Problem”, *Thought*, 5: 169–179.

[^kamp-1971]: Kamp, J. A. W., 1971, “Formal Properties of ‘Now’”, *Theoria*, 37: 227–273.

[^kant-1787]: Kant, I., 1787, *Critique of Pure Reason*, trans. N. K. Smith, London: Macmillan (1929).

[^kaplan-1989a]: Kaplan, D., 1989a, “Demonstratives”, in *Themes from Kaplan*, Oxford: Oxford University Press, pp. 481–563.

[^kaplan-1989b]: –––, 1989b, “Afterthoughts”, in *Themes from Kaplan*, Oxford: Oxford University Press, pp. 565–612.

[^kaplan-1990]: –––, 1990, “Words”, *Proceedings of the Aristotelian Society Supplement*, 64: 93–119.

[^kipper-2012]: Kipper, J., 2012, *A Two-Dimensional Guide to Conceptual Analysis*, Frankfurt: Ontos.

[^kipper-2017]: –––, 2017, “Propositional apriority and the nesting problem”, *Philosophical Studies*, 174: 1091–1104.

[^kripke-1980]: Kripke, S., 1980, *Naming and Necessity*, Cambridge, MA: Harvard University Press.

[^kroon-2004a]: Kroon, F., 2004a, “A-Intensions and Communication”, *Philosophical Studies*, 118: 279–298.

[^kroon-2004b]: –––, 2004b, “Descriptivism, Pretense, and the Frege–Russell Problems”, *Philosophical Review*, 113: 1–30.

[^laurence-2003]: Laurence, S. and E. Margolis, 2003, “Concepts and Conceptual Analysis”, *Philosophy and Phenomenological Research*, 67: 253–282.

[^lewis-1966]: Lewis, D., 1966, “An Argument for the Identity Theory”, *Journal of Philosophy*, 63: 17–25.

[^lewis-1969]: –––, 1969, *Convention*, Cambridge, MA: Harvard University Press.

[^lewis-1970]: –––, 1970, “How to Define Theoretical Terms”, *Journal of Philosophy*, 67: 427–46.

[^lewis-1972]: –––, 1972, “Psychophysical and Theoretical Identifications”, *Australasian Journal of Philosophy*, 50: 412–458.

[^lewis-1979]: –––, 1979, “Attitudes *De Dicto* and *De Se*”, *Philosophical Review*, 88: 513–543.

[^lewis-1980]: –––, 1980, “Mad Pain, Martian Pain”, in *Readings in the Philosophy of Psychology*, N. Block (ed.), Cambridge, MA: Harvard University Press, pp. 216–222.

[^lewis-1981]: –––, 1981, “Index, Context, and Content”, in *Philosophy and Grammar*, S. Kanger and S. Ohlman (eds.), Dordrecht: Reidel, pp. 79–100.

[^lewis-1994]: –––, 1994, “Reduction in Mind”, in *A Companion to the Philosophy of Mind*, S. Guttenplan (ed.), Oxford: Blackwell, pp. 412–431.

[^lewis-1997]: –––, 1997, “Naming the Colours”, *Australasian Journal of Philosophy*, 75: 325–342.

[^loar-1990]: Loar, B., 1990, “Phenomenal States”, *Philosophical Perspectives*, 4: 81–108.

[^loar-1999]: –––, 1999, “David Chalmers’s *The Conscious Mind*”, *Philosophy and Phenomenological Research*, 49: 465–495.

[^marconi-2005]: Marconi, D., 2005, “Two-Dimensional Semantics and the Articulation Problem”, *Synthese*, 143: 321–349.

[^melnyk-2008]: Melnyk, A., 2008, “Conceptual and Linguistic Analysis: A Two-Step Program”, *Noûs*, 42: 267–291.

[^neta-2014]: Neta, R., 2014, “Chalmers’s Frontloading Argument for A Priori Scrutability”, *Analysis*, 74: 651–661.

[^nimtz-2004]: Nimtz, C., 2004, “Two-Dimensionalism and Natural Kind Terms”, *Synthese*, 138: 125–148.

[^ninan-2010a]: Ninan, D., 2010a, “De Se Attitudes: Ascription and Communication”, *Philosophy Compass*, 5: 551–567.

[^ninan-2010b]: –––, 2010b, “Semantics and the objects of assertion”, *Linguistics and Philosophy*, 33: 355–380.

[^ninan-2013]: –––, 2013, “Self-Location and Other-Location”, *Philosophy and Phenomenological Research*, 87: 301–331.

[^perry-1979]: Perry, J., 1979, “The problem of the Essential Indexical”, *Noûs*, 13: 3–21.

[^perry-1980]: –––, 1980, “A Problem about Continued Belief”, *Pacific Philosophical Quarterly*, 61: 317–322.

[^perry-2001]: –––, 2001, *Knowledge, Possibility, and Consciousness*, Cambridge, MA: MIT Press.

[^perry-2006]: –––, 2006, “Stalnaker and Indexical Belief”, in *Content and Modality: Themes from the Philosophy of Robert Stalnaker*, J. Thomson and A. Byrne (eds.), Oxford: Clarendon Press, pp. 204–221.

[^pickel-2016]: Pickel, B., 2016, “Frontloading, Supposition, and Contraction”, *Philosophical Quarterly*, 66: 559–578.

[^pickel-2018]: Pickel, B. and M. Schulz, 2018, “Quinean Updates: In Defense of ‘Two Dogmas’”, *Journal of Philosophy*, 115: 57–91.

[^predelli-1998]: Predelli, S., 1998, “‘I am not here now’”, *Analysis*, 58: 107–115.

[^pryor-2006]: Pryor, J., 2006, “Hyper-Reliability and Apriority”, *Proceedings of the Aristotelian Society*, 106: 327–344.

[^putnam-1970]: Putnam, H., 1970, “Is Semantics Possible?” in *Languages, Belief and Metaphysics*, H. Kiefer and M. Munitz (eds.), *Contemporary Philosophic Thought: The International Philosophy Year Conferences at Brockport*, New York: SUNY Press, pp. 50–63. Reprinted in Putnam (1975), pp. 139–152.

[^putnam-1972]: –––, 1972, “The Meaning of ‘Meaning’”, *Minnesota Studies in the Philosophy of Science*, 7: 131–193. Reprinted in Putnam (1975), pp. 215–271.

[^putnam-1973]: –––, 1973, “Explanation and Reference”, in *Conceptual Change*, G. Pearce and P. Maynard (eds.): Dordrecht-Reidel, pp. 199-221. Reprinted in Putnam (1975), pp. 196–214.

[^putnam-1974]: –––, 1974, “The Refutation of Conventionalism”, *Noûs*, 8: 25–40. Reprinted in Putnam (1975), pp. 153–195.

[^putnam-1975]: –––, 1975, *Mind, Language, and Reality* (Philosophical Papers: Volume 2), Cambridge: Cambridge University Press.

[^quine-1951a]: Quine, W. V. O., 1951a, “Two Dogmas of Empiricism”, *Philosophical Review*, 60: 20–43.

[^quine-1951b]: –––, 1951b, “On Carnap’s Views on Ontology”, *Philosophical Studies*, 2: 65–72.

[^rabern-2012a]: Rabern, B., 2012a, “Against the Identification of Assertoric Content with Compositional Value”, *Synthese*, 189: 75–96.

[^rabern-2012b]: –––, 2012b, “Propositions and Multiple Indexing”, *Thought*, 1: 116–124.

[^rabern-2013]: –––, 2013, “Monsters in Kaplan’s Logic of Demonstratives”, *Philosophical Studies*, 164: 393–404.

[^rabinowicz-2010]: Rabinowicz, W., 2010, “Analyticity and Possible-World Semantics”, *Erkenntnis*, 72: 295–314.

[^richard-1990]: Richard, M., 1990, *Propositional Attitudes: An Essay on Thoughts and How We Ascribe Them*, Cambridge: Cambridge University Press.

[^rupert-2016]: Rupert, R.D., 2016, “Embodied Knowledge, Conceptual Change, and the A Priori; or, Justification, Revision and the Ways Life Could Go”, *American Philosophical Quarterly*, 53: 169–192.

[^sbardolini-2019]: Sbardolini, G., 2019, “Two-Dimensional Paradox”, *Australasian Journal of Philosophy*, 97: 605–617.

[^schroeter-2003]: Schroeter, L., 2003, “Gruesome Diagonals”, *Philosophers’ Imprint*, 3 (3): 1–23.

[^schroeter-2004]: –––, 2004, “The Rationalist Foundations of Chalmers’ 2D Semantics”, *Philosophical Studies*, 118: 227–255.

[^schroeter-2005]: –––, 2005, “Considering Empty Worlds as Actual”, *Australasian Journal of Philosophy*, 83: 331–347.

[^schroeter-2006]: –––, 2006, “Against A Priori Reductions”, *Philosophical Quarterly*, 56: 562–586.

[^schroeter-2014]: –––, 2014, “Scrutability and Epistemic Updating: Comments on Chalmers’ Constructing the World”, *Analysis*, 74: 638–651.

[^schroeter-2009]: Schroeter, L. and J. Bigelow, 2009, “Jackson’s Classical Model of Meaning”, in *Mind, Ethics, and Conditionals: Themes From the Philosophy of Frank Jackson*, I. Ravenscroft (ed.), Oxford: Oxford University Press, pp. 85–109.

[^schroeter-2009-2]: Schroeter, L. and F. Schroeter, 2009, “A Third Way in Metaethics”, *Noûs*, 43: 1–30.

[^searle-1983]: Searle, J. R., 1983, *Intentionality. An Essay in the Philosophy of Mind*, Cambridge: Cambridge University Press.

[^segerberg-1973]: Segerberg, K., 1973, “Two-Dimensional Modal Logic”, *Journal of Philosophical Logic*, 2: 77–96.

[^shoemaker-1999]: Shoemaker, S., 1999, “On David Chalmers’s *The Conscious Mind*”, *Philosophy and Phenomenological Research*, 59: 539–544.

[^sidelle-1989]: Sidelle, A., 1989, *Necessity, Essence, and Individuation: A Defense of Conventionalism*, Ithaca: Cornell University Press.

[^soames-2005]: Soames, S., 2005, *Reference and Description: The Case against Two-Dimensionalism*, Princeton: Princeton University Press.

[^soames-2006a]: –––, 2006a, “Reply to Critics of *Reference and Description*”, *Central Division Meetings of the American Philosophical Association*: URL $= \lt$http://www-rcf.usc.edu/${\sim}$soames/replies/Rep_Chicago.pdf$\gt$.

[^soames-2006b]: –––, 2006b, “Understanding Assertion”, in *Content and Modality: Themes from the Philosophy of Robert Stalnaker*, J. Thomson and A. Byrne (eds.), Oxford: Clarendon Press, pp. 222–250.

[^soames-2007]: –––, 2007, ‘The Substance and Significance of the Dispute over Two-Dimensionalism’, *Philosophical Books*, 48: 34–49.

[^soames-2014]: –––, 2014, “Epistemic Intensions”, *Philosophy and Phenomenological Research*, 89: 220–228.

[^speaks-2010]: Speaks, J., 2010, “The Epistemic Argument and Epistemic Two-Dimensionalism”, *Australasian Journal of Philosophy*, 88: 59–78.

[^stalnaker-1978]: Stalnaker, R., 1978, “Assertion”, *Syntax and Semantics*, 9: 315–332. Reprinted in Stalnaker (1999a), pp. 78–95.

[^stalnaker-1981]: –––, 1981, “Indexical Belief”, *Synthese*, 49: 129–151. Reprinted in Stalnaker (1999a), pp. 130–149.

[^stalnaker-1984]: –––, 1984, *Inquiry*, Cambridge, MA: MIT Press, Bradford.

[^stalnaker-1987]: –––, 1987, “Semantics for Belief”, *Philosophical Topics*, 15: 177–190. Reprinted in Stalnaker (1999a), pp. 117–129.

[^stalnaker-1988]: –––, 1988, “Belief Attribution and Context”, in *Contents of Thought*, R. Grimm and D. Merrill (eds.), Tucson: University of Arizona Press, pp. 156–181. Reprinted in Stalnaker (1999a), pp. 150–166.

[^stalnaker-1999a]: –––, 1999a, *Context and Content*, Oxford: Oxford University Press.

[^stalnaker-1999b]: –––, 1999b, “Introduction”, in Stalnaker (1999a), pp. 1–28.

[^stalnaker-2001]: –––, 2001, “On Considering a Possible World as Actual”, *Proceedings of the Aristotelian Society*, Supp. 75: 141–156. Reprinted in Stalnaker (2003), pp. 188–200.

[^stalnaker-2003]: –––, 2003, *Ways a World Might Be: Metaphysical and Anti-Metaphysical Essays*, Oxford: Clarendon Press.

[^stalnaker-2004]: –––, 2004, “Assertion Revisited: On the Interpretation of Two-Dimensional Modal Semantics”, *Philosophical Studies*, 118: 299–322.

[^stalnaker-2006]: –––, 2006, “Responses”, in *Content and Modality: Themes from the Philosophy of Robert Stalnaker*, J. Thomson and A. Byrne (eds.), Oxford: Clarendon Press, pp. 251–295.

[^stalnaker-2007]: –––, 2007, “Critical Notice of Scott Soames’s Case against Two-Dimensionalism”, *Philosophical Review*, 116: 251–266.

[^stalnaker-2008]: –––, 2008, *Our Knowledge of the Internal World*, Oxford: Clarendon Press.

[^stalnaker-2009]: –––, 2009, “On Hawthorne and Magidor on Assertion, Context, and Epistemic Accessibility”, *Mind*, 118: 399–409.

[^stalnaker-2014]: –––, 2014, *Context*, Oxford: Oxford University Press.

[^stalnaker-2017]: –––, 2017, “Précis of Context”, *Philosophical Studies*, 74: 1583–1585.

[^stanley-2014]: Stanley, J., 2014, “Constructing Meaning”, *Analysis*, 74: 662–676.

[^szabó-2017]: Szabó, Z.G., 2017, “Prospective Interpretation”, *Philosophical Studies*, 174: 1606–1616.

[^tiehen-2014]: Tiehen, J., 2014, “A Priori Scrutability and That’s All”, *Journal of Philosophy*, 111: 649–666.

[^topey-2018]: Topey, B., 2018, “Quinean Holism, Analyticity, and Diachronic Rational Norms”, *Synthese*, 195: 3143–3171.

[^torre-2010]: Torre, S., 2010, “Centered Assertion”, *Philosophical Studies*, 150: 97–114.

[^turner-2014]: Turner, J., 2014, “Scrying an Indeterminate World”, *Philosophy and Phenomenological Research*, 89: 229–237.

[^valaris-2009]: Valaris, M., 2009, “Two-Dimensionalism and the Epistemology of Recognition”, *Philosophical Studies*, 142: 427–445.

[^vlach-1973]: Vlach, F., 1973, *‘Now’ and ‘Then’: A Formal Study in the Logic of Tense Anaphora*, Ph.D. Thesis, Los Angeles: University of California, Los Angeles.

[^williamson-2007]: Williamson, T., 2007, *The Philosophy of Philosophy*, Oxford: Blackwell.

[^williamson-2012]: –––, 2012, “How Deep is the Distinction between A Priori and A Posteriori Knowledge?”, in *The A Priori in Philosophy*, A. Casullo and J. Thurow (eds.), Oxford: Oxford University Press.

[^wilson-2014]: Wilson, M., 2014, “David Chalmers versus the boll weevil”, *Philosophy and Phenomenological Research*, 89: 238–248.

[^wittmer-2013]: Wittmer, G., 2013, “Review of J. Kipper, *A Two-Dimensionalist Guide to Conceptual Analysis*”, *Notre Dame Philosophical Reviews*, 11 January 2013, [available online](https://ndpr.nd.edu/reviews/a-two-dimensionalist-guide-to-conceptual-analysis/)/.

[^wong-1996]: Wong, K-Y., 1996, “Sentence-Relativity and the Necessary Aposteriori”, *Philosophical Studies*, 83: 53–91.

[^yablo-1999]: Yablo, S., 1999, “Concepts and Consciousness”, *Philosophy and Phenomenological Research*, 59: 455–463.

[^yablo-2000a]: –––, 2000a, “Red, Bitter, Best”, *Philosophical Books*, 48: 17–23.

[^yablo-2000b]: –––, 2000b, “Textbook Kripkeanism and the Open Texture of Concepts”, *Pacific Philosophical Quarterly*, 81 (1): 98–122.

[^yablo-2002]: –––, 2002, “Coulda, Woulda, Shoulda”, in *Conceivability and Possibility*, T. Gendler and J. Hawthorne (eds.), Oxford: Oxford University Press, pp. 441–492.

[^yablo-2006]: –––, 2006, “No Fool’s Cold: Notes on Illusions of Possibility”, in *Two-Dimensional Semantics*, M. Garcia-Carpintero and J. Macia (eds.), Oxford: Oxford University Press, pp. 327–346.

[^yablo-2008]: –––, 2008, *Thoughts: Papers on Mind, Meaning, and Modality*, Oxford: Oxford University Press.

[^yalcin-2015]: Yalcin, S., 2015, “Semantics and Metasemantics in the Context of Generative Grammar”, in *Metasemantics: New Essays on the Foundations of Meaning*, A. Burgess and B. Sherman (ed.), Oxford: Oxford University Press, pp. 17–54.
