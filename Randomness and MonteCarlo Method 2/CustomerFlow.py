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
import statistics
import math

mean = np.array([10, 15, 5, 15, 10])
standardDeviation = np.array([2.3, 2.8, 1.6, 2.8, 2.3])
variance = standardDeviation ** 2

# Get the n and p of the first data to generate a binomial distribution
coreCustomerPValue = 1 - variance / mean
coreCustomerNValue = mean / coreCustomerPValue
casualCustomerPValue = 0.01
casualCustomerNValue = np.array([100, 150, 50, 150, 100])

count = 0
coreCustomer = 0
casualCustomer = 0

totalCore = np.zeros(20)
totalCasual = np.zeros(20)
totalCustomer = np.zeros(20)
numberOfIteration = 0
customerForEachIteration = np.zeros(1000)
while (numberOfIteration < 1000):
    for i in range(1, 21, 1):
        if (i <= 2):
            count = 0
        else:
            casualCustomerPValue = 0.002 * (coreCustomer + casualCustomer) + 0.01
            if (i <= 4):
                count = 1
            else:
                if (i <= 12):
                    count = 2
                else:
                    if (i <= 18):
                        count = 3
                    else:
                        count = 4

        coreCustomer = np.random.binomial(coreCustomerNValue[count], coreCustomerPValue[count])
        casualCustomer = np.random.binomial(casualCustomerNValue[count], casualCustomerPValue)
        allCustomer = coreCustomer + casualCustomer
        totalCore[i - 1] = totalCore[i - 1] + coreCustomer
        totalCasual[i - 1] = totalCasual[i - 1] + casualCustomer
        totalCustomer[i - 1] = totalCustomer[i - 1] + allCustomer
    print(totalCustomer)
    customerForEachIteration[numberOfIteration] = sum(totalCustomer)
    numberOfIteration = numberOfIteration + 1

print('Time Segment' + '\t' + 'Mean number of Core' + '\t\t' + 'Mean number of Casual' + '\t' + 'Mean Total')
print('------------------------------------------------------------------------')
for i in range(1, 21, 1):
    print('\t' + str(i) + '\t\t\t\t' + str((totalCore / 1000)[i - 1]) + '\t\t\t\t\t' + str((totalCasual / 1000)[i - 1]) \
          + '\t\t\t\t' + str((totalCustomer / 1000)[i - 1]))

coreSum = np.sum(totalCore / 1000)
casualSum = np.sum(totalCasual / 1000)
totalSum = np.sum(totalCustomer / 1000)
print('------------------------------------------------------------------------')
print('Total' + '\t\t\t\t' + str(coreSum) + '\t\t\t\t\t' + str(casualSum) + '\t\t\t\t' + str(totalSum))
print('Standard Deviation of the total customer   ' + str(np.std(customerForEachIteration)))
