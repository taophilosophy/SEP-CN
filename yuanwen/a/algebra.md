# Algebra
**First published Tue May 29, 2007; substantive revision Thu Nov 3, 2022**

*Pratt, Vaughan*

Algebra is a branch of mathematics sibling to geometry, analysis (calculus), number theory, combinatorics, etc. Although algebra has its roots in numerical domains such as the reals and the complex numbers, in its full generality it differs from its siblings in serving no specific mathematical domain. Whereas geometry treats spatial entities, analysis continuous variation, number theory integer arithmetic, and combinatorics discrete structures, algebra is equally applicable to all these and other mathematical domains.

*Elementary algebra*, in use for centuries and taught in secondary school, is the arithmetic of indefinite quantities or variables $x, y,\ldots$. Whereas the definite sum $3+4$ evaluates to the definite quantity 7, the indefinite sum $x+y$ has no definite value, yet we can still say that it is always equal to $y+x$, or to $x^2 -y^2$ if and only if $x$ is either $-y$ or $y+1$.

Elementary algebra provides finite ways of managing the infinite. A formula such as $\pi r^2$ for the area of a circle of radius $r$ describes infinitely many possible computations, one for each possible valuation of its variables. A universally true law expresses infinitely many cases, for example the single equation $x+y = y+x$ summarizes the infinitely many facts $1+2 = 2+1, 3+7 = 7+3$, etc. The equation $2x = 4$ selects one number from an infinite set of possibilities. And $y = 2x+3$ expresses the infinitely many points of the line with slope 2 passing through $(0, 3)$ with a finite equation whose solutions are exactly those points.

Elementary algebra ordinarily works with real or complex values. However its general methods, if not always its specific operations and laws, are equally applicable to other numeric domains such as the natural numbers, the integers, the integers modulo some integer $n$, the rationals, the quaternions, the Gaussian integers, the $p$-adic numbers, and so on. They are also applicable to many nonnumeric domains such as the subsets of a given set under the operations of union and intersection, the words over a given alphabet under the operations of concatenation and reversal, the permutations of a given set under the operations of composition and inverse, etc. Each such *algebraic structure*, or simply *algebra*, consists of the set of its elements and operations on those elements obeying the laws holding in that domain, such as the set $Z = \{0, \pm 1, \pm 2, \ldots \}$ of integers under the integer operations $x+y$ of addition, $xy$ of multiplication, and $-x$, negation, or the set $2^X$ of subsets of a set $X$ under the set operations $X\cup Y$ of union, $X\cap Y$ of intersection, and $X'$, complement relative to $X$.

The laws are often similar but not identical. For example integer multiplication distributes over addition, $x(y+z) = xy+xz$, but not conversely, for example $2+(3\times 5) = 17$ but $(2+3)\times(2+5) = 35$. In the analogy that makes intersection the set theoretic counterpart of multiplication and union that of addition, intersection distributes over union,

$$ X\cap(Y\cup Z) = (X\cap Y)\cup(X\cap Z), $$

as for the integers, but unlike the integers union also distributes over intersection:

$$ X\cup(Y\cap Z) = (X\cup Y)\cap(X\cup Z). $$

Whereas elementary algebra is conducted in a fixed algebra, *abstract* or *modern algebra* treats classes of algebras having certain properties in common, typically those expressible as equations. The subject, which emerged during the 19th century, is traditionally introduced via the classes of groups, rings, and fields. For example any number system under the operations of addition and subtraction forms an abelian (commutative) group; one then passes to rings by bringing in multiplication, and further to fields with division. The common four-function calculator provides the four functions of the field of reals.

The abstract concept of group in full generality is defined not in terms of a set of numbers but rather as an arbitrary set equipped with a binary operation $xy$, a unary inverse $x^{-1}$ of that operation, and a unit $e$ satisfying certain equations characteristic of groups. One striking novelty with groups not encountered in everyday elementary algebra is that their multiplication need not be abelian: $xy$ and $yx$ can be different! For example the group $S_3$ of the six possible permutations of three things is not abelian, as can be seen by exchanging adjacent pairs of letters in the word *dan*. If you exchange the two letters on the left before the two on the right you get *adn* and then *and*, but if you perform these exchanges in the other order you get *dna* and then *nda* instead of *and*. Likewise the group of 43,252,003,274,489,856,000 operations on Rubik’s cube and the infinite group $SO(3)$ of rotations of the sphere are not abelian, though the infinite group $SO(2)$ of rotations of the circle is abelian. Quaternion multiplication and matrix multiplication is also noncommutative. Abelian groups are often called additive groups and their group operation is referred to as addition $x+y$ rather than multiplication $xy$.

Groups, rings and fields only scratch the surface of abstract algebra. Vector spaces and more generally modules are restricted forms of rings in which the operands of multiplication are required to be a scalar and a vector. Monoids generalize groups by dropping inverse; for example the natural numbers form a monoid but not a group for want of negation. Boolean algebras abstract the algebra of sets. Lattices generalize Boolean algebras by dropping complement and the distributivity laws.

A number of branches of mathematics have found algebra such an effective tool that they have spawned algebraic subbranches. Algebraic logic, algebraic number theory, and algebraic topology are all heavily studied, while algebraic geometry and algebraic combinatorics have entire journals devoted to them.

Algebra is of philosophical interest for at least two reasons. From the perspective of foundations of mathematics, algebra is strikingly different from other branches of mathematics in both its domain independence and its close affinity to formal logic. Furthermore the dichotomy between elementary and abstract algebra reflects a certain duality in reasoning that Descartes, the inventor of Cartesian Dualism, would have appreciated, wherein the former deals with the reasoning process and the latter that which is reasoned about, as respectively the mind and body of mathematics.

Algebra has also played a significant role in clarifying and highlighting notions of logic, at the core of exact philosophy for millennia. The first step away from the Aristotelian logic of syllogisms towards a more algebraic form of logic was taken by Boole in an 1847 pamphlet and subsequently in a more detailed treatise, *The Laws of Thought*, in 1854. The dichotomy between elementary algebra and modern algebra then started to appear in the subsequent development of logic, with logicians strongly divided between the formalistic approach as espoused by Frege, Peano, and Russell, and the algebraic approach followed by C. S. Peirce, Schroeder, and Tarski.

## 1. Elementary algebra

Elementary algebra deals with numerical terms, namely *constants* 0, 1, 1.5, $\pi$, *variables* $x, y,\ldots$, and combinations thereof built with *operations* such as $+$, $-$, $\times$ , $\div$ , $\sqrt{\phantom{x}}$, etc. to form such terms as $x+1, x\times y$ (standardly abbreviated $xy$), $x + 3y$, and $\sqrt{x}$.

Terms may be used on their own in *formulas* such as $\pi r^2$, or in equations serving as *laws* such as $x+y = y+x$, or as *constraints* such as $2x^2 -x+3 = 5x+1$ or $x^2 + y^2 = 1$.

Laws are always true; while they have the same form as constraints they constrain only vacuously in that every valuation of their variables is a solution. The constraint $x^2 +y^2 = 1$ has a continuum of solutions forming a *shape*, in this case a circle of radius 1. The constraint $2x^2 -x+3 = 5x-1$ has two solutions, $x = 1$ or 2, and may be encountered in the solution of *word problems*, or in the determination of the points of intersection of two curves such as the parabola $y = 2x^2 -x+3$ and the line $y = 5x-1$.

### 1.1 Formulas

A formula is a term used in the computation of values by hand or machine. Although some attributes of physical objects lend themselves to direct measurement such as length and mass, others such as area, volume, and density do not and must be computed from more readily observed values with the help of the appropriate formula. For example the area of a rectangle $L$ inches long by $W$ inches wide is given by the formula $LW$ in units of square inches, the volume of a ball of radius $r$ is $4\pi r^3 /3$, and the density of a solid of mass $M$ and volume $V$ is given by $M/V$.

Formulas may be combined to give yet more formulas. For example the density of a ball of mass $M$ and radius $r$ can be obtained by substituting the above formula for the volume of a ball for $V$ in the above formula for the density of a solid. The resulting formula $M/(4\pi r^3 /3)$ is then the desired density formula.

### 1.2 Laws

Laws or identities are equations that hold for all applicable values of their variables. For example the commutativity law

$$ x+y = y+x $$

holds for all real values of $x$ and $y$. Likewise the associativity law

$$ x+(y+z) = (x+y)+z $$

holds for all real values of $x, y$ and $z$. On the other hand, while the law $x/(y/z) = zx/y$ holds for all numerical values of $x$, it holds only for nonzero values of $y$ and $z$ in order to avoid the illegal operation of division by zero.

When a law holds for all numerical values of its variables, it also holds for all expression values of those variables. Setting $x = M, y = 4\pi r^3$, and $z = 3$ in the last law of the preceding paragraph yields $M/(4\pi r^3 /3) = 3M/(4\pi r^3)$. The left hand side being our density formula from the preceding section, it follows from this instance of the above law that its right hand side is an equivalent formula for density in the sense that it gives the same answers as the left hand side. This new density formula replaces one of the two divisions by a multiplication.

### 1.3 Word problems

If Xavier will be three times his present age in four years time, how old is he? We can solve this *word problem* using algebra by formalizing it as the equation $3x = x + 4$ where $x$ is Xavier’s present age. The left hand side expresses three times Xavier’s present age, while the right hand side expresses his age in four years’ time.

A general rule for solving such equations is that any solution to it is also a solution to the equation obtained by applying some operation to both sides. In this case we can simplify the equation by subtracting $x$ from both sides to give $2x = 4$, and then dividing both sides by 2 to give $x = 2$. So Xavier is now two years old.

