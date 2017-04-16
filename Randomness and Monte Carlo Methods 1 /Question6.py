# -----------------------------------------------------------------------
#                       Additional Documentation
#   Author: Thuan Tran
#   Date: April 15th.2017
#   Randomness and Monte Carlo Method
#   Question 6 page 401
# =======================================================================
import random

import matplotlib.pyplot as plt
import numpy as np

# A global variable that represent the equation in the question
function = lambda x: 2 * np.pi * np.sin(4 * np.pi * x)

"""
    This function is used to return a random number if and only if the random number is less than
    2pi. The range of the random number is [0,0.25]
"""


def rej():
    rand = random.uniform(0, 0.25)
    if (function(rand) < np.pi * 2):
        return rand
    else:
        return rej()


"""
    This function is the main method where it will create a plot of f(x) from 0 to 0.25
    It will also create a list of 1000 random variables and use the global function 
    And plot them in a histogram 
"""


def main():
    # Generate a sequence of value from 0 to 0.25
    x = np.linspace(0, 0.25)
    y = function(x)
    plt.figure(1)
    plt.plot(x, y)
    plt.xlabel('X Value')
    plt.ylabel('Y Value ')
    list = []
    counter = 0
    # Create a list of 1000 random variable with the global function
    while (counter < 1000):
        list.append(function(random.uniform(0, 0.25)))
        counter = counter + 1
    plt.figure(2)
    plt.hist(list)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()


main()
