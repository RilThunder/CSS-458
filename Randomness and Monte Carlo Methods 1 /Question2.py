# -----------------------------------------------------------------------
#                       Additional Documentation
#   Author: Thuan Tran
#   Date: April 15th.2017
#   Randomness and Monte Carlo Method
#   Question 2 page 401
# =======================================================================


import random

import matplotlib.pyplot as plt
import numpy as np

"""
    This function is used to return a pair of value that use the Box-Muller Method 
    It used a mean and standard deviation from a normal distribution 
"""


def boxMethod():
    # Constant mean and stdDeviation can be changed
    mean = 7.0
    stdDeviation = 2.0
    # Formula of the Box-Muller method
    a = random.random() * 2 * np.pi
    b = stdDeviation * np.sqrt(-2 * np.log2(random.random()))
    firstCordinate = b * np.sin(a) + mean
    secondCordinate = b * np.cos(a) + mean
    return [firstCordinate, secondCordinate]


"""
    This function is the main method where it will generate 2 lists and plot them as histogram
    The first list composed of 500 pairs of values from the boxMethod
    The second list is the flatted version of the first list 
"""


def main():
    i = 0
    pair = []
    # Generate 500 pairs of normal distribution
    while (i < 500):
        pair.append(boxMethod())
        i = i + 1
    pairArray = np.array(pair)
    # Get the flatted version of the 500 pairs ( 1000 elements now)
    flattenArray = np.ndarray.flatten(pairArray)
    # The blue histogram is the flattenArray with 1000 elements
    plt.hist(flattenArray)
    # The organge and green bar is the pairArray where the orange is x value and green is y value
    plt.hist(pairArray)
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.show()


main()
