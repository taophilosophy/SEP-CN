# spacetime-holearg — active-passive（supplement）

> （《spacetime-holearg》词条补充材料，源：plato.stanford.edu/entries/spacetime-holearg/active-passive.html）

#### Supplement to The Hole Argument

## Active and Passive Covariance

### Its Importance for the Hole Argument

One of the more perplexing components of the hole argument is the transition from the general covariance of Einstein’s theory to our freedom to spread the metric field with great freedom over the spacetime manifold. The transition is from what is known as a “passive” view of coordinate transformations to an “active” view. It goes something like this:

*Passive view*:

The laws of Einstein’s theory are covariant under arbitrary coordinate transformations. That means that if we perform an arbitrary coordinate transformation, the laws stay the same in form. As a result we are free to use any coordinate transformation we like. The notion of “arbitrary” is mathematically rather imprecise. We need not linger to explicate the delicate matter of just what “arbitrary” may include. For it definitely includes coordinate transformations that are the identity outside some freely chosen neighborhood of the spacetime manifold and then come smoothly to differ from the identity only within. This is a passive form of a hole transformation.

*Active view*:

The formulae used to generate the above coordinate transformation can be used in a very different way. Say the coordinate transformation relabels the point (0,0,0,0) in the old coordinate system with the new label (1,1,1,1). We can also use that transformation within just one coordinate system in the active sense. Then the transformation is used to pick up whatever geometric structures live at the point (0,0,0,0) and redeposit them at the point (1,1,1,1) in the same coordinate sytem. This amounts to a different spreading of the geometrical structures over the spacetime.

### A Toy Example

In Einstein’s general theory of relativity, active redistributions of fields on the manifold will continue to satisfy the defining equations of the theory: Einstein’s field equations. But this is surely not obvious. Rather than plod through the abstract considerations that show this, we will describe an example of the very same transition from passive to active transformations in a greatly simplified case.

To begin, consider the example of a scalar field $f$ spread over a one dimensional manifold; that is, a real line with a coordinate $x$. The field will be represented by the function $f(x)$ in this $x$-coordinate system. The field law of our simple theory is just

$$\tag{AP1} d^2 f(x)/dx^2 = 0. $$

#### Covariance of the Field Equation

Consider the transformation to the new coordinate system

$$\tag{AP2} y = 2x. $$

This is just a relabeling with different coordinates of points in the same one-dimensional space, as shown in the figure:

![A horizontal line has five short vertical tick marks at equal spacing. They are labeled above from left to right as x=0, x=1, x=2, x=3 and x=4; and from below as y=0, y=2, y=4, y=6 and y=8.](../assets/spacetime-holearg/AP_Fig_1.svg)

We also assume that the field $f$ transforms as a scalar, so that the field transforms as

$$ F(y) = f(x). $$

(Say to yourself: “The value of the field $F$ at the point with coordinate $y$ in the new coordinate system is the same as value of the field $f$ in the old coordinate system at point $x$.”)

It is easy to see that this law is covariant under the transformation to the new coordinate system. We have for the differential operators

$$ d/dx = (dy/dx) \cdot (d/dy) = 2 (d/dy) $$

and thus

$$ d^2 /dx^2 = 4 (d^2 /dy^2) $$

By a simple substitution of the differential operator and the scalar transformation rule $F(y) = f(x)$ in (AP1) we arrive at

$$0 = d^2 f(x)/dx^2 = 4 (d^2 F(y)/dy^2) $$

which in turn entails

$$\tag{AP3} d^2 F(y)/dy^2 = 0 $$

This establishes the covariance of the field law (AP1) under the coordinate transformation (AP2); the transformed field law (AP3) has the same form as the original field law (AP1).

#### Passive Transformation

Now let us consider a passive transformation of this field. A simple solution of field law (AP1) in the $x$ coordinate system is

$$\tag{AP4} f(x) = x - 1 $$

