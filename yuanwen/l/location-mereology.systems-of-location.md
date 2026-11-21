# location-mereology — systems-of-location（supplement）

> （《location-mereology》词条补充材料，源：plato.stanford.edu/entries/location-mereology/systems-of-location.html）

#### Supplement to Location and Mereology

In the entry we discussed four locative relations—exact, weak, entire, and pervasive location—and we used exact location to define the others. This yields System 1 below. Here we sketch several other systems and discuss some of their consequences.

- System 1: Primitive Exact Location
- System 2: Primitive Weak Location, with Parsons-style Definitions
- System 3: Primitive Weak Location, with Eagle-style Definitions
- System 4: Primitive Entire Location
- System 5: Primitive Plural Pervasive Location

### System 1: Primitive Exact Location

For convenience, we set out definitions again here:

**(DS1.1)**

$x$ is weakly located at $y$ $=_{\df}$ $x$ is exactly located at something that overlaps $y$. $$\WKL(x, y) =_{\df} \exists z[L(x, z) \amp O(z, y)]$$

**(DS1.2)**

$x$ is entirely located at $y$ $=_{\df}$ $x$ is exactly located at some part of $y$. $$\EL(x, y) =_{\df} \exists z[L(x, z) \amp P(z, y)]$$

**(DS1.3)**

$x$ is pervasively located at $y$ $=_{\df}$ $x$ is exactly located at something of which $y$ is a part. $$PL(x, y) =_{\df} \exists z[L(x, z) \amp P(y, z)]$$

One important fact about (DS1.1) is that it makes

- **Exactness** If a thing is weakly located somewhere, then it’s exactly located somewhere. $$\forall x\forall y[\WKL (x, y) \rightarrow \exists zL(x, z)]$$

an analytic and hence necessary truth (Parsons 2007). This is important because there are reasons to doubt that Exactness is necessary. At least two exotic cases pose problems for Exactness. The first is

- **Pointy objects in gunky space** (Gilmore 2006: 203; Parsons 2007: 207–9).
- All regions are extended and gunky and decompose into smaller (but still extended and still gunky) regions,
- object $o_p$ is an unextended, point-like, located entity, and
- nothing is located any non-region.

Since $o_p$ is point-like, it is too small to be exactly located at any extended region, but it should still be weakly located at many regions—in particular, at each in a sequence of nested regions that ‘converge onto’ it. So, if it is possible that (i)–(iii) are all true, then it is possible that, contrary to Exactness, a thing is weakly located somewhere without being exactly located anywhere. A second problem case is

- **Almond in the void** (Kleinschmidt 2016). An almond lies within an extended simple region larger than the almond. There are no regions as small as, or smaller than, the almond. The almond is not located at any non-regions.

Since the almond lies within the region, it should count as being weakly located at the region. Since the region is larger than the almond, the almond is not exactly located at the region. Since there are no regions that are the same size as the almond, the almond is not exactly located anywhere. Therefore, we have another apparent case of weak location without exact location, contrary to Exactness.

### System 2: Primitive Weak Location, with Parsons-style Definitions

A system in which weak location is primitive may fare better with the two cases above. We will consider two such systems, the first of which traces to Parsons (2007). Its core is the following definition of exact location:

**(DS2.1)**

$x$ is exactly located at $y$ $=_{\df}$ $x$ is weakly located at all and only those entities that overlap $y$. $$L(x, y) =_{\df} \forall z[\WKL(x, z) \leftrightarrow O(y, z)]$$

The remainder of System 2 results from dropping (DS1.1) and retaining (DS1.2) and (DS1.3). One potential virtue of System 2 is that it does not make Exactness analytic. Having dropped the definition of weak location in terms of exact location, nothing forces us to deny the possibility of something that is weakly located at certain regions while not being exactly located anywhere. This is just what we wanted to say about the pointy object $o_p$ in gunky space. So here System 2 improves on System 1.

