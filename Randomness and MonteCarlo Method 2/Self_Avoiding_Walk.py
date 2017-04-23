# =============================================================================
# Randomness and MonteCarlo Method 2
# Note: The animateRandomWalk function belongs to professor Johnny Lin (University of Washington Bothell)
# Thuan Tran
# April 22th , 2017
#
# =============================================================================

import math
import numpy as N
import matplotlib.pyplot as plt

"""
    Constants for this assignment
"""
firstStep = 3
lastStep = 10
numberOfTimes = 1000

"""
    This function repareset a random self walk
    During random self walk, each walk will be random and will not cross where it used to walk
    Initile starting point will be the origin (0,0)
    If a walk randomly crossed where it used to walk, the walk will end there
"""


def randomSelfWalk():
    firstList = []  # List of cordinates of x and y Axis
    secondList = []
    sumX = 0  # Represent where on the x Axis the walk is at
    sumY = 0  # Same as above but y Axis
    firstList.append(sumX)
    secondList.append(sumY)

    while (True):
        randomX = N.random.randint(0, 2)
        # Determind go right or left, or up or down
        if (randomX == 0):
            sumX = sumX - 1
        else:
            sumX = sumX + 1
        randomY = N.random.randint(0, 2)

        if (randomY == 0):
            sumY = sumY - 1
        else:
            sumY = sumY + 1

        # Oops, already walked there before, stop
        if (firstList.__contains__(sumX) and secondList.__contains__(sumY)):
            break

        # Didn't walk before, add to list
        firstList.append(sumX)
        secondList.append(sumY)

    output_list_y = N.asarray(secondList)
    output_list_x = N.asarray(firstList)

    return (output_list_x, output_list_y)


""""
    This function animate the walk by walking through each point in the X cordinate and y Cordinate
    And update the plot 
    This function was written by Professor Johnny Lin
"""


def animateWalk(x_points, y_points):
    plt.ion()  # - Turn interative mode on

    mylines = plt.plot(x_points, y_points, "o-")  # - mylines is a list of
    #  lines drawn by plot
    line = mylines[0]  # - there's only one line drawn by the above plot call
    plt.axis([N.min(x_points), N.max(x_points),
              N.min(y_points), N.max(y_points)])
    plt.title('Random Walk')
    for i in range(N.size(x_points)):
        line.set_xdata(x_points[:i + 1])
        line.set_ydata(y_points[:i + 1])
        plt.draw()
        plt.pause(1)
    plt.ioff()


"""""
    This function calculates the displacement of a walk with n number of steps
    It will also record the frequency of a random walk that is at least n number of steps
    :parameter n number of step
    
"""""


def functionOfN(n):
    # Initilize to default value
    dictionaryDisplacement[str(n)] = 0
    dictionary[str(n)] = 0
    i = 0
    count = 0
    countDisplaceMent = 0
    sumOfDistance = 0.0

    while (i < numberOfTimes):
        # Get the self-avoiding walk
        xpts, ypts = randomSelfWalk()
        # See how much step the walk took
        size = N.size(xpts)
        # Record the value and calculate the distance
        if (size == n):
            countDisplaceMent = countDisplaceMent + 1
            finalXPosition = xpts[-1]
            finalYPosition = ypts[-1]
            sumOfDistance = sumOfDistance + finalXPosition ** 2 + finalYPosition ** 2
        if (size >= n):
            count = count + 1
        i = i + 1
    # Save the variable of the number of steps the function f(n) took at least
    dictionary[str(n)] = count

    # Get the fraction of number of time the function produce at least n steps over number of iteration
    print("Now print out the fraction of part b")
    print(count / numberOfTimes)
    if (countDisplaceMent == 0):
        print("There is no walk that match the number of Step")
    else:
        result = math.sqrt(sumOfDistance / countDisplaceMent)
        dictionaryDisplacement[str(n)] = result
        print("The Root-Mean Square Displace is " + str(result))


dictionary = {}
dictionaryDisplacement = {}
print("Now print out a random Self-Avoiding Walk")
xpts, ypts = randomSelfWalk()  # - Test the randomWalkPoints method
animateWalk(xpts, ypts)  # using animation
for i in range(firstStep, lastStep, 1):
    functionOfN(i)

plt.figure()
# Prepare the xAxis and y axis for the plot

xAxis = []
yAxis = []

rangeToIterate = range(firstStep, lastStep, 1)
index = 0
for i in sorted(dictionary):
    yAxis.append(dictionary[i])
    xAxis.append(rangeToIterate[index])
    index = index + 1

plt.bar(xAxis, yAxis)
plt.title("Plot count at least n steps was taken")
plt.xlabel('Number of steps')
plt.ylabel('Frequency')

plt.figure()
yAxis = []

for i in sorted(dictionaryDisplacement):
    yAxis.append(dictionaryDisplacement[i])

plt.bar(xAxis, yAxis)
plt.title('Plot display the Displacement')
plt.ylabel('Displacement')
plt.xlabel('Number of steps')
plt.show()