If Xavier is twice as old as Yvonne and half the square of her age, how old is each? This is more complicated than the previous example in three respects: it has more unknowns, more equations, and terms of higher degree. We may take $x$ for Xavier’s age and $y$ for Yvonne’s age. The two constraints may be formalized as the equations $x = 2y$ and $x = y^2 /2$, the latter being of degree 2 or *quadratic*.

Since both right hand sides are equal to $x$ we can infer $2y = y^2 /2$. It is tempting to divide both sides by $y$, but what if $y = 0$? In fact $y = 0$ is one solution, for which $x = 2y = 0$ as well, corresponding to Xavier and Yvonne both being newborns. Setting that solution to one side we can now look for solutions in which $y$ is not zero by dividing both sides by $y$. This yields $y = 4$, in which case $x = 2y = 8$. So now we have a second solution in which Xavier is eight years old and Yvonne four.

In the absence of any other information, both solutions are legitimate. Had the problem further specified that Yvonne was a toddler, or that Xavier was older than Yvonne, we could have ruled out the first solution.

### 1.4 Cartesian geometry

Lines, circles, and other curves in the plane can be expressed algebraically using *Cartesian coordinates*, named for its inventor Rene Descartes. These are defined with respect to a distinguished point in the plane called the *origin*, denoted $O$. Each point is specified by how far it is to the right of and above $O$, written as a pair of numbers. For example the pair (2.1, 3.56) specifies the point 2.1 units to the right of $O$, measured horizontally, and 3.56 units above it, measured vertically; we call 2.1 the $x$ coordinate and 3.56 the $y$ coordinate of that point. Either coordinate can be negative: the pair $(-5, -1)$ corresponds to the point 5 units to the left of $O$ and 1 unit below it. The point $O$ itself is coordinatized as (0, 0).

*Lines.* Given an equation in variables $x$ and $y$, a point such as (2, 7) is said to be a *solution* to that equation when setting $x$ to 2 and $y$ to 7 makes the equation true. For example the equation $y = 3x+5$ has as solutions the points (0, 5), (1, 8), (2, 11), and so on. Other solutions include (.5, 6.5), (1.5, 9.5), and so on. The set of all solutions constitutes the unique straight line passing through (0, 5) and (1, 8). We then call $y = 3x+5$ the *equation of* that line.

*Circles.* By Pythagoras’s Theorem the square of the distance between two points $(x, y)$ and $(x', y')$ is given by $(x'-x)^2 +(y'-y)^2$. As a special case of this, the square of the distance of the point $(x, y)$ to the origin is $x^2 +y^2$. It follows that those point at distance $r$ from the origin are the solutions in $x$ and $y$ to the equation $x^2 +y^2 = r^2$. But these points are exactly those forming the circle of radius $r$ centered on $O$. We identify this equation with this circle.

*Varieties* The roots of any polynomial in $x$ and $y$ form a curve in the plane called a *one-dimensional variety* of *degree* that of the polynomial. Thus lines are of degree 1, being expressed as polynomials $ax+by+c$, while circles centered on $(x', y')$ are of degree 2, being expressed as polynomials $(x-x')^2 +(y-y')^2 -r^2$. Some varieties may contain no points, for example $x^2 +y^2 +1$, while others may contain one point, for example $x^2 +y^2$ having the origin as its one root. In general however a two-dimensional variety will be a curve. Such a curve may cross itself, or have a cusp, or even separate into two or more components not connected to each other.

*Space* The two-dimensional plane is generalized to three-dimensional space by adding to the variables $x$ and $y$ a third variable $z$ corresponding to the third dimension. The conventional orientation takes the first dimension to run from west to east, the second from south to north, and the third from below to above. Points are then triples, for example the point $(2, 5, -3)$ is 2 units to the east of the origin, 5 units to the north of it, and 3 units below it.

*Planes and spheres*. These are the counterparts in space of lines and circles in the plane. An equation such as $z = 3x + 2y$ defines not a straight line but rather a flat plane, in this case the unique plane passing through the points (0, 1, 2), (1, 0, 3), and (1, 1, 5). And the sphere of radius $r$ centered on the origin is given by $x^2 +y^2 +z^2 = r^2$. The roots of a polynomial in $x, y$ and $z$ form a surface in space called a two-dimensional variety, of degree that of the polynomial, just as for one-dimensional varieties. Thus planes are of degree 1 and spheres of degree 2.

These methods generalize to yet higher dimensions by adding yet more variables. Although the geometric space we experience physically is limited to three dimensions, conceptually there is no limit to the number of dimensions of abstract mathematical space. Just as a line is a one-dimensional subspace of the two-dimensional plane, and a plane is a two-dimensional subspace of three-dimensional space, each specifiable with an equation, so is a *hyperplane* a three-dimensional subspace of four-dimensional space, also specifiable with an equation such as $w = 2x - 7y + z$.

## 2. Abstract Algebra

Elementary algebra fixes some domain, typically the reals or complex numbers, and works with the equations holding within that domain. *Abstract* or *modern algebra* reverses this picture by fixing some set $A$ of equations and studying those domains for which those equations are identities. For example if we take the set of all identities expressible with the operations of addition, subtraction, and multiplication and constants 0 and 1 that hold for the integers, then the algebras in which those equations hold identically are exactly the commutative rings with identity.

Historically the term modern algebra came from the title of the first three editions of van der Waerden’s classic text of that name, renamed simply “Algebra” for its fourth edition in 1955. Volume 1 treated groups, rings, general fields, vector spaces, well orderings, and real fields, while Volume 2 considered mainly linear algebra, algebras (as vector spaces with a compatible multiplication), representation theory, ideal theory, integral algebraic elements, algebraic functions, and topological algebra. On the one hand modern algebra has since gone far beyond this curriculum, on the other this considerable body of material is already more than what can be assumed as common knowledge among graduating Ph.D. students in mathematics, for whom the typical program is too short to permit mastering all this material in parallel with focusing on their area of specialization.

A core feature of abstract algebra is the existence of domains where familiar laws fail to hold. A striking example is commutativity of multiplication, which as we noted in the introduction need not hold for the multiplication of an arbitrary group, even so simple a group as the six permutations of three letters.

### 2.1 Semigroups

We begin with the concept of a binary operation on a set $X$, namely a function $f: X^2 \rightarrow X$ such that $f(x, y)$ is an element of $X$ for all elements $x, y$ of $X$. Such an operation is said to be *associative* when it satisfies $f(f(x, y), z) = f(x, f(y, z))$ for all $x, y, z$ in $X$.

A *semigroup* is a set together with an associative operation, called the *multiplication* of the semigroup and notated $xy$ rather than $f(x, y)$.

The product $xx$ of an element with itself is denoted $x^2$. Likewise $xxx$ is denoted $x^3$ and so on.

*Examples*

- The set of all nonempty words over a given alphabet under the operation of concatenation.
- The set of all functions $f: X \rightarrow X$ on a set $X$ under the operation of function composition.
- The set of integer $n\times n$ matrices under matrix multiplication, for a fixed positive integer $n$.

Concatenation $uv$ of words $u, v$ is associative because when a word is cut into two, the concatenation of the two parts is the original word regardless of where the cut is made. The concatenation of **al** and **gebra** is the same as that of **algeb** and **ra**, illustrating associativity of concatenation for the case $x = $ **al**, $y =$ **geb**, $z =$ **ra**.

Composition $f\cdot g$ of two functions $f$ and $g$ is associative via the reasoning

$$\begin{align*} (f\cdot(g\cdot h))(x) &= f((g\cdot h)(x)) \\ &= f(g(h(x))) \\ &=(f\cdot g)(h(x)) \\ &=((f\cdot g)\cdot h)(x) \end{align*}$$

for all $x$ in $X$, whence $f\cdot(g\cdot h) = (f\cdot g)\cdot h$.

A semigroup $H$ is a *subsemigroup* of a semigroup $G$ when $H$ is a subset of $G$ and the multiplication of $G$ restricted to $H$ coincides with that of $H$. Equivalently a subsemigroup of $G$ is a subset $H$ of $G$ such that for all $x, y$ in $H, xy$ is in $H$.

*Examples*

- The semigroup of all nonempty words over a given alphabet has as a subsemigroup the words of even length; however the words of odd length do not form a subsemigroup because the concatenation of two odd-length words is not of odd length.
- The semigroup of all functions $f: X \rightarrow X$ on a set $X$ under function composition has as subsemigroups the injective or one-to-one functions, the surjective or onto functions, and the bijections or permutations.

A binary operation is called *commutative* when it satisfies $f(x, y) = f(y, x)$ for all $x, y$ in $X$. A *commutative semigroup* is a semigroup whose operation is commutative. All the examples so far have been of noncommutative semigroups. The following illustrate the commutative case.

*Examples*

- The set of positive integers under addition.
- The set of all integers under addition.
- The set of words on a one-letter alphabet under concatenation.
- The set $\{0, 1\}$ of bits (binary digits) under any of the operations AND, OR, XOR.
- The set $2^X$ of subsets of a fixed set $X$ under any of the set theoretic operations intersection, union, symmetric difference.
- The set of vectors in the upper right quadrant of the plane under vector addition.
- The same but omitting the origin.
- The set of all three-dimensional vectors under vector addition.
- The set of polynomials in one variable $x$ with integer coefficients under polynomial addition.
- The set of integer $m\times n$ matrices under matrix addition, for fixed positive integers $m,n$.

