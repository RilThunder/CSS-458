import numpy as np
import random

def distribution(npts):
    distribution = np.zeros(npts)
    count = 0 # This is the index of the 1D array
    for i in distribution:
        while True:
            # Generate random X and Y for later comparison
            randomX = random.uniform(0.0,1.0)
            randomY = random.uniform(0.0,2.0)
            # Only when it satisfy these requirements then we place them into the array
            if (randomX < 0.5 and randomY <=1.75):
                distribution[count] = 1.75
                count +=1
                break
            else:
                if (randomX >= 0.5 and randomY <= 0.25):
                    distribution[count]= 0.25
                    count = count+1
                    break
            continue
    return distribution

# Testing
a = distribution(100)

print(a)