System 2 does not help, however, with Almond in the void. Since the almond is weakly located at all and only the regions that overlap the extended simple region, (DS2.1) yields the unwanted verdict that the almond is exactly located at the region, and (DS1.3) then yields the unwanted verdict that it is also pervasively located there. The verdicts are unwanted because in both cases the almond is intuitively too small to be exactly and pervasively located at the relevant region. One may suggest to define entire location directly in terms of weak location as ‘$y$ overlaps all of $x$’s weak locations’. According to this definition, the almond is entirely located at the region (the same holds for (DS1.2)). But then it becomes implausible not to define ‘$x$ is pervasively located at $y$’ as ‘$x$ is weakly located at every region that overlaps $y$’, which yields (again) the unwanted verdict that the almond is pervasively located at the region. So, System 2, and minor variants thereof, seem unable to handle Almond in the void.

A second problem for System 2 and (DS2.1) arises from the fact that they make

- **Quasi-functionality** Nothing has two different exact locations, unless each of those locations overlaps exactly the same things as the other—i.e., unless they mereologically coincide. $$\forall x\forall y\forall z[(L(x, y) \amp L(x, z)) \rightarrow CO(y, z)]$$

an analytic and hence necessary truth. There are many who would deny Quasi-functionality, and there are others who would deny that it is necessary. (It is worth noting that in the presence of a suitably extensional mereology Quasi-functionality entails full-blown Functionality).

For now, we can consider a third exotic problem case:

- **Time traveling Suzy**. As an adult, Suzy travels back in time and visits herself as an infant. Time traveling, adult Suzy stands near the crib in which Baby Suzy sleeps. Adult Suzy is exactly located at a certain adult-sized region, $r_A$, and Baby Suzy is exactly located at a certain baby-sized region, $r_B$. The two regions, $r_A$ and $r_B$, do not even overlap, much less coincide. And yet one thing, Suzy, is exactly located at each of them. (We borrow the character of Suzy from Vihvelin 1996).

As with the two previous cases, not everyone will grant the possibility of Time traveling Suzy. Some will deny the possibility of backward time travel or self-visitation; others will allow it but deny that it involves single thing having two exact locations. However, for those who grant the possibility of the case as described, it generates an argument against System 2.

### System 3: Primitive Weak Location, with Eagle-style Definitions

The fact that System 2 entails Quasi-functionality motivates the following system of definitions due to Eagle (2010a, 2016a,b). To be precise, Eagle starts with a relation he calls “occupation” and stipulates that an entity occupies a region iff the entity can, in whole or in part, be found at that region. We take this relation to be weak location. Indeed, Eagle (2019) considers the general consequences of taking weak location as primitive, independently of particular definitions of other locative notions in terms of it. One possibility is to define Containment $(\CN)$, Filling $(F)$, and Exact Location as follows. (For a thorough assessment of Eagle’s theory of location see Costa and Calosi (2022) and Payton 2023.)

**(DS3.1)**

$x$ is contained in $y =_{\df}$ each part of $x$ occupies a part of $y$. $$\CN(x, y) =_{\df} \forall w [P(w, x) \rightarrow \exists z [P(z, y) \amp \WKL (w, z)]]$$

**(DS3.2)**

$x$ fills $y =_{\df}$ each part of $y$ is occupied by $x$. $$F(x, y) =_{\df} \forall w [P(w, y) \rightarrow \WKL(x, w)]$$

**(DS3.3)**

$x$ is exactly located at $y$ $=_{\df}$ $x$ is contained in $y$, $x$ fills $y$, and there are no proper parts of $y$ that $x$ is contained in and fills. $$ \begin{align} L(x, y) =_{\df}\ &\CN(x, y) \amp F(x, y) \amp {}\\ &\neg\exists w [PP(w, y) \amp \CN(x, w) \amp F(x, w)] \end{align} $$