An element $x$ of $X$ is a *left identity* for $f$ when $f(x, y) = y$ for all $y$ in $X$, and a *right identity* when $f(y, x) = y$ for all $y$ in $X$. An *identity* for $f$ is an element that is both a left identity and a right identity for $f$. An operation $f$ can have only one identity, because when $x$ and $y$ are identities they are both equal to $f(x,y)$.

A *monoid* is a semigroup containing an identity for the multiplication of the semigroup, notated 1.

*Examples*

- The identity for concatenation is the empty word. Hence words under concatenation form a monoid when the empty word is allowed.
- The identity for addition is zero, or the origin in the case of vector addition. Hence any of the above examples of semigroups for which the operation is addition forms a monoid if and only if it contains zero.
- The identity for composition is the identity function $1_X : X \rightarrow X$ defined as $1_X (x) = x$ for all $x$ in $X$, whence the semigroup of all functions on a set $X$ forms a monoid.

A monoid $H$ is a *submonoid* of a monoid $G$ when it is a subsemigroup of $G$ that includes the identity of $G$.

### 2.2 Groups

When two elements $x, y$ of a monoid satisfy $xy = 1$ we say that $x$ is the left inverse of $y$ and $y$ is the right inverse of $x$. An element $y$ that is both a left and right inverse of $x$ is called simply an inverse of $x$.

A *group* is a monoid every element of which has an inverse.

The cardinality of a group is traditionally referred to as its *order*. A group element $g$ is said to be of order $n$ when $n$ is the least positive integer for which $g^n = 1$.

*Examples*

- The monoid of integers under addition, because every integer $x$ has inverse $-x$.
- The set $\{0, 1\}$ of bits (binary digits) under the operation $\XOR$, because each bit is its own inverse: $0 \XOR 0 = 1 \XOR 1 = 0$. This is just the case $n = 2$ of the monoid $\{0,1,2,\ldots,n-1\}$ of integers mod(ulo) $n$ under addition mod $n$ (e.g. $3 + 4 = 2$ (mod 5)). Here 0 is its own inverse and the inverse of $m$ when nonzero is $n - m$.
- The monoid $S_X$ of bijections or permutations $f: X \rightarrow X$ under composition, because every permutation has an inverse $f^{-1}$. When $X$ has $n$ elements $S_n$ is of order $n!$. $S_n$ is abelian if and only if $n \le 2$.
- The monoid of rotations of the plane about a point under composition, because every rotation can be reversed. This group is called the circle group, denoted SO(2).
- The monoid of rotations of three-dimensional space about a point under composition, again because every rotation can be reversed. This group is denoted SO(3).
- The monoid of symmetries (rotations and reflections) of the regular $n$-gon about its center that carry the $n$-gon into itself, again by reversibility. This group is called the *dihedral group* $D_n$, and is of order $2n$. Like $S_n, D_n$ is abelian if and only if $n \le 2$; in particular $D_3 = S_3$.

A *subgroup* of a group $G$ is a submonoid of $G$ closed under inverses. The monoids of natural numbers and of even integers are both submonoids of the monoid of integers under addition, but only the latter submonoid is a subgroup, being closed under negation, unlike the natural numbers.

An *abelian group* is a group whose operation is commutative. The group operation of an abelian group is conventionally referred to as addition rather than multiplication, and abelian groups are sometimes called additive groups.

A *cyclic* group is a group $G$ with an element $g$ such that every element of $G$ is of the form $g^i$ for some positive integer $i$. Cyclic groups are abelian because $g^{i}g^j = g^{i + j} = g^j g^{i}$. The group of integers under addition, and the groups of integers mod $n$ for any positive integer $n$, all form cyclic groups, with 1 as a generator in every case. All cyclic groups are isomorphic to one of these. There are always other generators when the group is of order 3 or more, for example $-1$, and for groups of prime order every nonzero element is a generator.

### 2.3 Rings

A *ring* is an abelian group that is also a monoid by virtue of having a second operation, called the *multiplication* of the ring. Zero *annihilates*, meaning that $0x = x0 = 0$. Furthermore multiplication distributes over addition (the group operation) in both arguments. That is, $x(y+z) = xy + xz$ and $(x+y)z = xz + yz$.

*Examples*

- The additive group of integers expanded with the operation of integer multiplication.
- The additive group of polynomials in one variable $x$ with integer coefficients expanded with  polynomial multiplication.
- The additive group of integer $n\times n$ matrices, for a fixed positive integer *n,* expanded with matrix multiplication.
- The group of numbers of the form $a+b\sqrt{2}$ where $a$ and $b$ are integer, because $(a+b\sqrt{2})(c+d\sqrt{2}) = ac+2bd+(bc+ad)\sqrt{2}$.
- The group of integers mod $n$ for $n \ge 2$, because $(x+an)(y+bn) = xy + (xb + ya + abn)n$.

In all but the last example, the integers (other than the integer $n$ giving the size of the matrices) may be replaced by any of the rationals, the reals, or the complex numbers. When replacing the integers with the reals the fourth example becomes simply the ring of reals because even if $b$ is zero $a$ can be any real. However when replacing with the rational numbers the ring includes the rationals, but is more than that because $\sqrt{2}$ is irrational, yet it does not contain for example $\sqrt{3}$.

### 2.4 Fields

A *field* is a ring for which the multiplicative monoid of nonzero ring elements is an abelian group. That is, multiplication must be commutative, and every nonzero element $x$ must have a reciprocal $1/x$.

*Examples*

- The ring of rationals, because rational multiplication is commutative and every nonzero rational $m/n$ has reciprocal $n/m$.
- The ring of reals, and the ring of complex numbers, for the analogous reasons.
- The ring of numbers of the form $a+b\sqrt{2}$ where $a$ and $b$ are rational, because $a+b\sqrt{2}$ is zero only when $a=b=0$, and otherwise has reciprocal $(a-b\sqrt{2})/(a^2 -2b^2 )$; called the field of *quadratic irrationals*.
- The ring $Z_p$ of integers modulo a prime $p$, because the multiplicative monoid of nonzero numbers includes a number $g$ such that $g^{p-1} = 1$ and every nonzero number has the form $g^i$ for some integer $i$, and hence has an inverse, namely $g^{p-1-i}$.

The last example does not generalize directly to other moduli. However for any modulus that is a power $p^n$ of a prime, it can be shown that there exists a unique multiplication making the group $Z_{p^n}$ a ring in a way that makes the nonzero elements of the ring a cyclic (and therefore abelian) group under the multiplication, and hence making the ring a field. The fields constructed in this way are the only finite fields.

### 2.5 Applications

Why study entire classes? Well, consider for example the set $Z$ of integers along with the binary operation of addition $x+y$, the unary operation of negation $-x$, and the constant 0. These operations and the constant satisfy various laws such as $x+(y+z) = (x+y)+z, x+y = y+x, x+0 = x$, and $x+(-x) = 0$. Now consider any other algebra with operations that not only have the same names but also satisfy the same laws (and possibly more), called a *model* of those laws. Such an algebra could serve any of the following purposes.

(i) It could tell us to what extent the equational laws holding of the integers characterize the integers. Since the set $\{0, 1\}$ of integers mod 2 under addition and negation satisfies all the laws that the integers do, we immediately see that no single equational property of the integers tells us that there are infinitely many integers. On the other hand any finite model of the equational theory of the integers necessarily satisfies some law that the integers don’t satisfy, in particular the law $x+x+\ldots +x = 0$ where the number of $x$$s$ on the left hand side is the size of the model. Since the equational theory of the integers contains no such law we can tell from its theory as a whole that the integers must be an infinite set. On the other hand the rational numbers under addition and negation satisfy exactly the same equational properties as the integers, so this theory does not characterize the algebra of integers under addition and subtraction with sufficient precision to distinguish it from the rationals.

(ii) It could provide us with a useful new domain that can be substituted for the integers in any application depending only on equational properties of the integers, but which differs from the integers in other (necessarily nonequational) useful respects. For example the rationals, which satisfy the same laws as we just noted, differ in having the *density* property, that between any two rationals there lies another rational. Another difference is that it supports division: whereas the ratio of two integers is usually not an integer, the ratio of two rationals is always a rational. The reals also satisfy the same equations, and like the rationals are dense and support division. Unlike the rationals however the reals have the *completeness* property, that the set of all upper bounds of any nonempty set of reals is either empty or has a least member, needed for convergent sequences to have a limit to converge to.

This idea extends to other operations such as multiplication and division, as with fields. A particularly useful case of such a generalization is given by the use of complex numbers in Cartesian geometry. When $x$ and $y$ range over the field of reals, $x^2 +y^2 =1$ describes the ordinary Euclidean circle in two dimensions, but when the variables range over the complex numbers this equation describes the complex counterpart of the circle, visualizable as a two-dimensional surface embedded in four real dimensions (regarding the complex plane as having two real dimensions). Or if the variables range over the integers mod 7, which form a field under the usual arithmetic operations mod 7, the circle consists of eight points, namely $(\pm 1, 0), (0, \pm 1)$, and $(\pm 2, \pm 2)$. Certain theorems about the Euclidean circle provable purely algebraically remain provable about these other kinds of circles because all the equations on which the proof depends continue to hold in these other fields, for example the theorem that a line intersects a circle in at most two points.

(iii) It could help us decide whether some list of equational laws intended to axiomatize the integers is *complete* in the sense that any equation holding of the integers follows from the laws in that list. If some structure satisfies all the axioms in the list, but not some other equation that holds of the integers, then we have a witness to the incompleteness of the axiomatization. If on the other hand we can show how to construct any algebra satisfying the axioms from the algebra of integers, limiting ourselves only to certain algebraic constructions, then by a theorem of Birkhoff applicable to those constructions we can infer that the axiomatization is complete.

