#Data Distribution is a list of all possible values, and how often each value occurs.

#random distribution-set of random numbers that follow a certain probability density function

from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

#shuffle - changes the original array
import numpy as np
arr=np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)


#permutation - doesn't change the original array
print(random.permutation(arr))