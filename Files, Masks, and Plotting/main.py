# -----------------------------------------------------------------------
#                       Additional Documentation
#   Author: Thuan Tran
#   Date: April 4rd.2017
#   Python File, Masks and Plotting
# =======================================================================
import numpy as N
import matplotlib.pyplot as plt


"""
    This function is used to load data from a text file, compute its average, median and standard deviation
    Assumption: The text file is in the same directory with the python file 
"""
def main():
    theFile = open("ASFG_Ts.txt", "r")
    i = 1
    # Skip the first 3 lines that include the names and a blank line
    while (i <= 3):
        theFile.readline()
        i = i + 1
    lines = theFile.readlines()
    JulianDay = []
    temperature = []
    for line in lines:
        # if the size of the line is not 82, it means that some data is missing
        if line.__sizeof__() != 82:
            # Use a flag variable
            temperature.append(N.finfo(N.float64).max)

            continue
        result = line.split("\t")[3].rstrip()
        day = float(line[0:8].rstrip())
        x = float(result)
        temperature.append(x)
        JulianDay.append(day)
    myarray = N.asarray(temperature)
    # Get the temperature where the temperature is not the flag
    newTemp = myarray[myarray != N.finfo(N.float64).max]
    newDay = N.asarray(JulianDay)
    # Calculate and display the mean, standard deviation and median
    average = newTemp.mean()
    print("The average temperature is " + str(average) + "\n")
    std = newTemp.std()
    print("The standard deviation is " + str(std) + "\n")
    med = N.median(newTemp)
    print("The median is " + str(med) + "\n")
    # Plot Julian Day(y axis) vs the temperature(x axis)
    plt.plot(newTemp, newDay)
    plt.xlabel("Temperature")
    plt.ylabel("Julian Day")
    plt.show()


# Call the main module
main()