(iv) It could give another of way of defining a class, besides the standard way of listing axioms. In the case at hand, the class of all algebras with a constant, a unary operation, and a binary operation, satisfying all the laws satisfied by the integers, is exactly the class of abelian groups.

## 3. Universal Algebra

Universal algebra is the next level of abstraction after abstract algebra. Whereas elementary algebra treats equational reasoning in a particular algebra such as the field of reals or the field of complex numbers, and abstract algebra studies particular classes of algebras such as groups, rings, or fields, universal algebra studies classes of classes of algebras. Much as abstract algebra numbers groups, rings, and fields among its basic classes, so does universal algebra count varieties, quasivarieties, and elementary classes among its basic classes of classes.

A *model* of a theory is a structure for which all the equations of that theory are identities. Terms are built up from variables and constants using the operations of the theory. An equation is a pair of terms; it is satisfied by an algebra when the two terms are equal under all valuations of (assignments of values to) the $n$ variables appearing in the terms, equivalently when they denote the same $n$-ary operation. A quasiequation is a pair consisting of a finite set of equations, called the premises or antecedents, and another equation, the conclusion; it is satisfied by an algebra when the two terms of the conclusion are equal under all valuations of the $n$ variables appearing in the terms satisfying the premises. A first order formula is a quantified Boolean combination of relational terms.

A *variety* is the class of all models of a set of equations. A *quasivariety* is the class of all models of a set of quasiequations. An *elementary class* is the class of all models of a set of first-order formulas.

Quasivarieties have received much less attention than either varieties or elementary classes, and we accordingly say little about them here. Elementary classes are treated in sufficient depth elsewhere in this encyclopedia that we need not consider them here. We therefore focus in this section on varieties.

Abelian groups, groups, rings, and vector spaces over a given field all form varieties.

A central result in this area is the theorem that a lattice arises as the lattice of subalgebras of some algebra if and only if it arises as the lattice of congruences on some algebra. Lattices of this sort are called *algebraic lattices*. When the congruences of an algebra permute, its congruence lattice is modular, a strong condition facilitating the analysis of finite algebras in particular.

### 3.1 Concepts

Familiar theorems of number theory emerge in algebraic form for algebras. An algebra $A$ is called directly irreducible or *simple* when its lattice of congruences is the two-element lattice consisting of $A$ and the one-element algebra, paralleling the notion of prime number $p$ as a number whose lattice of divisors has two elements $p$ and 1. However the counterpart of the fundamental theorem of arithmetic, that every positive integer factors uniquely as a product of primes, requires a more delicate kind of product than direct product. Birkhoff’s notion of subdirect product enabled him to prove the Subdirect Representation Theorem, that every algebra arises as the subdirect product of its subdirectly irreducible quotients. Whereas there are many subdirectly irreducible groups, the only subdirectly irreducible Boolean algebra is the initial or two-element one, while the subdirectly irreducible rings satisfying $x^n = x$ for some $n \gt 1$ are exactly the finite fields.

Another central topic is duality: Boolean algebras are dual to Stone spaces, complete atomic Boolean algebras are dual to sets, distributive lattices with top and bottom are dual to partially ordered sets, algebraic lattices are dual to semilattices, and so on. Duality provides two ways of looking at an algebra, one of which may turn out to be more insightful or easier to work with than the other depending on the application.

The structure of varieties as classes of all models of some equational theory is also of great interest. The earliest result in this area is Birkhoff’s theorem that a class of algebras is a variety if and only if it is closed under formation of quotients (homomorphic images), subalgebras, and arbitrary (including empty and infinite) direct products. This “modern algebra” result constitutes a completeness theorem for equational logic in terms of its models. Its elementary counterpart is the theorem that the equational theories on a free algebra $F(V)$, defined as the deductively closed sets of equations that use variables from $V$, are exactly its substitutive congruences.

A locally finite variety is one whose finitely generated free algebras are finite, such as pointed sets, graphs (whether of the directed or undirected variety), and distributive lattices. A congruence permutable variety is a variety all of whose algebras are congruence permutable. Maltsev characterized these in terms of a necessary and sufficient condition on their theories, namely that $F$(3) contain an operation $t(x, y, z)$ for which $t(x, x, y) = t(y, x, x) = y$ are in the theory. Analogous notions are congruence distributivity and congruence modularity, for which there exist analogous syntactic characterizations of varieties of algebras with these properties. A more recently developed power tool for this area is McKenzie’s notion of tame congruences, facilitating the study of the structure of finite algebras.

Within the algebraic school, varieties have been defined with the understanding that the operations of a signature form a set. Insights from category theory, in particular the expression of a variety as a monad, defined as a monoid object in the category $C^C$ of endofunctors of a category $C$ (Set in the case of ordinary universal algebra) indicate that a cleaner and more general notion of variety is obtained when the operations can form a proper class. For example the important classes of complete semilattices, CSLat, and complete atomic Boolean algebras, CABA, form varieties only with this broader notion of signature. In the narrow algebraic sense of variety, the dual of a variety can never be a variety, whereas in the broader monadic notion of variety, the variety Set of sets is dual to CABA while CSLat is self-dual.

### 3.2 Equational Logic

*Axiom systems.* Identities can also be used to transform equations to equivalent equations. When those equations are themselves identities for some domain, the equations they are transformed into remain identities for that domain. One can therefore start from some finite set of identities and manufacture an unlimited number of new identities from them.

For example if we start from just the two identities $(x+y)+z = x+(y+z)$ and $x+y = y+x$, we can obtain the identity $(w+x)+(y+z) = (w+y)+(x+z)$ via the following series of transformations.

$$\begin{align*} (w+x)+(y+z) &= ((w+x)+y)+z \\ &=(w+(x+y))+z \\ &=(w+(y+x))+z \\ &=((w+y)+x)+z \\ &=(w+y)+(x+z) \end{align*}$$

This process of manufacturing new identities from old is called *deduction*. Any identity that can be generated by deduction starting from a given set $A$ of identities is called a *consequence* of $A$. The set of all consequences of $A$ is called the *deductive closure* of $A$. We refer to $A$ as an *axiomatization* of its deductive closure. A set that is its own deductive closure is said to be *deductively closed*. It is straightforward to show that *a set is deductively closed if and only if it is the deductive closure of some set*.

An *equational theory* is a deductively closed set of equations, equivalently the set of all consequences of some set $A$ of equations. Every theory always has itself as its own axiomatization, but it will usually also have smaller axiomatizations. A theory that has a finite axiomatization is said to be *finitely based* or *finitely axiomatizable*.

**Effectiveness.** Finitely based theories can be effectively enumerated. That is, given a finite set $A$ of equations, one can write a computer program that prints consequences of $A$ for ever in such a way that every consequence of $A$ will appear at some finite position in the infinite list of all consequences. The same conclusion obtains when we weaken the requirement that $A$ be finite to merely that it can be effectively enumerated. That is, if the axiomatization is effectively enumerable so is its deductive closure.

(In reconciling the finite with the infinite, bear in mind that if we list all the natural numbers 0, 1, 2, … in order, we obtain an infinite list every member of which is only finitely far from the beginning, and also has a well-defined predecessor (except for 0) and successor. Only if we attempt to pad this list out at the “end” with infinite numbers does this principle break down.

One way to visualize there being an “end” that could have more elements beyond it is to consider the rationals of the form $1/n$ for all nonzero integers $n$, in increasing order. This list starts out $-1/1, -1/2, -1/3,\ldots$ and after listing infinitely many negative rationals of that form, with no greatest such, switches over to positive rationals, with no first such, finally ending with 1/3, 1/2, 1/1. The entire list is discrete in the sense that every rational except the endpoints $-1/1$ and 1/1 has a well-defined predecessor and successor in this subset of the rationals, unlike the situation for the set of all rationals between $-1/1$ and $1/1$. This would no longer be the case were we to introduce the rational 0 “in the middle”, which would have neither a predecessor nor a successor.)

**Equational Logic.** Our informal account of deduction can be formalized in terms of five rules for producing new identities from old. In the following, $s$ and $t$ denote arbitrary terms.

(*R*1)

From nothing infer $t = t$.

(*R*2)

From $s = t$ infer $t = s$.

(*R*3)

From $s = t$ and $t = u$ infer $s = u$.

(*R*4)

From $s_1 = t_1, s_2 = t_2 , \ldots ,s_n = t_n$ infer $f(s_1, s_2 , \ldots ,s_n)= f(t_1, t_2 , \ldots ,t_n)$, where $f$ is an $n$-ary operation.

(*R*5)

From $s = t$ infer $s' = t'$ where $s'$ and $t'$ are the terms resulting from consistently substituting terms for variables in $s$ and $t$ respectively.

“Consistently” in this context means that if a term is substituted for one occurrence of a given variable, the same term must be substituted for all occurrences of that variable in both $s$ and $t$. We could not for example appeal solely to *R*5 to justify substituting $u+v$ for $x$ in the left hand side of $x+y = y+x$ and $v+u$ for $x$ in the right hand side, though some other rule might permit it.