System 3 entails neither Exactness nor Quasi-Functionality. Failure of Exactness entails that it can handle pointy objects in gunky space. One might be tempted to run the same argument for Time Travelling Suzy. Things are however a little more nuanced. Suppose that Adult Suzy at $r_A$ has a part that Baby Suzy at $r_B$ does not have, and that Baby Suzy at $r_B$ has a part that Adult Suzy at $r_A$ does not have. If so, Suzy will be only contained at the sum of $r_A$ and $r_B$ (i.e., $r_A +r_B$) and will be uniquely exactly located there. Intuitively, this is not the correct result. Even in the absence of mereological change a slightly modified Time Travelling Suzy scenario raises problems of over-generation of exact locations. Suppose Suzy travels back in time to visit herself and is exactly located at two *congruent* regions $r_A$ and $r_B$, as before. We stipulate that $r_A$ is the sum of two regions $r_A$-left and $r_A$-right. The same for $r_B$. Furthermore, Suzy$_A$ is the sum of Suzy$_A$-left and Suzy$_A$-right, that are exactly located at $r_A$-left and $r_A$-right respectively. Now consider the region $r$ which is the sum of $r_A$-left and $r_B$-right $(r = r_A$-left $+ r_B$-right). The definitions above entail that Suzy is exactly located at $r_A$, and at $r_B$, but also at the disconnected region $r$.

What about the Almond in the void? The almond is contained and fills the (larger) simple region. Hence the system delivers that the almond is exactly located at the region.

Finally, there is another case that spells trouble for System 3, namely:

- **Nested Multilocation** (adapted from Kleinschmidt 2011, discussed in the main text). Clifford is a large statue of a dog, made of small statues. Clifford shrinks, travels back in time, and is given the name ‘Odie’. Odie, together with many other small statues, is used to build Clifford. Odie is exactly located at $r_S$, a small region; Clifford is exactly located at $r_L$, a large region; and $r_S$ is a proper part of $r_L$.

If we assume that Odie is identical to Clifford, we get the result that a single thing is exactly located at two different regions, one of which is a proper part of the other. (DS3.3) rules this out, which might strike some readers as a drawback. Interestingly, this system rules out extended simples by definition—Costa and Calosi (2022).

### System 4: Primitive Entire Location

Next, we consider a system of definitions (due to Correia 2022) on which entire location is primitive.

**(DS4.1)**

$x$ is exactly located at $y$ $=_{\df}$ $x$ is entirely located at $y$ but not at any proper part of $y$ (Correia 2022: 567). $$L(x, y) =_{\df} \EL(x, y) \amp {\sim} \exists z[\PP(z, y) \amp \EL(x, z)]$$

**(DS4.2)**

$x$ is weakly located at $y$ $=_{\df}$ $x$ is entirely located at some region $z$ such that for any $w$, if $w$ is a part of $z$ and $x$ is entirely located at $w$, then $w$ overlaps $y$ (Correia 2022: 568). $$\begin{align} WKL(x, y)\,=_{df}\,&\exists z [\text{EL}(x, z)\ \land \\ &\forall w [(P(w, z) \land \text{ EL}(x, w)) \rightarrow \text{ O}(w, y)]] \end{align}$$

Correia (2022) goes on to define pervasive location in terms of entire location; we leave this out to save space. What is important here is to note that System 3 handles both Time traveling Suzy and Pointy objects in gunky space.

Start with the former. Intuitively, Suzy is entirely located at $r_A$ but not at any of its proper parts. If that is correct, then (DS4.1) yields the result that Suzy is exactly located at $r_A$, as desired. Parallel comments go for $r_B$. So, Suzy has two different, disjoint, exact locations, as desired.

Turning now from (DS4.1) to (DS4.2), one might wonder what could justify adopting the rather complicated definition instead of the simpler definition: ‘$x$ is weakly located at $y$’ as ‘$y$ overlaps every region at which $x$ is entirely located’. Correia notes that the simpler definition would mishandle cases like Time traveling Suzy. Consider some region $r_C$ that overlaps $r_A$, the adult-sized region, but not $r_B$, the baby-sized region. Region $r_C$ does not overlap *every* region at which Suzy is entirely located. For example, $r_C$ does not overlap $r_B$. So, the simpler definition yields the intuitively incorrect result that Suzy is not weakly located at $r_C$.

