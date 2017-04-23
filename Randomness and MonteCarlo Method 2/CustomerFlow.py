# =============================================================================
# Randomness and MonteCarlo Method 2
# Customer Flow Simulation page 195
# Daniel P. Maki and Maynard Thompson, Mathematical Modeling and Computer Simulation,
# Belmont, CA: Thomson Brooks/Cole, 2006:
#
# Thuan Tran
# April 22th , 2017
#
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

# The number of iterations the simulation will do for the day
trials = 1000

# Input data from the assignment
mean = np.array([10, 15, 5, 15, 10])
standardDeviation = np.array([2.3, 2.8, 1.6, 2.8, 2.3])
variance = standardDeviation ** 2

# Get the n and p of the first data to generate a binomial distribution
coreCustomerPValue = 1 - variance / mean
coreCustomerNValue = mean / coreCustomerPValue
casualCustomerPValue = 0.01
casualCustomerNValue = np.array([100, 150, 50, 150, 100])

# total number at each time segments for 1 iteration (20 time segments)
totalCore = np.zeros(20)
totalCasual = np.zeros(20)
totalCustomer = np.zeros(20)

# Total number of customer for 1000 trials
customerForEachIteration = np.zeros(trials)

# number of Customer of all iteration for each time segment
coreCustomerForEachTimeSegment = np.zeros(20)
normalCustomerForEachTimeSegment = np.zeros(20)
totalCustomerForEachTimeSegment = np.zeros(20)

"""""
    This function is used to calculate all the data to generate the table in the assignment
    It will calculate the number of total customer for all day, for each segment
    It will also calculate the number of core and casual customer at each segment
    :parameter n the p value to calculate for the binomial distribution for each time segment
"""""


def getTheDataForTable(n):
    numberOfIteration = 0
    coreCustomer = 0
    casualCustomer = 0
    # Define global variable to access and modify
    global totalCore
    global casualCustomerPValue
    global totalCasual
    global totalCustomer
    global coreCustomerForEachTimeSegment
    global normalCustomerForEachTimeSegment
    global totalCustomerForEachTimeSegment
    global customerForEachIteration
    while (numberOfIteration < trials):
        for i in range(1, 21, 1):
            # Perform a context switch for the time segments
            if (i <= 2):  # 11-12 PM
                count = 0
            else:
                casualCustomerPValue = n * (coreCustomer + casualCustomer) + 0.01
                if (i <= 4):  # 12 - 1 PM
                    count = 1
                else:
                    if (i <= 12):  # 1-5 PM
                        count = 2
                    else:
                        if (i <= 18):  # 5-8PM
                            count = 3
                        else:
                            count = 4  # 8 - 9 PM
            # Draw a number of a binomial distribution
            coreCustomer = np.random.binomial(coreCustomerNValue[count], coreCustomerPValue[count])
            casualCustomer = np.random.binomial(casualCustomerNValue[count], casualCustomerPValue)
            allCustomer = coreCustomer + casualCustomer  # Get and save the data for each time segment
            totalCore[i - 1] = totalCore[i - 1] + coreCustomer
            totalCasual[i - 1] = totalCasual[i - 1] + casualCustomer
            totalCustomer[i - 1] = totalCustomer[i - 1] + allCustomer

        # Get and save the data for all time segment across all iteration
        for i in range(1, 21, 1):
            coreCustomerForEachTimeSegment[i - 1] = coreCustomerForEachTimeSegment[i - 1] + totalCore[i - 1]
            normalCustomerForEachTimeSegment[i - 1] = normalCustomerForEachTimeSegment[i - 1] + totalCasual[i - 1]
            totalCustomerForEachTimeSegment[i - 1] = totalCustomerForEachTimeSegment[i - 1] + totalCustomer[i - 1]

        customerForEachIteration[numberOfIteration] = sum(totalCustomer)
        numberOfIteration = numberOfIteration + 1
        # Reset to a whole new day
        totalCustomer = np.zeros(20)
        totalCore = np.zeros(20)
        totalCasual = np.zeros(20)
    return customerForEachIteration / trials


"""
    This function is used to perform the analysis of the relationship between
    the p value versus the total average number of customer
    This function will also analyze the relationship between the mall traffic and the
    total average number of customer
"""


def Analysis():
    # Define these gloval vaiable for access and modify
    global casualCustomerNValue
    global coreCustomerForEachTimeSegment
    global normalCustomerForEachTimeSegment
    global totalCustomerForEachTimeSegment
    global customerForEachIteration

    coreCustomerForEachTimeSegment = np.zeros(20)
    normalCustomerForEachTimeSegment = np.zeros(20)
    totalCustomerForEachTimeSegment = np.zeros(20)
    customerForEachIteration = np.zeros(trials)

    # The p value
    xAxis = np.arange(0.002, 0.004, 0.0001)
    yAxis = []

    # The percentage increase of mall traffic
    xAxisPercentage = []
    yAxisPercentage = []

    percent = 0.1  # Initialze value assume that the store increase 10 percent

    for i in xAxis:
        # Assume that the new customer value will change with respect to the frequency
        # Not change after it receive new value
        # For example : the change will based on default value
        # Not based on the previous change

        casualCustomerNValue = np.array([100, 150, 50, 150, 100])

        # Get the total number of customer with respect to that p value
        yAxis.append(np.sum(getTheDataForTable(i)))

        casualCustomerNValue = casualCustomerNValue * (1 + percent)
        xAxisPercentage.append(percent)
        yAxisPercentage.append(np.sum(getTheDataForTable(xAxis[0])))
        percent = percent + 0.02

    # Plot and label the figures
    plt.figure()
    plt.plot(xAxis, yAxis)
    plt.xlabel('P value, probability')
    plt.ylabel('Average number of customer')
    plt.title('Number of average customer if we increase the p value from 0.002 to 0.004 with'
              'increment of 0.0001')
    plt.figure()
    plt.plot(xAxisPercentage, yAxisPercentage)
    plt.xlabel('Percentage')
    plt.ylabel('Average number of customer')
    plt.title('Number of average customer if we increase the mall traffic with increment of 2%')
    plt.show()


def main():
    getTheDataForTable(0.002)
    # Display the table
    print('Time Segment' + '\t' + 'Mean number of Core' + '\t\t' + 'Mean number of Casual' + '\t' + 'Mean Total')
    print('------------------------------------------------------------------------')
    for i in range(1, 21, 1):
        print('\t' + str(i) + '\t\t\t\t' + str((coreCustomerForEachTimeSegment / trials)[i - 1]) + '\t\t\t\t\t' + str(
            (normalCustomerForEachTimeSegment / trials)[i - 1]) \
              + '\t\t\t\t' + str((totalCustomerForEachTimeSegment / trials)[i - 1]))

    # Get the data for the last row
    coreSum = np.sum(coreCustomerForEachTimeSegment / trials)
    casualSum = np.sum(normalCustomerForEachTimeSegment / trials)
    totalSum = np.sum(totalCustomerForEachTimeSegment / trials)

    print('------------------------------------------------------------------------')
    print('Total' + '\t\t\t\t' + str(coreSum) + '\t\t\t\t\t' + str(casualSum) + '\t\t\t\t' + str(totalSum))
    print('Standard Deviation of the total customer   ' + str(np.std(customerForEachIteration)))

    Analysis()


main()
