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

from graphics import *
import matplotlib.pylot as plt
from random import random

EMPTY = 0
TREE = 1
BURNING = 2

WIN_SIZE = 300


def main():
    t = 5  # number of time steps
    n = 19  # size of forest
    percentList = []
    probability = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)
    index = 0
    for number in range(8):
        forest = initForest(n)

        grids = []
        grids.append(forest)

        for i in range(10):
            forestExtended = extendLat(forest)
            forest = applyExtended(forestExtended, probability[index])
            grids.append(forest)
        # print "After generation"
        #    for grid in grids:
        #        displayMat(grid)
        #        print
        finalResult = grids[-1]

        count = 0.0
        for i in finalResult:
            for j in i:
                if j != TREE:
                    count += 1

        percent = count / (n - 2) ** 2
        percentList.append(percent)
        index = index + 1
    print('The percentage of tree burned in each simulation ')
    print(percentList)
    plt.plot(probability, percentList)
    plt.show()
    # showGraphs(grids)


# Function to return forest of all trees with one burning
# tree in the middle.  Forest is surrounded by ground.

def initForest(n):
    forest = [[] for i in range(n)]
    probTree = 0.5
    probBurning = 0.5
    for i in range(n):
        for j in range(n):
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

        if (random() < burnProbability):
            returnValue = BURNING
        else:
            returnValue = TREE


    else:
        returnValue = TREE

    return returnValue


# Function to display animation of a list of grids

def showGraphs(graphList):
    win = GraphWin("Fire", WIN_SIZE, WIN_SIZE)
    win.setBackground("white")
    for grid in graphList:
        drawMat(win, grid)


# Function to draw matrix
# Empty (EMPTY = 0) shows yellow; tree (TREE = 1) shows green;
# burning tree (BURNING = 2) shows burnt orange.

def drawMat(win, mat):
    n = len(mat) - 2
    width = WIN_SIZE / (n + 1)
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            cell = Rectangle(Point(width * i, width * j), \
                             Point(width * (i + 1), width * (j + 1)))
            if (mat[i][j] == EMPTY):
                cell.setFill("yellow1")
            elif (mat[i][j] == TREE):
                cell.setFill("green2")
            else:
                cell.setFill("orange2")
            cell.draw(win)


main()
