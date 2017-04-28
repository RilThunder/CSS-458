import numpy as np
import random

HOT = 50
COLD = 0
AMBIENT = 25
hotSites = ((4, 5), (7, 8), (4, 8))
coldSites = ((3, 4), (7, 5), (1, 5))


def diffusion(site, N, NE, E, SE, S, SW, W, NW):
    list = [N, NE, E, SE, S, SW, W, NW]
    listOfCoefficient = []
    sumOfCoeffiencient = 0
    count = 0
    while (True and count < 8):
        distribution = np.random.normal(0.0, 0.5)

        sumOfCoeffiencient += distribution
        count = count + 1
        listOfCoefficient.append(distribution)

    listOfCoefficient = np.asarray(listOfCoefficient)
    list = np.asarray(list)
    totalSum = listOfCoefficient * list

    totalSum = totalSum.sum()

    return (1 - sumOfCoeffiencient) * site + totalSum


def initBar(m, n, hotSites, coldSites):
    ambientBar = np.zeros((m, n))
    ambientBar.fill(AMBIENT)

    return applyHotCold(ambientBar, hotSites, coldSites)


def applyHotCold(bar, hotSites, coldSites):
    newBar = bar

    for x in hotSites:
        newBar[x[0]][x[1]] = HOT
    for x in coldSites:
        newBar[x[0]][x[1]] = COLD

    return newBar


def difussionExtended(theBar):
    shape = theBar.shape
    numberOfRow = shape[0]
    numberOfColumn = shape[1]
    for x in range(1, numberOfRow - 1):
        for y in range(1, numberOfColumn - 1):
            theBar[x][y] = diffusion(theBar[x][y], theBar[x - 1][y], theBar[x - 1][y - 1], theBar[x][y + 1],
                                     theBar[x + 1][y + 1], theBar[x + 1][y], theBar[x + 1][y - 1], theBar[x][y - 1],
                                     theBar[x - 1][y - 1])
    return theBar


def reflectingLAT(lat):
    shape = lat.shape

    latNS = np.concatenate((lat[0, :].reshape(1, shape[1]), lat, lat[-1, :].reshape(1, shape[1])))
    valueToReturn = np.concatenate((latNS[:, 0].reshape(shape[0] + 2, 1), latNS, latNS[:, -1].reshape(shape[0] + 2, 1)),
                                   axis=1)

    return valueToReturn


def diffusionSim(m, n, t):
    bar = initBar(m, n, hotSites, coldSites)

    grids = []
    for i in range(t):
        barExtended = reflectingLAT(bar)

        bar = difussionExtended(barExtended)
        bar = applyHotCold(bar, hotSites, coldSites)
        grids.append(bar)
    return grids


x = diffusionSim(10, 10, 20)
print(x[0])