![Horizontal x and vertical f(x) coordinate axes, labeled ‘x’ and ‘f(x)’ respectively, are shown as straight lines for the Cartesian plane. The x axis has tick marks at 0, 1, 2, 3 and 4 and the f(x) axis has tick marks at -1, 0, 1 and 2. An oblique straight line passes through points -1 on the vertical axis and 1 on the horizontal axis and is labeled ‘f(x) = x-1’.](../assets/spacetime-holearg/AP_Fig_2.svg)

If we transform this solution to the new coordinate system y by replacing $f(x)$ by $F(y)$ and $x$ by $y/2$, we arrive at

$$\tag{AP5} F(y) = y/2 - 1 $$

![Horizontal y and vertical F(y) coordinate axes, labeled ‘y’ and ‘F(y)’ respectively, are shown as straight lines for the Cartesian plane. The y axis has tick marks at 0, 2, 4, 6, 8 and the F(y) axis has tick marks at -1, 0, 1 and 2. An oblique straight line passes through points -1 on the vertical axis and 2 on the horizontal axis and is labeled ‘F(y)=y/2-1’.](../assets/spacetime-holearg/AP_Fig_3.svg)

This is just the same field as (AP4), but now described in the new coordinate system $y$. To get a sense of the sameness, note that the field (AP2) vanishes at the point $x=1$ in the $x$ coordinate system. The field $F(y)$ vanishes at the point $y=2$. These vanishings happen at the same point in space. It is the point that has coordinate $x=1$ in the $x$ coordinate system and $y=2$ in the $y$ coordinate system.

#### Active Transformation

Now comes the tricky part—pay attention! We have learned a useful mathematical fact through our generation of the field (AP5):

The field $F(y) = y/2 - 1$ solves the field law $d^2 F(y)/dy^2 = 0$

This fact uses the variable “$y$” to designate the coordinate system. Forget for a moment that values of $y$ indicate particular points in the one dimensional space. Just think of it as a mathematical fact about a real valued variable $y$ and function $F$ of it. The mathematical fact remains true if we rewrite it using the label “$x$” instead of “$y$” for the real variable. Then it says:

The field $F(x) = x/2 - 1$ solves the field law $d^2 F(x)/dx^2 = 0$

This mathematic fact can be given a new physical interpretation. Let the variable “$x$” be the $x$ coordinate of our original coordinate system. We have now discovered a *new* field in the original $x$ coordinate system that also satisfies the field equation. That is, we now have the two fields in the original $x$ coordinate system:

The field $f(x) = x - 1$ solves the field law $d^2 f(x)/dx^2 = 0$

The field $F$(x) $= x/2 - 1$ solves the field law $d^2 F(x)/dx^2 = 0$

![Horizontal x and vertical f(x), F(x) coordinate axes are labeled ‘x’ for the horizontal axis and ‘f(x)’ and ‘F(x)’ for the vertical axis. The axes are shown as straight lines for the Cartesian plane. The x axis has tick marks at 0, 1, 2, 3, 4 and the f(x), F(x) axis has tick marks at -1, 0, 1 and 2. An oblique straight line passes through points -1 on the vertical axis and 1 on the horizontal axis and is labeled ‘f(x) = x-1.’ A second oblique straight line passes through -1 on the f(x), F(x) axis and 2 on the x axis and is labeled ‘F(x) = x/2 - 1’.](../assets/spacetime-holearg/AP_Fig_4.svg)

Lest there be any doubt that the two fields are different, note that they are both described in the same coordinate system $x$, but are different functions of $x$. The points at which they vanish are now different. $f(x)$ vanishes at $x=1$ and $F(x)$ vanishes at $x=2$.

What we have done is to use the covariance of the original field law (AP1) to generate a new solution of the field law (AP1). That new solution is generated by taking the field at a point in space with coordinate $x$ and moving it to a new point in space with coordinate $y = 2x$ in the same coordinate system.

![The figure is the same as the previous figure that shows oblique lines labeled f(x) = x -1 and F(x) = x/2 - 1. The only change is the addition of three curved arrows, aligned horizontally, that point from the f(x) = x -1 line to the F(x) = x/2 - 1 line.](../assets/spacetime-holearg/AP_Fig_5.svg)

This use of the transformation (AP2) $y = 2x$ is an active use of the transformation.