An equational theory as a set of pairs of terms amounts to a binary relation on the set of all terms. Rules *R*1–*R*3 correspond to respectively reflexivity, symmetry, and transitivity of this binary relation, $i.e$. these three rules assert that an equational theory is an *equivalence relation*. Rule *R*4 expresses the further property that this binary relation is a *congruence*. Rule *R*5 further asserts that the relation is a substitutive congruence. It can be shown that a binary relation on the set of terms is an equational theory if and only if it is a substitutive congruence. These five rules therefore completely axiomatize equational logic in the sense that every consequence of a set $A$ of equations can be produced from $A$ via finitely many applications of these five rules.

### 3.3 Birkhoff’s Theorem

A variety is by definition the class of models of some equational theory. In 1935 Birkhoff provided an equivalent characterization of varieties as any class closed under quotients (homomorphic images), direct products, and subalgebras. These notions are defined as follows.

Given two algebras $(X, f_1 , \ldots f_k)$ and $(Y, g_1 , \ldots g_k)$, a *homomorphism* $h: (X, f_1 , \ldots f_k) \rightarrow (Y, g_1 , \ldots g_k)$ is a function $h: X \rightarrow Y$ satisfying $h(f_i (x_0 , \ldots ,x_{n_{ i}-1 })) = g_i (h(x_0), \ldots ,h(x_{n_{ i}-1 })))$ for each $i$ from 1 to $k$ where $n_i$ is the arity of both $f_i$ and $g_i$.

A *subalgebra* of an algebra is a set of elements of the algebra closed under the operations of the algebra.

Let $I$ be an arbitrary set, which may be empty, finite, or infinite. A *family* $\langle A_{i}\rangle_{i\in I}$ of algebras $(X_i, f_{1}^i,\ldots, f_k^i)$ indexed by $I$ consists of one algebra $A_i$ for each element $i$ of $I$. We define the *direct product* $\Pi A_i$ (or $\Pi_{i\in I} A_i$ in full) of such a family as follows.

The underlying set of $\Pi A_i$ is the cartesian product $\Pi X_i$ of the underlying sets $X_i$, and consists of those $I$-tuples whose $i$-th element is some element of $X_i$. ($I$ may even be uncountable, but in this case the nonemptiness of $\Pi X_i$ as a consequence of the nonemptiness of the individual $X_i$’s is equivalent to the axiom of choice. This should be kept in mind for any constructive applications of Birkhoff’s theorem.)

The $j$-th operation of $\Pi A_i$, of arity $n_j$, takes an $n_j$-tuple $t$ of elements of $\Pi X_i$ and produces the $I$-tuple $\langle f_{j}^i(t_{1}^i , \ldots t_{n_{ j} }^i)\rangle_{i\in I}$ where $t_k^i$ is the $i$-th component of the $k$-th component of $t$ for $k$ from 1 to $n_j$.

Given two algebras $A$, $B$ and a homomorphism $h: A \rightarrow B$, the *homomorphic image* $h(A)$ is the subalgebra of $B$ consisting of elements of the form $h(a)$ for $a$ in $A$.

Given a class $C$ of algebras, we write $P(C)$ for the class of all algebras formed as direct products of families of algebras of $C, S(C)$ for the class of all subalgebras of algebras of $C$, and $H(C)$ for the class of all homomorphic images of algebras of $C$.

It is relatively straightforward to show that any equation satisfied by all the members of $C$ is also satisfied by all the members of $P(C), S(C)$, and $H(C)$. Hence for a variety $V, P(V) = S(V) = H(V)$.

Birkhoff’s theorem is the converse: for any class $C$ such that $P(C) = S(C) = H(C), C$ is a variety. In fact the theorem is slightly stronger: for any class $C$, *HSP*$(C)$ is a variety. That is, to construct all the models of the theory of $C$ it suffices to close $C$ first under direct products, then under subalgebras, and finally under homomorphic images; that is, later closures do not compromise earlier ones provided $P, S$, and $H$ are performed in that order.

A basic application of Birkhoff’s theorem is in proving the completeness of a proposed axiomatization of a class $C$. Given an arbitrary model of the axioms, it suffices to show that the model can be constructed as the homomorphic image of a subalgebra of a direct product of algebras of $C$.

This completeness technique complements the completeness observed in the previous section for the rules of equational logic.

## 4. Linear Algebra

### 4.1 Vector Spaces

Sibling to groups, rings, and fields is the class of *vector spaces* over any given field, constituting the universes of linear algebra. Vector spaces lend themselves to two opposite approaches: axiomatic or abstract, and synthetic or concrete. The axiomatic approach takes fields (whence rings, whence groups) as a prerequisite; it first defines a notion of $R$-module as an abelian group with a scalar multiplication over a given ring $R$, and then defines a vector space to be an $R$-module for which $R$ is a field. The synthetic approach proceeds via the familiar representation of vector spaces over the reals as $n$-tuples of reals, and of linear transformations from $m$-dimensional to $n$-dimensional vector spaces as $m\times n$ matrices of reals. For the full generality of vector spaces including those of infinite dimension, $n$ need not be limited to finite numbers but can be any cardinal.

The abstract approach, as adopted by such classical texts as Mac Lane and Birkhoff, has a certain purist appeal and is ideally suited to mathematics majors. The concrete approach has the benefit of being able to substitute calculus or less for groups-rings-fields as a prerequisite, suiting it to service courses for scientists and engineers needing only finite-dimensional matrix algebra, which enjoys enormous practical applicability. Linear algebra over other fields, in particular finite fields, is used in coding theory, quantum computing, etc., for which the abstract approach tends to be better suited.

For any field $F$, up to isomorphism there is exactly one vector space over $F$ of any given finite dimension. This is a theorem in the abstract approach, but is an immediate consequence of the representation in the concrete approach (the theorem is used in relating the two approaches).

Another immediate consequence of the concrete approach is duality for finite-dimensional vector spaces over $F$. To every vector space $V$, of any dimension, corresponds its dual space $V^*$ comprised of the *functionals* on $V$, defined as the linear transformations $f: V\rightarrow F$, viewing the field $F$ as the one-dimensional vector space. The functionals form a vector space under coordinatewise addition $(f+g)(u) = f(u)+g(u)$ and multiplication $(xf)(u) = x(f(u))$ by any scalar $x$ in $F$, and we take $V^*$ to be that space. This operation on vector spaces extends to the linear transformations $f: U\rightarrow V$ as $f^* : V^*\rightarrow U^*$ defined such that $f$ maps each functional $g: V\rightarrow F$ to $g\cdot f: U\rightarrow F$. Repeating this operation produces a vector space that, in the finite-dimensional case, is isomorphic to $V$, that is, $V \cong V^{**}$, making the operation an involution. The essence of duality for finite-dimensional vector spaces resides in its involutary nature along with the reversal of the linear transformations.

This duality is easily visualized in the concrete approach by viewing linear transformations from $U$ to $V$ as $m\times n$ matrices. The duality simply transposes the matrices while leaving the machinery of matrix multiplication itself unchanged. It is then immediate that this operation is an involution that reverses maps—the $m\times n$ matrix linearly transforming an $n$-dimensional space $U$ to an $m$-dimensional one $V$ transposes to an $n\times m$ matrix linearly transforming the $m$-dimensional space $V^*$ to the $n$-dimensional space $U^*$.

### 4.2 Associative Algebras

The linear transformations $f: V\rightarrow V$ on a vector space $V$ can be added, subtracted, and multiplied by scalars, pointwise in each case, and hence form a vector space. When the space has finite dimension $n$, the linear transformations are representable as $n\times n$ matrices.

In addition they can be composed, whence they form a vector space equipped with a bilinear associative operation, namely composition. In the finite-dimensional case, composition is just the usual matrix product. Vector spaces furnished with such a product constitute *associative algebras*. Up to isomorphism, all associative algebras arise in this way whether of finite or infinite dimension, providing a satisfactory and insightful characterization of the notion in lieu of an axiomatic characterization, not given here.

Well-known examples of associative algebras are the reals, the complex numbers, and the quaternions. Unlike vector spaces, many nonisomorphic associative algebras of any given dimension greater than one are possible.

A class of associative algebras of interest to physicists is that of the Clifford algebras. Clifford algebras over the reals (which as vector spaces are Euclidean spaces) generalize complex numbers and quaternions by permitting any number of formal quantities $e$ analogous to $i = \sqrt{-1}$ to be adjoined to the field of reals. The common feature of these quantities is that each satisfies either $e^2 = -1$ or $e^2 = 1$. Whereas there are a great many associative algebras of low dimension, only a few of them arise as Clifford algebras. The reals form the only one-dimensional Clifford algebra, while the hyperbolic plane, defined by $e^2 = 1$, and the complex plane, defined by $e^2 = -1$, are the two two-dimensional Clifford algebras. The hyperbolic plane is just the direct square of the real field, meaning that its product is coordinatewise, $(a, b)(c, d) = (ac, bd)$, unlike that of the complex plane where it defined by $(a, b)(c, d) = (ac - bd, ad+bc)$. The two four-dimensional Clifford algebras are the $2\times 2$ matrices and the quaternions. Whereas the $2\times 2$ matrices contain zero divisors (nonzero matrices whose product is zero), and so form only a ring, the quaternions contain no zero divisors and so form a division ring. Unlike the complex numbers however, the quaternions do not form a field because their multiplication is not commutative. Complex multiplication however makes the complex plane a commutative division ring, that is, a field.

## 5. Algebraization of mathematics

A number of branches of mathematics have benefited from the perspective of algebra. Each of algebraic geometry and algebraic combinatorics has an entire journal devoted to it, while algebraic topology, algebraic logic, and algebraic number theory all have strong followings. Many other more specialized areas of mathematics have similarly benefited.

### 5.1 Algebraic geometry

