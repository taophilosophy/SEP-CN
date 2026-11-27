# time-travel-phys — toy-models（supplement）

> （《time-travel-phys》词条补充材料，源：plato.stanford.edu/entries/time-travel-phys/toy-models.html）

#### Supplement to Time Travel and Modern Physics

## Remarks and Limitations on the Toy Models

The two toy models presented above have the virtue of being mathematically tractable, but they involve certain simplifications and potential problems that lead to trouble if one tries to make them more complicated. Working through these difficulties will help highlight the conditions we have made use of.

Consider a slight modification of the first simple model proposed to us by Adam Elga. Let the particles have an *electric charge*, which produces forces according to Coulomb’s law. Then set up a situation like that depicted in figure S1:

![a diagram: link to extended description below](../assets/time-travel-phys/figure-s1.svg)

*Figure S1:* Set-up for Elga’s Paradox. [An extended description of figure S1 is in the supplement.]

The dotted line indicates the path the particle will follow if no forces act upon it. The point labeled *P* is the left edge of the time-travel region; the two labels are a reminder that the point at the bottom and the point at the top are one and the same.

Elga’s paradox is as follows: if no force acts on the particle, then it will enter the time-travel region. But if it enters the time travel region, and hence reappears along the bottom edge, then its later self will interact electrically with its earlier self, and the earlier self will be deflected away from the time-travel region. It is easy to set up the case so that the deflection will be enough to keep the particle from ever entering the time-travel region in the first place. (For instance, let the momentum of the incoming particle towards the time travel region be very small. The mere existence of an identically charged particle inside the time travel region will then be sufficient to deflect the incoming particle so that it never reaches $L+$.) But, of course, if the particle never enters the region at all, then it will not be there to deflect itself….

One might suspect that some complicated collection of charged particles in the time-travel-region can save the day, as it did with our mirror-reflection problem above. But (unless there are infinitely many such particles) this can’t work, as conservation of particle number and linear momentum show. Suppose that some finite collection of particles emerges from $L{-}$ and supplies the repulsive electric force needed to deflect the incoming particle. Then exactly the same collection of particles must be “absorbed” at $L+$. So at all times after $L+$, the only particle there is in the world is the incoming particle, which has now been deflected away from its original trajectory.

The deflection, though, means that the linear momentum of the particle has changed from what is was before $L{-}$. But that is impossible, by conservation of linear momentum. No matter how the incoming particle interacts with particles in the time-travel region, or how those particle interact with each other, total linear momentum is conserved by the interaction. And whatever net linear momentum the time-traveling particles have when they emerge from $L{-}$, that much linear momentum most be absorbed at $L+$. So the momentum of the incoming particle can’t be changed by the interaction: the particle can’t have been deflected. (One could imagine trying to create a sort of “S” curve in the trajectory of the incoming particle, first bending to the left and then to the right, which leaves its final momentum equal to its initial momentum, but moving it over in space so it misses $L+$. However, if the force at issue is repulsive, then the bending back to the right can’t be done. In the mirror example above, the path of the incoming particle can be changed without violating the conservation of momentum because at the end of the process momentum has been transferred to the mirror.)

How does Elga’s example escape our analysis? Why can’t a continuity principle guarantee the existence of a solution here?

The continuity assumption breaks down because of two features of the example: the concentration of the electric charge on a point particle, and the way we have treated (or, more accurately, failed to treat) the point *P*, the edge of $L+$ (and $L{-})$. We have assumed that a point particle either hits $L+$, and then emerges from $L{-}$, or else it misses $L+$ and sails on into the region of space-time above it. This means that the charge on the incoming particle only has two possibilities: either it is transported whole back in time or it completely avoids time travel altogether. Let’s see how it alters the situation to imagine the charge itself to be continuously divisible.

Suppose that, instead of being concentrated at a point, the incoming object is a little stick, with electric charge distributed even across it (figure S2).

![a diagram: link to extended description below](../assets/time-travel-phys/figure-s2.svg)

*Figure S2:* Elga’s Paradox with a Charged Bar. [An extended description of figure S2 is in the supplement.]

Once again, we set things up so that if there are no forces on the bar, it will be completely absorbed at $L+$. But we now postulate that if the bar should *hit* the point *P*, it will fracture: part of it (the part that hits $L+)$ will be sent back in time and the rest will continue on above $L+$. So continuity of a sort is restored: now we have not just the possibility of the whole charge being sent back or nothing, we have the continuum degrees of charge in between.

It is not hard to see that the restoration of continuity restores the existence of a consistent solution. If no charge is sent back through time, then the bar is not deflected and all of it hits $L+$ (and hence is sent back through time). If all the charge is sent back through time, then is incoming bar is deflected to an extent that it misses $L+$ completely, and so no charge is sent back. But if just the right amount of charge is sent back through time, then the bar will be only partially deflected, deflected so that it hits the edge point *P*, and is split into a bit that goes back and a bit that does not, with the bit that goes back being just the right amount of charge to produce just that deflection (figure 11).

![a diagram: link to extended description below](../assets/time-travel-phys/figure-s3.svg)

*Figure S3:* Solution to Elga’s Paradox with a Charged Bar. [An extended description of figure S3 is in the supplement.]

Our problem about conservation of momentum is also solved: the piece of the bar that does not time travel has lower momentum to the right at the end than it had initially, but the piece that does time travel has a higher momentum (due to the Coulomb forces), and everything balances out.

Is it cheating to model the charged particle as a bar that can fracture? What if we insist that the particle is truly a point particle, and hence that its time travel is an all-or-nothing affair?

In that case, we now have to worry about a question we have not yet confronted: what happens if our point particle hits exactly at the point *P* on the diagram? Does it time-travel or not? Confronting this question requires us to face up to a feature of the rather cheap way we implemented time travel in our toy models by cut-and-paste. The way we rejiggered the space-time structure had a rather severe consequence: the resulting space-time is no longer a *manifold*: the topological structure at the point *P* is different from the topological structure elsewhere. Mathematical physicists simply don’t deal with such structures: the usual procedure is to eliminate the offending point from the space-time and thus restore the manifold structure. In this case, that would leave a *bare singularity* at point *P*, an open edge to space-time into which anything could disappear and out of which, for all the physics tells us, anything could emerge.

In particular, if we insist that our particle is a point particle, then if its trajectory should happen to intersect *P* it will simply disappear. What could cause the extremely fortuitous result that the trajectory strikes precisely at *P*? The emergence of some other charged particle, with just the right charge and trajectory, *from* *P* (on $L{-})$. And we are no longer bound by any conservation laws: the bare singularity can both swallow and produce whatever mass or change or momentum we like. So if we insist on point particles, then we have to take account of the singularity, and that again saves the day.

Consideration of these (slightly more complicated) toy models does not replace the proving of theorems, of course. But they do serve to illustrate the sorts of consideration that necessarily come into play when trying to spell out the physics of time travel in all detail. Let us now discuss some results regarding some slightly more realistic models that have been discussed in the physics literature.