This might suggest that we should define ‘$x$ is weakly located at $y$’ as ‘$y$ overlaps some region at which $x$ is entirely located’. After all, while $r_C$ does not overlap *every* entire location of Suzy, it does overlap at least one—for example, $r_A$. But this would overgenerate cases of weak location. Take some small cubical region 20 km away from Suzy and her crib. Suzy is not weakly located at that cubical region. But according to the latest proposed definition, she is, since the cubical region does overlap *some* entire location of Suzy—for example, the exact location of the whole Milky Way Galaxy, which includes $r_A$ and $r_B$ as proper parts.

Correia’s own (DS4.2) yields the correct verdict. According to that definition, $r_C$’s overlapping *some* entire location of Suzy is not sufficient for Suzy to be weakly located at $r_C$. Nor is it *necessary* that $r_C$ overlaps *every* entire location of Suzy. Instead, what is necessary and sufficient is that there be a region $z$ at which Suzy is entirely located *every part w of which* is such that if Suzy is entirely located at $w$, then $w$ overlaps $r_C$. It is plausible that there are such regions $z$. Take region $r_A$. Suzy is entirely located at it but not at any of its proper parts. And $r_A$ overlaps $r_C$. So every part of $r_A$ at which Suzy is entirely located $(r_A$ alone) overlaps $r_C$. Or consider some proper superregion of $r_A$—call it $r_A^+$—that does not have $r_B$ as a part. Again every part of $r_A^+$ at which Suzy is entirely located (every part of $r_A^+$ that has $r_A$ as a part) overlaps $r_C$.

Now we turn to System 4’s treatment of Pointy objects in gunky space. The point-like object $o_p$ is entirely located at many regions. But—in light of the gunky structure of space in this case—every region at which it is entirely located has other such regions as proper parts. So, by (DS4.1), $o_p$ is not exactly located anywhere, as desired. (DS4.2) also yields the correct verdict that $o_p$ is *weakly* located at many regions, but we leave this for the reader to show.

Two other cases we considered above might be seen as posing problems for System 4. One is Nested Multilocation. Correia (2022: 567) notes that (DS4.1) rules this out; we leave it for the reader to check.

The second potentially problematic case for System 4 is Almond in the void. As Correia notes, (DS4.1) yields the result that the almond is exactly located at the region. For the almond is entirely located there, and it is not entirely located at any proper part of that region. Correia (2022: 581) embraces this outcome, but some readers may find it implausible.

### System 5: Primitive Plural Pervasive Location

A fifth system of definitions may improve on the four considered so far. The fifth system (adapted with modification from Loss 2019 and 2023) is based on a primitive locative relation that we have not yet mentioned: plural pervasive location. The fifth system also crucially relies on the assumption that regions are located at themselves (Casati & Varzi 1999: 121). Here is an informal gloss of the new relation:

- **Plural pervasive location**: one or more entities $xx$ are plurally pervasively located at region $y$ if and only if:
- $xx$ collectively completely fill $y$,
- each of $xx$ ‘helps’ to fill $y$, that is, each of $xx$ is at least weakly located at $y$, and
- if there is just one of $xx$, then that thing has a size that is at least as great as the size of $y$ (Loss 2019, 2023). In symbols: $\PPL(xx, y)$.

The four locative relations we have considered so far are all, we assume, singular in both argument places. Plural pervasive location, however, has a plural argument place for occupants. Its first argument place can take either a single thing or more things collectively.

