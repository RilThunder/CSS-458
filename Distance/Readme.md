Create a function distance that takes a vector of x-locations and a vector of y-locations and calculates the distance at all points defined by those locations from a given point. For instance, say you have the following vectors of x and y-locations for a 4 by 3 Cartesian grid and the (x,y) location of the point pt:

>>>import numpy as N

>>>x = N.array([0, 1, 2, 3, 4])

>>>y = N.array([0, 1, 2, 3])

>>>pt = N.array([-2.3, 2.1])

The following distance function call will return dist, a NumPy array of shape (3,4) that holds the distance from pt to each point specified by x and y:

>>>dist = distance(x, y, pt)

Hint: Remember that a NumPy array encoding a (4,3) Cartesian grid will have shape (3,4), since it's the last index that runs through the columns (Links to an external site.). Also, depending on how you'll display the output array, you have to remember whether the point (x[0], y[0]) is in the upper-left or lower-left corner. (These hints are meant not as prescriptive but rather to just alert you to some possible confusing issues.)

Make sure you include adequate, appropriate, and complete documentation. This includes a docstring for the function as well as comment lines in the code. For an example of adequate documentation, see my routine to calculate mixing ratio (Links to an external site.). (Don't worry if you don't know what mixing ratio is; just pay attention to the documentation.)

Test Code
Your solution must give the following results. Given this input:

>>>import numpy as N

>>>x = N.arange(5)

>>>y = N.arange(4)

>>>print(distance(x, y, [-2.3, 3.3]))

you must get this output (to within reasonable tolerances):

>>>[[ 4.02243707  4.66690476  5.42033209  6.24339651  7.11196175]

>>> [ 3.25269119  4.02243707  4.87647414  5.77754273  6.70671305]

>>> [ 2.64196896  3.54682957  4.49221549  5.45710546  6.43272881]

>>> [ 2.3194827   3.31360831  4.31045241  5.30848378  6.30713881]]

In the above listing, the "origin" point (x[0], y[0]) is in the upper left-hand corner.
