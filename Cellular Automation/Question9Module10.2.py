"""
Author Thuan Tran
Date: April 28th,2017
Cellular Automation
Module 10.2 Project 9
"""




import numpy as np
import matplotlib.pyplot as plt

# To do, figure out the logic error in diffusion method
# List of constants
totalSimulation = 30
rate = 0.1
HOT = 50
COLD = 0
AMBIENT = 25
# Random hot and cold location
hotSites = ((4, 5), (7, 8), (4, 8))
coldSites = ((3, 4), (7, 5), (1, 5))

"""""
    This function is the original Diffusion function in the book 
"""""


def originalDiffusion(diffusionRate, site, N, NE, E, SE, S, SW, W, NW):
    return (1 - 8 * diffusionRate) * site + diffusionRate * (N + NE + E + SE + S + SW + W + NW)


"""""
    This function is the modified diffusion that use probability
"""""


def diffusion(diffusionRate, site, N, NE, E, SE, S, SW, W, NW):
    list = [N, NE, E, SE, S, SW, W, NW]
    listOfCoefficient = []
    sumOfCoeffiencient = 0
    count = 0
    while (True and count < 8):
        # Draw a random number
        distribution = np.random.normal(0.0, 0.5)
        # Get the sumOfCoefficient for later calculating the site itself coefficient
        sumOfCoeffiencient += distribution
        count = count + 1
        listOfCoefficient.append(distribution)

    listOfCoefficient = np.asarray(listOfCoefficient)
    list = np.asarray(list)
    # calculate the average how each neighbor affect the site
    totalSum = ((1 + listOfCoefficient) * diffusionRate) * list

    totalSum = totalSum.sum()

    return (1 - abs((listOfCoefficient).sum())) * site + totalSum


"""""
    This function is the function in the book where it will initialize the bar with hot and cold value 
"""""
def initBar(m, n, hotSites, coldSites):
    ambientBar = np.zeros((m, n))
    ambientBar.fill(AMBIENT)

    return applyHotCold(ambientBar, hotSites, coldSites)


"""
    Apply the hold and cold value to the bar
"""
def applyHotCold(bar, hotSites, coldSites):
    newBar = bar

    for x in hotSites:
        newBar[x[0]][x[1]] = HOT
    for x in coldSites:
        newBar[x[0]][x[1]] = COLD

    return newBar


"""
    Calculate how effect of neightboring cell to the current location
"""


def difussionExtended(theBar, diffusionRate, number):
    shape = theBar.shape
    numberOfRow = shape[0]
    numberOfColumn = shape[1]
    if number == 1:
        # Decide to use whether the original or modified difusion
        function = diffusion
    else:
        function = originalDiffusion
    for x in range(1, numberOfRow - 1):
        for y in range(1, numberOfColumn - 1):
            theBar[x][y] = function(diffusionRate, theBar[x][y], theBar[x - 1][y], theBar[x - 1][y - 1],
                                    theBar[x][y + 1],
                                    theBar[x + 1][y + 1], theBar[x + 1][y], theBar[x + 1][y - 1], theBar[x][y - 1],
                                    theBar[x - 1][y - 1])
    return theBar


""""
    This function is used to extend the bar by concatening its row and column 
"""""
def reflectingLAT(lat):
    shape = lat.shape
    # Concatenate the row
    latNS = np.concatenate((lat[0, :].reshape(1, shape[1]), lat, lat[-1, :].reshape(1, shape[1])))
    # Concatenate the column
    valueToReturn = np.concatenate((latNS[:, 0].reshape(shape[0] + 2, 1), latNS, latNS[:, -1].reshape(shape[0] + 2, 1)),
                                   axis=1)

    return valueToReturn


""""" 
    The simulation of diffusion 
"""""


def diffusionSim(m, n, t, simulation):
    totalGrids = []

    numberOfSimulation = 0
    while numberOfSimulation < totalSimulation:
        bar = initBar(m, n, hotSites, coldSites)
        grids = []
        for i in range(t):
            barExtended = reflectingLAT(bar)

            bar = difussionExtended(barExtended, rate, simulation)
            bar = applyHotCold(bar, hotSites, coldSites)
            grids.append(bar)

        numberOfSimulation += 1
        # Save the total grids created at each simulation
        totalGrids.append(grids)
    return totalGrids


def getMean(list):
    minTemp = 0
    firstTime = True
    maxTemp = 0
    meanTemp = 0
    meanList = []
    count = 0
    for eachTimeStep in list:
        tempList = []
        for x in eachTimeStep:
            middle = x.shape
            # Get the point in the middle. Can change to other point if desired
            row = int(middle[0] / 2)
            column = int(middle[1] / 2)
            middleTemp = x[row][column]
            tempList.append(middleTemp)
            if firstTime:
                minTemp = middleTemp
                maxTemp = middleTemp
                firstTime = False
            if (middleTemp > maxTemp):
                maxTemp = middleTemp
            if (middleTemp < minTemp):
                minTemp = middleTemp
            tempList.append(middleTemp)
        meanTempThisIteration = np.average(np.asarray(tempList))

        meanList.append(meanTempThisIteration)
    return meanList


x = np.asarray(diffusionSim(10, 10, 20, 1))

yAxis = getMean(x)
# Find the min and max of all grids in all simulation




xAxis = range(1, totalSimulation + 1)
# Plot the simulation with probability diffusion
plt.figure()
plt.bar(xAxis, yAxis)
plt.title('Simulation with probability difusion')
plt.xlabel(' The number of each simulation')
plt.ylabel('The temperature')

y = np.asarray(diffusionSim(10, 10, 20, 0))
yAxis = getMean(y)
plt.figure()
plt.bar(xAxis, yAxis)
plt.title('Simulation with actual difusion')
plt.xlabel(' The number of each simulation')
plt.ylabel('The temperature')
plt.show()