Algebraic geometry begins with what we referred to in the introduction as shapes, for example lines $y = ax +b$, circles $x^2 +y^2 = r^2$, spheres $x^2 +y^2 +z^2 = r^2$, conic sections $f(x, y) = 0$ where $f$ is a quadratic polynomial in $x$ and $y$, quadric surfaces $f(x, y, z) = 0$ with $f$ again quadratic, and so on.

It is convenient to collect the two sides of these equations on the left so that the right side is always zero. We may then define a shape or *variety* to consist of the roots or *zeros* of a polynomial, or more generally the common zeros of a set of polynomials.

Ordinary analytical or Cartesian geometry is conducted over the reals. Algebraic geometry is more commonly conducted over the complex numbers, or more generally over any algebraically closed field. The varieties definable in this way are called *affine varieties*.

Sometimes however algebraic closure is not desirable, for example when working at the boundary of algebraic geometry and number theory where the field may be finite, or the rationals.

Many kinds of objects are characterized by what structure their maps hold invariant. Posets transform via monotone functions, leaving order invariant. Algebras transform via homomorphisms, leaving the algebraic structure invariant. In algebraic geometry varieties transform via *regular* $n$-ary *functions* $f: A^n \rightarrow A$, defined as functions that are locally rational polynomials in $n$ variables. Locally rational means that at each point of the domain of $f$ there exists a neighborhood on which $f$ is the ratio of two polynomials, the denominator of which is nonzero in that neighborhood.

This notion generalizes to regular functions $f: A^n \rightarrow A^m$ defined as $m$-tuples of regular $n$-ary functions.

Given two varieties $V, V'$ in $A^n$ and $A^m$ respectively, a regular function from $A^n$ to $A^m$ whose restriction to $V$ is a function from $V$ to $V'$ is called a *regular function of varieties*. The category of affine varieties is then defined to have as its objects all affine varieties and as its morphisms all regular functions thereof.

Polynomials being continuous, one would expect regular functions between varieties to be continuous also. A difficulty arises with the shapes of varieties, where there can be cusps, crossings, and other symptoms of singularity. What is needed here is a suitable topology by which to judge continuity.

The trick is to work not in affine space but its *projective space*. To illustrate with Euclidean three-space, its associated projective space is the unit sphere with antipodal points identified, forming a two-dimensional manifold. Equivalently this is the space of all (unoriented) lines through the origin. Given an arbitrary affine space, its associated projective space is the space of all such lines, understood as a manifold.

The topology on projective space appropriate for algebraic geometry is the *Zariski topology*, defined not by its open sets but rather by its closed sets, which are taken to be the algebraic sets, namely those sets constituting the common zeros of a set of homogeneous polynomials. The crucial theorem is then that regular maps between affine varieties are continuous with respect to the Zariski topology.

### 5.2 Algebraic number theory

Algebraic number theory has adopted these generalizations of algebraic geometry. One class of varieties in particular that has been of great importance to number theory is that of elliptical curves.

A celebrated success of algebraic number theory has been Andrew Wiles’ proof of Fermat’s so-called “last theorem.” This had remained an open problem for over three and a half centuries.

### 5.3 Algebraic topology

Algebraic topology analyzes the holes and obstructions in connected topological spaces. A topologist is someone who imagines all objects to be made of unbreakable but very pliable playdough, and therefore does not see the need to distinguish between a coffee cup and doughnut because either can be turned into the other. Topology is concerned with the similarities and differences between coffee cups with $n$ handles, surfaces with $n$ holes, and more complicated shapes. Algebraic topology expresses the invariants of such shapes in terms of their homotopy groups and homology groups.

### 5.4 Algebraic logic

Algebraic logic got off to an early start with Boole’s introduction of Boolean algebra in an 1847 pamphlet. The methods of modern algebra began to be applied to Boolean algebra in the 20th century. Algebraic logic then broadened its interests to first order logic and modal logic. Central algebraic notions in first order logic are ultraproducts, elementary equivalence, and elementary and pseudoelementary varieties. Tarski’s cylindric algebras constitute a particular abstract formulation of first order logic in terms of diagonal relations coding equality and substitution relations encoding variables. Modal logic as a fragment of first order logic is made algebraic via Boolean modules.

## 6. Free Algebras

Given any system such as integer arithmetic or real arithmetic, we can write $T$ for the set of all definite terms such as $1 + (2/3)$ built from constants and constituting the definite language, and $T[V]$ for the larger indefinite language permitting variables drawn from a set $V$ in place of some of the constant symbols, with terms such as $x + (2/y)$. When $V$ contains only a single variable $“x”$, $T[\{“x”\}]$ is usually abbreviated to $T[“x”]$ or just $T[x$] which is usually unambiguous. This convention extends to the algebra $\Phi$ of terms of $T$ together with its list of operation symbols viewed as operations for combining terms; we write $\Phi[V$] and call it the *term algebra* on $V$.

This notion of term algebra is a purely syntactic one involving only the operation symbols, constants, and variables of some language. The terms $2 + 3$ and $3 + 2$ are distinct; likewise $x + y$ and $y + x$ are distinct terms. As such they can be considered concrete terms.

Now in a universe such as the integers certain concrete terms are equivalent in the sense that they always evaluate to the same element of the universe regardless of the values of their variable, for example $x + y$ and $y + x$. It is convenient to collect equivalent concrete terms into equivalence classes each of which is to be thought of as an abstract term.

As a simple example of abstract terms consider linear polynomials of the form $ax + by$ where $a$ and $b$ are nonnegative integers, for example $7x + 3y$. The set of all such polynomials includes 0 and is closed under polynomial addition, an associative and commutative operation. This set together with the operation of addition and the zero polynomial therefore constitutes a commutative monoid.

This monoid is an example of a free algebra, namely the free commutative monoid on two generators $x$ and $y$. What makes it free is that it satisfies no laws other than those of a commutative monoid. It is not however a free monoid because it satisfies the commutative law. The free monoid on two generators $x$ and $y$ is instead the set of all finite strings over the two-letter alphabet $\{x,y\}$.

When commutativity is introduced as a law, it identifies the previously distinct strings $xy$ and $yx$ as a single polynomial; more generally any two strings with the same number of $x$s and $y$s are identified.

Free monoids and free commutative monoids are examples of free $C$-algebras where $C$ is a class of algebras. In these two examples the class $C$ is respectively that of monoids and commutative monoids.

A free $C$-algebra is an algebra that lives at the frontier of syntax and semantics. On the semantic side it is a member of $C$. On the syntactic side its elements behave like terms subject to the laws of $C$, but no other laws expressible with its generators. Commutativity $xy = yx$ is expressible with two generators and so a free monoid on two or more generators cannot be commutative, though the free monoid on one generator, namely the set of all finite strings over a one-letter alphabet does form a commutative monoid on one generator.

On the syntactic side, the free $C$-algebra $B$ on a set $X$ arises as a quotient of the term algebra formed from $X$ (viewed as a set of variables) using the operation symbols and constants common to the algebras of $C$. The quotient identifies those terms that have the same value for all algebras $A$ of $C$ and all valuations assigning values in $A$ to the variables of $X$. This performs just enough identifications to satisfy every law of $C$ (thereby making this quotient a $C$-algebra) while still retaining the syntactic essence of the original term algebra in a sense made more precise by the following paragraph.

(Since the concept of a term algebra can seem a little circular in places, a more detailed account may clarify the concept. Given the language of $C$, meaning the operation symbols and constant symbols common to the algebras of $C$, along with a set $X$ of variables, we first form the underlying set of the algebra, and then interpret the symbols of the language as operations on and values in that set. The set itself consists of the terms built in the usual way from those variables and constant symbols using the operation symbols; in that sense these elements are syntactic. But now we change our point of view by treating those elements as semantic, and we look to the constant symbols and operation symbols of the language as syntactic entities needing to be interpreted in this semantic domain (albeit of terms) in order to turn this set of terms into an algebra of terms. We interpret each constant symbol as itself. And we interpret each $n$-ary operation symbol $f$ as the $n$-ary operation that takes any $n$ terms $t_1 , \ldots ,t_n$ as its $n$ arguments and returns the single term $f(t_1 , \ldots ,t_n)$. Note that this interpretation of $f$ only *returns* a term, it does not actually *build* it. All term building was completed when we produced the underlying set of the algebra.)

From the semantic side, a $C$-algebra $B$ together with a subset $X$ of $B$ thought of as variables is said to be a free $C$-algebra on $X$, or is freely generated by $X$, when, given any $C$-algebra $A$, any valuation in $A$ of the variables in $X$ (that is, any function $f: X\rightarrow A$) uniquely extends to a homomorphism $h: B\rightarrow A$. (We say that $h: B\rightarrow A$ extends $f: X\rightarrow A$ when the restriction of $h$ to $X$ is $f$.)

As a convenient shorthand a free $C$-algebra on no generators can also be called an initial $C$-algebra. An initial $C$-algebra has exactly one homomorphism to every $C$-algebra.

Before proceeding to the examples it is worthwhile pointing out an important basic property of free algebras as defined from the semantic side.

*Two free algebras $B, B'$ on respective generator sets $X, Y$ having the same cardinality are isomorphic.*

