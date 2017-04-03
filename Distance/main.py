#-----------------------------------------------------------------------
#                       Additional Documentation
#   Author: Thuan Tran
#   Date: April 3rd.2017
#   Python Distance Function
#=======================================================================


import numpy as N

#-------------------- Main module ---------------------
"""
    This function is used to test the distance function below and print out the result
"""
def main():
    x = N.array([0, 1, 2, 3, 4])
    y = N.array([0, 1, 2, 3])
    pt = N.array([-2.3, 3.3])
    print(distance(x, y, pt))

#-------------------- General Function: Distance Function ---------------------
"""
    This function is used to calculate a distance from a point to others point and return the result
    Method Arguments:
    *firstList: The array of the values in the x axis
    *secondList: The array of the values in the y axis
    *originalPoint: an array that hold the cordinate of the original Point (x,y)
    
    For every point in the x axis, it will be connected to a point on the y axis (Cartesian Product)
    
    Return:
    An array that have the distance from the original Point to every point on the x and y axis
"""
def distance(firstList, secondList, originalPoint):
    ## Perform cartesian product and calculate the distance at the same time
    output = [((((xAxis - originalPoint[0]) ** 2) + ((yAxis - originalPoint[1]) ** 2)) ** 0.5) \
              for xAxis in firstList for yAxis in secondList]

    ## Reshape the array in a row wise order
    output = N.reshape(output, (secondList.size, firstList.size), order='F')
    return output

# Call the main module
main()
