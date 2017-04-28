import numpy as np
import matplotlib.pyplot as plt

# A simple function that computer the value of the derivative
def getVal(x):
    changeInY = (-2.0 / x**3)
    return changeInY


def actualFunction(equation, xVal):
    x = np.array(xVal)
    y = equation(x) # Calculate y Value for every value of X
    plt.plot(x, y,'r',label="Actual Function")



# Define the equation
def my_formula(x):
    return 1/x**2

def main():
    # Starting from 1.01 and end at 5 with the increment of 0.01
    xValue = np.arange(1.01,5.01,0.01)

    # List of point to plot
    xList =[]
    yList = []
    # Initial Value
    xList.append(1)
    yList.append(1)
    for i in xValue:
        # Calculate the value using Euler's Method
        newX = i
        newY = yList[-1]+0.01* getVal(xList[-1])
        xList.append(newX)
        yList.append(newY)

    plt.plot(xList,yList,'b',label="Estimate Function")
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    # Plot the actual function
    actualFunction(my_formula, xValue)
    plt.legend(loc='upper right')
    plt.title('The function 1 / x^2 ')
    plt.show()


main()



