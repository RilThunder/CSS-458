#-----------------------------------------------------------------------
#                       Additional Documentation
#   Author: Thuan Tran
#   Date: April 12th.2017
#   Python Computational Error
#=======================================================================




import numpy as np
import matplotlib.pyplot as plt



#-----------------------------------------------------------------------
# This area is used to define the initial constant
#=======================================================================
growth = 9.3 /100
initialInvestment = 500
time = [10,20,30,40]
time = np.asanyarray(time)
analyticAnswer = [1267.25,3211.86,8140.0,20632.19]
analyticAnswer = np.asanyarray(analyticAnswer)

# Calculate the result using Python
result = np.zeros(4);
for i in range(4):
    result[i]= initialInvestment*np.exp(growth * time[i])

#Calculate the absolute error and Relative error
abosoluteError = np.abs(analyticAnswer - result)
relativeError = abosoluteError / np.abs(analyticAnswer)


# Display the error
print('The abosulte error is')
print( abosoluteError)
print('The relative error is')
print(relativeError)

# Plot analytic answer vs result
# Line style and marker and color were choosed to make a distinction between two plot
plt.plot(time,result, marker='o', color='r')
plt.plot(time,analyticAnswer, linestyle ='--', color='g')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()