By way of proof, pick any bijection $f: X\rightarrow Y$. This, its inverse $f': Y\rightarrow X$, and the two identity functions on respectively $X$ and $Y$, form a system of four functions closed under composition. Each of these functions is from a generator set to an algebra and therefore has a unique extension to a homomorphism. These four homomorphisms are also closed under composition. The one from $B$ to itself extends the identity function on $X$ and therefore must be the identity homomorphism on $B$ (since the latter exists and its restriction to $X$ is the identity function on $X)$. Likewise the homomorphism from $G$ to $G$ is an identity function. Hence the homomorphisms between $B$ and $G$ compose in either order to identities, which makes them isomorphisms. But this is what it means for $B$ and $B'$ to be isomorphic.

This fact allows us to say *the* free algebra on a given set, thinking of isomorphic algebras as being “morally” the same. Were this not the case, our quotient construction would be incomplete as it produces a unique free algebra, whereas the above definition of free algebra allows any algebra isomorphic to that produced by the quotient construction to be considered free. Since all free algebras on $X$ are isomorphic, the quotient construction is as good as any, and is furthermore one way of proving that they exist. It also establishes that the choice of set of variables is irrelevant except for its cardinality, as intuition would suggest.

### 6.1 Free monoids and groups

Take $C$ to be the class of monoids. The term algebra determined by the binary operation symbol and the constant symbol for identity can be viewed as binary trees with variables and copies of the constant symbol at the leaves. Identifying trees according to associativity has the effect of flattening the trees into words that ignore the order in which the operation was applied (without however reversing the order of any arguments). This produces words over the alphabet $X$ together with the identity. The identity laws then erase the identities, except in the case of a word consisting only of the identity symbol, which we take to be the empty word.

Thus the monoid of finite words over an alphabet $X$ is the free monoid on $X$.

Another representation of the free monoid on $n$ generators is as an infinite tree, every vertex of which has $n$ descendants, one for each letter of the alphabet, with each edge labeled by the corresponding letter. Each vertex $v$ represents the word consisting of the letters encountered along the path from the root to $v$. The concatenation of $u$ and $v$ is the vertex arrived at by taking the subtree whose root is the vertex $u$, noticing that this tree is isomorphic to the full tree, and locating $v$ in this subtree as though it were the full tree.

If we ignore the direction and labels of the edges in this tree we can still identify the root: it is the only vertex with $n$ edges incident on it, all other vertices have $n+1$, namely the one incoming edge and the $n$ outgoing ones.

The free *commutative* monoid on a set is that monoid whose generators behave like letters just as for free monoids (in particular they are still atoms), but which satisfy the additional law $uv = vu$. We make further identifications, *e.g.* of “dog” and “dgo”. Order of letters in a word is now immaterial, all that matters is how many copies there are of each letter. This information can be represented as an $n$-tuple of natural numbers where $n$ is the size of the alphabet. Thus the free commutative monoid on $n$ generators is $N^n$, the algebra of $n$-tuples of natural numbers under addition.

It can also be obtained from the tree representation of the free monoid by identifying vertices. Consider the case $n = 2$ of two letters. Since the identifications do not change word length, all identifications are of vertices at the same depth from the root. We perform all identifications simultaneously as follows. At every vertex $v$, identify $v_{01}$ and $v_{10}$ and their subtrees. Whereas before there were $2^n$ vertices at depth $n$, now there are $n+1$. Furthermore instead of a tree we have the upper right quadrant of the plane, that is, $N^2$, rotated 135 degrees clockwise, with every vertex $v$ at the top of a diamond whose other vertices are $v_0$ and $v_1$ at the next level down, and the identified pair $v_{01} = v_{10}$ below both.

To form the free group on $n$ generators, first form the free monoid on $2n$ generators, with generators organized into complementary pairs each the inverse of the other, and then delete all adjacent complementary pairs from all words.

This view is not particularly insightful. The group counterpart of the tree representation does a better job of presenting a free group. Consider the free group on $n = 2$ generators $A$ and $B$. We start with the free monoid on 4 generators $A, B, a, b$ where $a$ is the inverse of $A$ and $b$ that of $B$. Every vertex of this tree has 4 descendants. So the root has degree 4 and the remaining vertices have degree 5: every vertex except the root has one edge going in, say the generator $a$, and four out. Consider any nonroot vertex $v$. The effect of deleting adjacent complementary pairs is to identify the immediate ancestor of $v$ with one of the four descendants of $v$, namely the one that makes the path from the ancestor to the descendant a complementary pair. For every nonroot vertex $v$ these identifications reduce the degree of $v$ from 5 to 4. The root remains at degree 4.

So now we have an infinite graph every vertex of which has degree 4. Unlike the tree for the free monoid on 2 generators, where the root is topologically different from the other vertices, the tree for the free group on 2 generators is entirely homogeneous. Thus if we throw away the vertex labels and rely only on the edge labels to navigate, any vertex can be taken as the identity of the group.

This homogeneity remains the case for the free abelian group on 2 generators, whose vertices are still of degree 4. However the additional identifications turns it from a tree (a graph with no cycles) to a grid whose vertices are the lattice points of the plane. That is, the free abelian group on 2 generators is $Z^2$, and on $n$ generators $Z^n$. The edges are the line segments joining adjacent lattice points.

### 6.2 Free rings

With no generators the free monoid, free group, and free ring are all the one-element algebra consisting of just the additive identity 0. A ring with identity means having a multiplicative identity, that is, a word $\varepsilon$. But this makes $\varepsilon$ a generator for the additive group of the ring, and the free abelian group on one generator is the integers. So the free ring with identity on no generators is the integers under addition and now multiplication.

The free ring on one generator $x$ must include $x^2 , x^3$, etc. by multiplication, but these can be added and subtracted resulting in polynomials such as $7x^3 -3x^2 +2x$ but without a constant term, with the exception of 0 itself. The distributivity law for rings means that a term such as $(7x+x^2 )(2x^3 +x)$ can be expanded as $7x^2 +x^3 +14x^4 +2x^5$. It should now be clear that these are just ordinary polynomials with no constant term; in particular we are missing the zero-degree polynomial 1 and so this ring has no multiplicative identity. However it is a commutative ring even though we did not specify this. The free ring with identity on one generator introduces 1 as the multiplicative identity and becomes the ordinary one-variable polynomials since now we can form all the integers. Just as with monoids, the free ring with identity on two generators is not commutative, the polynomials $xy$ and $yx$ being distinct. The free *commutative* ring with identity on two generators however consists of the ordinary two-variable polynomials over the integers.

### 6.3 Free combinatorial structures

From the examples so far one might conclude that all free algebras on one or more generators are infinite. This is by no means always the case; as counterexamples we may point to a number of classes: sets, pointed sets, bipointed sets, graphs, undirected graphs, Boolean algebras, distributive lattices, etc. Each of these forms a locally finite variety as defined earlier.

A pointed set is an algebra with one constant, say $c$. The free pointed set on $x$ and $y$ has three elements, $x, y$, and $c$. A bipointed set is an algebra with two constants $c$ and $d$, and the free bipointed set on $x$ and $y$ then has four elements, $x, y, c$, and $d$.

Graphs, of the oriented kind arising in say automata theory where multiple edges may connect the same two vertices, can be organized as algebras having two unary operations $s$ and $t$ satisfying $s(s(x)) = t(s(x)) = s(x)$ and $t(t(x)) = s(t(x)) = t(x)$. The free graph on one generator $x$ has three elements, $x, s(x)$, and $t(x)$, constituting respectively an edge and its two endpoints or *vertices*. In this framework the vertices are the elements satisfying $s(x) = x$ (and hence $t(x) = x$ since $x = s(x) = t(s(x)) = t(x)$); all other elements constitute edges. The free graph on $n$ generators consists of $n$ such edges, all independent. Other graphs arise by identifying elements. There is no point identifying an edge with either another edge or a vertex since that simply absorbs the first edge into the second entity. This leaves only vertices; identifying two vertices yields a single vertex common to two edges, or to the same edge in the identification $s(x) = t(x)$ creating a self-loop.

The term “oriented” is to be preferred to “directed” because a directed graph as understood in combinatorics is an oriented graph with the additional property that if $s(x) = s(y)$ and $t(x) = t(y)$ then $x = y$; that is, only one edge is permitted between two vertices in a given direction.

Unoriented graphs are defined as for graphs with an additional unary operation $g$ satisfying $g(g(x)) = x$ and $s(g(x)) = t(x)$ (whence $s(x) = s(g(g(x))) = t(g(x)))$. The free undirected graph on $x$ consists of $x, s(x), t(x)$, and $g(x)$, with the pair $x, g(x)$ constituting the two one-way lanes of a two-lane highway between $s(x) = t(g(x))$ and $t(x) = s(g(x)$). Identification of elements of undirected graphs works as for their oriented counterparts: it is only worth identifying vertices. However there is one interesting twist here: vertices can be of two kinds, those satisfying $x = g(x)$ and those not. The latter kind of vertex is now asymmetric: one direction of the bidirectional edge is identified with its vertices while the other one forms an oriented loop in the sense that its other direction is a vertex. This phenomenon does not arise for undirected graphs defined as those satisfying “if $s(x) = s(y)$ and $t(x) = t(y)$ then $x = y$.”

### 6.4 Free logical structures

Boolean algebras are traditionally defined axiomatically as complemented distributive lattices, which has the benefit of showing that they form a variety, and furthermore a finitely axiomatizable one. However Boolean algebras are so fundamental in their own right that, rather than go to the trouble of defining lattice, distributive, and complemented just for this purpose, it is easier as well as more insightful to obtain them from the initial Boolean algebra. It suffices to define this as the two-element set $\{0, 1\}$, the constants (zeroary operations) 0 and 1, and the $2^{2^2} = 16$ binary operations. A Boolean algebra is then any algebra with those 16 operations and two constants satisfying the equations satisfied by the initial Boolean algebra.