For examples, return to Figure 1 in the main text. While neither $o_1$ alone nor $o_2$ alone completely fills $r_3$, taken together $o_1$ and $o_2$ do completely fill it, so $o_1$ and $o_2$ are plurally pervasively located at $r_3$. But one should also allow for singular cases of this same relation: one can say that $o_1$ is plurally pervasively located at $r_1$. Further, one should allow for intuitively ‘overdetermined’ cases of plural pervasive location and say that $o_1$ and $o_3$ are plurally pervasively located at $r_5$—though each one on its own is also plurally pervasively located there. We do not, however, allow for cases in which some objects $xx$ are plurally pervasively located at $y$ even though one of $xx$ is not even weakly located at $y$. For example, although $o_1$ and $o_3$ are plurally pervasively located at $r_5, o_1$ and $o_2$ are not, because $o_2$ is not even weakly located at $r_5$: it does not help to fill it.

The final clause in our gloss of plural pervasive location is needed to ensure that we are attending to a *non-additive* plural pervasive location relation.

Let object $o_m$ be a square, one square meter in area. Suppose that $o_m$ is multilocated: it is exactly located at the square region $r_7$ and also exactly located at the square region $r_8$. These regions do not overlap. The fusion of $r_7$ and $r_8 (r_7 +r_8)$ is a rectangle, two square meters in area. Must $o_m$ be plurally pervasively located at $r_7 +r_8$?

There seem to be two relations in the vicinity of plural pervasive location, and the answer to the foregoing question depends on which relation we are asking about. One of them, call it $\PPL_A$, obeys an additivity principle:

- **$\boldsymbol{\PPL_A}$ Additivity**. For any $x$, any $yy$, and any $z$, if $z$ is a fusion of $yy$ and $x$ is plurally pervasively located$_A$ at each of $yy$, then $x$ is plurally pervasively located$_A$ at $z$.

If our question about $r_7 +r_8$ was about $\PPL_A$, then the answer is ‘Yes’. Object $o_m$ is exactly located at $r_7$, so it is plurally pervasively located there. Likewise, for $r_8$. So, given $\PPL_A$ Additivity, $o_m$ is plurally pervasively located$_A$ at their fusion, $r_7 +r_8$.

However, it seems that we can also grasp a *PPL*-like relation, call it $\PPL_N$, that is not additive in this way. If our question is about $\PPL_N$, then the answer is presumably ‘No’. An object bears $\PPL_N$ only to those regions that are the same size or smaller than the object. When an object is multilocated, it may be exactly located at each of several regions but not at their fusion. Likewise, such an object may be plurally pervasively located$_N$ at each of several regions but not their fusion. This seems to be the case with $o_m$. It is one square meter in area: that is its one and only size. It is not, for example, two square meters in area. The region $r_7 +r_8$, on the other hand, is two square meters in area. Since this is not the same size or smaller than the size of $o_m$, we should say that $o_m$ is not plurally pervasively located$_N$ at $r_7 +r_8$. Object $o$ is not big enough to be plurally pervasively located$_N$ at $r_7 +r_8$.

This completes our preamble. If we invoke the ‘is one of’ predicate from plural logic, symbolized as ‘$\prec$’, then we can state System 5 as follows:

**(DS5.1)**

$x$ is exactly located at $y$ $=_{\df}$ $x$ is plurally pervasively located at $y$ but not at anything that has $y$ as a proper part (Loss 2023). $$L(x, y) =_{\df} \PPL(x, y) \amp \forall z[(\PPL(x, z) \amp P(y, z)) \rightarrow z=y]$$

**(DS5.2)**

$x$ is weakly located at $y$ $=_{\df}$ $x$ is one of some things that are plurally pervasively located at $y$. $$\WKL(x, y) =_{\df} \exists xx[x\prec xx \amp \PPL(xx, y)]$$

Notice that both exact and weak location are defined so that both of their argument positions are singular, though they are defined in term of plural pervasive location. It is also worth noting that while System 5 adopts Loss’s definition of exact location, it does not adopt his complex definition of weak location. The definition we consider here is simpler.

Unlike Systems 1–4, System 5 handles Pointy objects in gunky space, Almond in the void, and Time traveling Suzy. It does not, however, help with Nested Multilocation. We will consider these cases one by one.

