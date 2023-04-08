# set is collection of unique elements, used for operations involving intersection, union, difference.

import numpy as np

arr = np.array([1, 1, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7])
x=np.unique(arr)
print(x)


#finding union
arr1= np.array([1,2,3,4])
arr2=np.array([3,4,5,6])
arrUnion=np.union1d(arr1, arr2)
print(arrUnion)


#finding intersection
arrInter=np.intersect1d(arr1, arr2)
print(arrInter)

#finding difference
arrDiff=np.setdiff1d(arr1, arr2, assume_unique=True)
print(arrDiff)

#finding symmetric difference
arrSym=np.setxor1d(arr1, arr2, assume_unique=True)
print(arrSym)