An almost-definitive property of the class of Boolean algebras is that their polynomials in the initial Boolean algebra are all the operations on that algebra. The catch is that the inconsistent class consisting of only the one-element or inconsistent algebra also has this property. This class is easily ruled out however by adding that Boolean algebra is consistent. But just barely—adding any new equation to Boolean algebra (without introducing new operations) axiomatizes the inconsistent algebra.

Sheffer has shown that the constants and the 16 operations can be generated as polynomials in just one constant, which can be 0 or 1, and one binary operation, which can be NAND, $\neg(x\wedge y)$, or NOR, $\neg(x\vee y)$. Any such sufficient set is called a *basis*. Along the same lines Stone has shown that conjunction, exclusive-or, and the constant 1 form a basis. The significance of Stone’s basis over Sheffer’s is that Boolean algebras organized with those operations satisfy all the axioms for a commutative ring with identity with conjunction as multiplication and exclusive-or as addition, as well as the law $x^2 = 1$. Any ring satisfying this last condition is called a *Boolean ring*. Boolean rings are equivalent to Boolean algebras in the sense that they have the same polynomials.

An atom of a Boolean algebra is an element $x$ such that for all $y, x\wedge y$ is either $x$ or 0. An atomless Boolean algebra is one with no atoms.

There is exactly one Boolean algebra of cardinality every finite power of 2, and it is isomorphic to the Boolean algebra of a power set $2^X$ of that cardinality under the set operations of union, intersection, and complement relative to $X$. Hence all finite Boolean algebras have cardinality a power of 2. This situation changes with infinite Boolean algebras; in particular countable Boolean algebras exist. One such is the free Boolean algebra on countably many generators, which is the only countable atomless Boolean algebra. The finite and cofinite (complement of a finite set) subsets of the set $N$ of natural numbers form a subalgebra of the powerset Boolean algebra $2^N$ not isomorphic to the free Boolean algebra, but it has atoms, namely the singleton sets.

The free Boolean algebra $F(n)$ on $n$ generators consists of all $2^2 n$ $n$-ary operations on the two-element Boolean algebra. Boolean algebras therefore form a locally finite variety.

The equational theory of distributive lattices is obtained from that of Boolean algebras by selecting as its operations just the monotone binary operations on the two-element algebra, omitting the constants. These are the operations with the property that if either argument is changed from 0 to 1, the result does not change from 1 to 0. A distributive lattice is any model of those Boolean equations between terms built solely with monotone binary operations. Hence every Boolean algebra is a distributive lattice.

Distributive lattices can be arbitrarily “thin.” At the extreme, any chain (linear or total order, $e.g$. the reals standardly ordered) under the usual operations of max and min forms a distributive lattice. Since we have omitted the constants this includes the empty lattice, which we have not excluded here as an algebra. (Some authors disallow the empty set as an algebra but this proscription spoils many good theorems without gaining any useful ones.) Hence there exist distributive lattices of every possible cardinality.

Every finite-dimensional vector space is free, being generated by any choice of basis. This extends to infinite-dimensional vector spaces provided we accept the Axiom of Choice. Vector spaces over a finite field therefore form a locally finite variety when scalar multiplication is organized as one unary operation for each field element.

### 6.5 Free algebras categorially

We now consider how free algebras are organized from the perspective of category theory. We defined the free algebra $B$ generated by a subset $X$ of $B$ as having the property that for every algebra $A$ and every valuation $f: X\rightarrow A$, there exists a unique homomorphism $h: B\rightarrow A$. Now every homomorphism $h: B\rightarrow A$ necessarily arises in this way, since its restriction to $X$, as a function from $X$ to $A$, is a valuation. Furthermore every function $f: X\rightarrow A$ arises as the restriction to $X$ of its extension to a homomorphism. Hence we have a bijection between the functions from $X$ to $A$ and the homomorphisms from $B$ to $A$.

Now the typing here is a little casual, so let us clean it up. Since $X$ is a set while $A$ is an algebra, $f$ is better typed as $f: X\rightarrow U(A)$ where $U(A)$ denotes the underlying set of $A$. And the relationship of $X$ to $B$ is better understood with the notation $B = F(X)$ denoting the free algebra generated by the set $X$. So $U$ maps algebras to sets while $F$ maps sets to algebras. $F$ and $U$ are not in general inverses of each other, but they are nonetheless related in a way we now make precise.

For any category $\mathbf{C}$, the notation $\mathbf{C}(A, B)$ is generally used to denote the set of all morphisms from object $A$ to object $B$ in category $\mathbf{C}$. And the set of all functions from the set $X$ to the set $Y$ can be understood as the particular case $\mathbf{Set}(X, Y)$ of this convention where $\mathbf{C}$ is taken to be the class $\mathbf{Set}$ of all sets, which we can think of as *discrete* algebras, that is, algebras with no structure. A class of algebras along with a specified set of homomorphisms between any two of its members is an instance of a *category*. The members of the class are called the *objects* of the category while the homomorphisms are called the *morphisms*.

The bijection we have just observed can now be stated as

$$ \mathbf{C}(F(X), A) \cong \mathbf{Set}(X, U(A)) $$

Such a bijection is called an *adjunction* between $\mathbf{Set}$ and $\mathbf{C}$. Here $F: \mathbf{Set}\rightarrow \mathbf{C}$ and $U: \mathbf{C}\rightarrow \mathbf{Set}$ are respectively the left and right *adjoints* of this adjunction; we say that $F$ is left adjoint to (or of) $U$ and $U$ right adjoint to $F$.

We have only described how $F$ maps sets to algebras, and $U$ maps algebras to sets. However $F$ also maps functions to homomorphisms, mapping each function $f$ to its unique extension as a homomorphism, while $U$ maps homomorphisms to functions, namely the homomorphism itself as a function. Such maps between categories are instances of *functors*.

In general a category $C$ consists of objects $a, b, c$ and morphisms $f: a\rightarrow b$, together with an associative composition law for “composable” morphisms $f: b\rightarrow c$, $g: a\rightarrow b$ yielding the morphism $fg: a\rightarrow c$. Furthermore every object a has an identity element $1_a : a\rightarrow a$ which whenever composable with a morphism $f$ (on one side or the other) composes with it to yield $f$. A functor $F: C\rightarrow D$ maps objects of $C$ to objects of $D$ and morphisms of $C$ to morphisms of $D$, such that $F(fg) = F(f)F(g)$ and $F(1_a) = 1_{F(a)}$. That is, functors are “homomorphisms of categories,” preserving composition and identities.

With no further qualification such a category is considered an *abstract* category. The categories we have been working with are *concrete* in the sense that they come with a given underlying set or *forgetful* functor $U: C\rightarrow$Set. That is, algebras are based on sets, homomorphisms are certain functions between these sets, and $U$ simply “forgets” the algebraic structure. Such forgetful functors are *faithful* in the sense that for any two morphisms $f, g: a\rightarrow b$ of $C$, if $U(f) = U(g)$ then $f = g,$ i.e. $U$ does not identify distinct homomorphisms. In general a concrete category is defined as a category $C$ together with a faithful forgetful functor $U: C\rightarrow \textrm{Set}$.

Categories themselves admit a further generalization to 2-categories as algebras over two-dimensional graphs, with associative composition of 1-cells generalized to the 2-associative pasting of 2-cells. A further simplification of the free-algebra machinery then obtains, namely via abstract adjunctions as the natural 2-dimensional counterpart of isomorphisms in a category, which in turn is the natural 1-dimensional counterpart of equality of elements in a set, the 0-dimensional idea that two points can turn out to be one. This leads to a notion of abstract monad as simply the composition of an adjoint pair of 1-cells, one of which is the 1-cell abstracting the functor $F$ that manufactures the free algebra $F(V)$ from $V$. Ordinary or concrete monads arise as the composition of functors as concrete 1-cells of a 2-category of categories.

## References（引用注释）

> 原文参考文献已转为脚注引用：文内“作者-年份”引用组后附 [^key] 标记，完整条目见本文末脚注定义。

## Academic Tools

> |   | [How to cite this entry](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=algebra). |
> | --- | --- |
> |   | [Preview the PDF version of this entry](https://leibniz.stanford.edu/friends/preview/algebra/) at the [Friends of the SEP Society](https://leibniz.stanford.edu/friends/). |
> |   | [Look up topics and thinkers related to this entry](https://www.inphoproject.org/entity?sep=algebra&redirect=True) at the Internet Philosophy Ontology Project (InPhO). |
> |   | [Enhanced bibliography for this entry](https://philpapers.org/sep/algebra/) at [PhilPapers](https://philpapers.org/), with links to its database. |

## Other Internet Resources

- [Many algebraic topics](http://mathworld.wolfram.com/topics/Algebra.html), at Mathworld, Wolfram Research.
- [Linear algebra](http://www.answers.com/topic/linear-algebra), at Answers.com

## Related Entries

Boolean algebra: the mathematics of | category theory

[^harold-1979]: Harold R. Jacobs, *Elementary Algebra*, 876pp, W.H. Freeman, 1979.

[^bartel-1930]: Bartel Leendert van der Waerden, *Moderne Algebra* (2 volumes), Springer, Vol. 1 1930, Vol. 2 1931.

[^herstein-1975]: I.N. Herstein, *Topics in Algebra*, 2nd ed, 400pp, Wiley, 1975.

[^saunders-1978]: Saunders Mac Lane, *Categories for the Working Mathematician*, Springer-Verlag, 1978.