Consider first an ordinary case of exact location: for example, object $o_1$ and region $r_1$, as depicted in Figure 1. Object $o_1$ does completely fill $r_1$ all by itself, and it is at least as large as $r_1$, so we should say that $o_1$ is plurally pervasively located at $r_1$. Further, it should be clear that while $o_1$ is plurally pervasively located at other regions (e.g., $r_5$), none of them have $r_1$ as a proper part. So (DS5.1) counts $o_1$ as being exactly located at $r_1$.

Now consider Pointy objects in gunky space. The pointy object $o_p$ does not completely fill any region on its own. It is too small. So, it is not plurally pervasively located at any region, and hence, according to (DS5.1), it is not exactly located at any region. Is $o_p$ weakly located at any region? Well, consider some solid, ball-shaped region $r^*$ with $o_p$ intuitively at its center. Although $o_p$ by itself does not completely fill $r^*$, $o_p$ and $r^*$, collectively, do completely fill $r^*$, given the assumption that regions are located at themselves (Casati & Varzi 1999: 121). So, we should say that $o_p$ and $r^*$ are plurally pervasively located at $r^*$, hence that $o_p$ is one of some things that are plurally pervasively located at $r^*$. In that case, (DS5.2) says that $o_p$ is weakly located at $r^*$, as desired. The pointy object is weakly located at regions such as $r^*$ but not exactly located anywhere.

Almond in the void is handled in a similar fashion. The almond does not completely fill the extended simple region on its own, but the region and the almond, taken together, do fill the region. So, the almond is weakly but not exactly located at the region.

Now consider Time traveling Suzy. We wanted to be able to say that Suzy is exactly located at the adult-sized region $r_A$ and also at the baby-sized region $r_B$. Start with $r_A$. Suzy on her own completely fills $r_A$, and her size is at least as great as the size of $r_A$. Parallel remarks go for $r_B$. So, Suzy is plurally pervasively located at $r_A$ and also at $r_B$. Is she plurally pervasively located at anything that has $r_A$ as a proper part?

It is tempting to suggest that Suzy is plurally pervasively located at the fusion of $r_A$ and $r_B, r_A +r_B$. In some sense, she does completely fill $r_A +r_B$. However, she is not big enough to fill that fusion in the relevant sense. To be plurally pervasively located at $r_A +r_B$, Suzy must have a size that is at least as great as the size of $r_A +r_B$. Loss would say that Suzy does not have such a size. At most, Suzy has two sizes: the first is her adult volume, $v_A$, and the second is her baby volume, $v_B$. Neither of these sizes is as great as the size of $r_A +r_B$. Crucially, Suzy does *not* have a third size: that of an adult together with a baby. If this is correct, then we should say that Suzy is *not* plurally pervasively located at $r_A +r_B$ or (for parallel reasons) at any other region that has $r_A$ as a proper part. And in that case, (DS5.1) counts Suzy as being exactly located at $r_A$. Parallel remarks go for $r_B$. So System 5 allows us to say that Suzy is exactly located at $r_A$ and also at the disjoint region $r_B$.

Finally, consider Nested Multilocation. Here System 5 offers us no help. The desired result was that a single thing, Clifford (which is identical to Odie), is exactly located at two regions, one of which is a proper part of the other. This is immediately ruled out by (DS5.1). The table below sums up the results.

| *System* | *Pointy objects in gunky space* | *Almond in the void* | *Time traveling Suzy* | *Nested multilocation* |
| --- | --- | --- | --- | --- |
| 1. *Prim. Exact Loc.* | No | No | Yes | Yes |
| 2. *Prim. Weak Loc., Parsons-style* | Yes | No | No | No |
| 3. *Prim. Weak Loc., Eagle-style* | Yes | No | Problematic | No |
| 4. *Prim. Entire Loc.* | Yes | No | Yes | No |
| 5. *Prim. Plural Pervasive Loc.* | Yes | Yes | Yes | No |
