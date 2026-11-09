# nonwellfounded-set-theory — self-similar-sets（supplement）

> （《nonwellfounded-set-theory》词条补充材料，源：plato.stanford.edu/entries/nonwellfounded-set-theory/self-similar-sets.html）

#### Supplement to Non-wellfounded Set Theory

## A few points concerning self-similar sets of real numbers

Discussions of circularity rarely touch on *self-similar* sets in the usual sense, mostly because the mathematics involved seems so different. We want to raise the topic here because in recent years it has become clear that there really are commonalities.

Probably most readers have seen pictures of sets such as the Mandelbrot set, sets of points in the plane which exhibit self-similarity. Clearly there is nothing problematic about such sets. A picture of a self-similar set doesn't manifest object circularity because the picture is not a “part” of itself in any problematic sense. On the other hand, there is a sense in which a self-similar set does exhibit collection similarity. To clarify this, it makes sense to consider a simpler example, the *Cantor (middle-third) set*.

The Cantor set *c* is a certain subset of the set of real numbers between 0 and 1. It has several equivalent definitions/characterizations:

1. Take the unit interval [0,1], then remove the open middle third (1/3, 2/3), leaving two disconnected pieces. For each of those, remove the open middle third. Keep going for infinitely many steps. Then *c* is what remains “at the end”.
2. *c* is the set of numbers possessing a ternary (base 3) decimal expansion with no 1's.
3. *c* is the unique non-empty compact subset of the unit interval [0,1] such that c = c/3 ∪ 2/3 + c/3, where c/3 denotes the set {x/3 : x ∈ c}, and 2/3 + c/3 denotes the same set, with each point increased by 2/3.

The first characterization involves recursion in a certain way, though it is different from recursion on numbers.

The second point gives another interesting characterization, one which is not relevant to our discussion. We mention it only to underscore the point that important objects frequently have more than one description.

The last point is one that really does appear as collection circularity: it defines a set in terms of itself. This kind of definition does not always define a set uniquely, and so it calls out for an analysis.

In another supplement, presented [ at the end of this entry](nonwellfounded-set-theory.modeling-circularity.md), we indicate why commonalities in the mathematics behind the diverse set of examples which we have seen. From streams to sets to fractals, there are similar principles at work.
