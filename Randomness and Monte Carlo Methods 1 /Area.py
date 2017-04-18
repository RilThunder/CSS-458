# -----------------------------------------------------------------------
#                       Additional Documentation
#   Author: Thuan Tran
#   Date: April 15th.2017
#   Randomness and Monte Carlo Method
# =======================================================================

import random

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

imagineArea = 1.5 * 2
function = lambda x: np.sqrt(np.cos(x) ** 2 + 1)
actualArea = integrate.quad(function, 0.0, 2.0)
numberofTimes = 300  # Number of Iterations
calArea = np.zeros(300)  # holder for the calculated Area from throwing darts
index = 0
simulation = np.zeros(300)  # Number of dars at each iteration
numberofDarts = 1000

while (numberofTimes > 0):
    numberofDarts = numberofDarts + 100
    count = 0
    dartsBelow = 0.0
    while (count <= numberofDarts):
        count = count + 1
        randomX = random.uniform(0.0, 2.0)
        randomY = random.uniform(0.0, 1.5)
        # Get the actual y location at the random x location
        locationY = function(randomX)
        if (randomY < locationY):
            dartsBelow = dartsBelow + 1
    calculatedArea = imagineArea * (dartsBelow / numberofDarts)
    numberofTimes = numberofTimes - 1
    # Save the variables to plot later
    calArea[index] = calculatedArea
    simulation[index] = numberofDarts
    index = index + 1

# Get the relative error
error = [x - actualArea for x in calArea]
relativeError = np.absolute(error)
plt.plot(simulation, relativeError[:, 0])  # Only need the first column of the relative error
plt.ylabel('Relative Error')
plt.xlabel('Number of darts')
plt.show()

# As the number of darts increase, the relative error start to become smaller