#Addition is done between two arguments whereas summation happens over n elements.

import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([1,2,3])
newarr=np.add(arr1, arr2)
print(newarr)

newArr=np.sum([arr1, arr2])
print(newArr)

#If you specify axis=1, NumPy will sum the numbers in each array.
newArrAxis=np.sum([arr1, arr2], axis=1)
print(newArrAxis)

#Cummulative sum means partially adding the elements in array.
newArrComm=np.cumsum(arr1)
print(newArrComm)