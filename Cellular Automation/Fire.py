# Fire.py
#
# Simulation of fire spread by generating a list of grids simulating
# fire spreading, the total burned, and the percentage burned
#
# Introduction to Computational Science:  Modeling and Simulation for the Sciences
# Angela B. Shiflet and George W. Shiflet
# Wofford College
# Copyright 2006 by Princeton University Press
#
# In site,  
# 	EMPTY (0) - empty,  
# 	TREE (1) - non - burning tree,  
# 	BURNING (2) - burning tree  
# Next value based on site and nearest neighbors (N, E, S, W) 
#


# Tiny modification by Thuan Tran
# Module 10.3 Project 9
# Date April 29th,2017


import numpy as np
from numpy.polynomial import Polynomial
from random import random

import matplotlib.pyplot as plt

# Constants
EMPTY = 0
TREE = 1
BURNING = 2
TIMESTEP = 10
WIN_SIZE = 300


def main():
    t = 5  # number of time steps
    n = 17  # size of forest
    percentListEachExperiment = []
    percentList = []
    probability = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)
    index = 0
    # Do 8 experiments, each with different probability of burning
    for number in range(9):
        forest = initForest(n)

        grids = []
        grids.append(forest)
        for experiment in range(10):
            for i in range(TIMESTEP):
                forestExtended = extendLat(forest)
                forest = applyExtended(forestExtended, probability[index])
                grids.append(forest)

            finalResult = grids[-1]

            # Count how many area that is not tree
            count = 0.0
            for i in finalResult:
                for j in i:
                    if j != TREE:
                        count += 1

            percent = count / ((n) ** 2)
            # Get the percent of buring at each simulation at each probability of burning
            percentListEachExperiment.append(percent)
        # Get the average percent of burning for that probability
        percentList.append(np.average(np.asarray(percentListEachExperiment)))
        index = index + 1
        percentListEachExperiment = []
    print('The average percentage of tree burned in each simulation ')
    print(percentList)
    plt.figure()
    plt.plot(probability, percentList, label='Calculated Data')
    # Decided to use 5th order polynomial
    p = Polynomial.fit(probability, percentList, 5)
    plt.plot(*p.linspace(), label='Curved Data')
    plt.legend(loc='upper left')
    plt.xlabel('Probability of burning')
    plt.ylabel('Percent of tree burned')
    plt.title('Graph that show the percent of tree burn as probability of burn increase')
    plt.show()


# Function to return forest of all trees with one burning
# tree in the middle.  Forest is surrounded by ground.

def initForest(n):
    forest = [[] for i in range(n)]
    probTree = 0.5
    probBurning = 0.5
    for i in range(n):
        for j in range(n):
            # Initialize the middle tree to burning
            if (i == n / 2 and j == n / 2):
                forest[i].append(BURNING)
                continue
            forest[i].append(TREE)

    return forest


# Function to return an (n + 2) - by - (n + 2) matrix
# with periodic boundaries for mat, an n - by - n matrix

def extendLat(mat):
    n = len(mat)
    matNS = [mat[n - 1]]
    matNS = matNS + mat
    matNS.append(mat[0])
    matExt = [[] for i in range(n + 2)]
    for i in range(n + 2):
        matExt[i] = [matNS[i][n - 1]] + matNS[i] + [matNS[i][0]]
    return matExt


# Function to display values in a matrix

def displayMat(mat):
    for row in mat:
        print (row)


# Function to apply spread function

def applyExtended(mat, probabiltity):
    copy = copyInsideMat(mat)
    n = len(copy)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            site = mat[i][j]
            N = mat[i - 1][j]
            E = mat[i][j + 1]
            S = mat[i + 1][j]
            W = mat[i][j - 1]
            copy[i - 1][j - 1] = spread(site, N, E, S, W, probabiltity)
    return copy


# Function to return a copy of the inside of a square matrix

def copyInsideMat(mat):
    m = len(mat) - 2
    copy = [[] for i in range(m)]

    for i in range(m):
        for j in range(m):
            copy[i].append(mat[i + 1][j + 1])

    return copy


# Function to spread fire by the following rules:
#   At next time step an empty site remains empty.
#   Burning tree results in empty cell next time step.
#   Perhaps next time step tree with burning neighbor(s) burns itself.
#   Perhaps tree is hit by lightning and burns next time step.

def spread(site, N, E, S, W, burnProbability):
    probImmune = 0.5  # probability of immunity from catching fire - global variable
    probLightning = 0.01  # probability of lightning - global variable
    if (site == EMPTY) or (site == BURNING):
        returnValue = EMPTY
    elif (site == TREE) and ((N == BURNING) or (E == BURNING) or
                                 (S == BURNING) or (W == BURNING)):
        # There is now no probability of lightning or immune
        if (random() < burnProbability):
            returnValue = BURNING
        else:
            returnValue = TREE


    else:
        returnValue = TREE

    return returnValue


main()
