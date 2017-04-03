#-----------------------------------------------------------------------
#                       Additional Documentation
#   Author: Thuan Tran
#   Date: April 3rd.2017
#   Python Exponential Function
#=======================================================================

import math

#-------------------- Main module ---------------------
"""
    This function is used to test the exponential function below and print out the result
"""
def main():
    a = exponential(3.4,tol=1e-8)
    print(a)


#-------------------- General Function:  exponential ---------------------
""" Method Arguments:
    * x: The number to calculate the exponential in the form e^x
    e^x is calulated through : Sum(n->infinity) of (x^n/n!) where n start at 0
    * tol: The tolerance level so that the function will stop will it reach this level
    Output:
    This function will return the exponential of x in the form e^x
"""


def exponential(x,tol=1e-10):
    sum = 0 # The current sum
    n=0 #  N is on the documentation above
    previousSum = 0
    range = 0 # The difference between the previous Sum and this sum. Used to check if the sum converge

    while (True): # Loop untl the sum converge
        previousSum = sum
        sum = sum +( (x**n)/math.factorial(n)) #Utilize the Factorial function
        n=n+1
        range = sum-previousSum # Check the difference between 2 sums
        if (range < tol):
            return sum # They are in the range, return the value

# Call the main module
main()