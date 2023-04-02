# joining means putting contents of two or more arrays in a single array

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# join 2d arrays (axis=1 means along rows)
arr1d = np.array([[1, 2], [3, 4]])
arr2d = np.array([[5, 6], [7, 8]])
arrdd = np.concatenate((arr1d, arr2d), axis=1)
print(arrdd)

arrddd = np.concatenate((arr1d, arr2d))  # axis=0
print(arrddd)

# using stack function (same as concatenation but with new axis)
arrstack = np.stack((arr1, arr2))
print(arrstack)


#hstack - to stack along rows
arrhstack=np.hstack((arr1, arr2))
print(arrhstack)

#vstack - to stack along columns
arrvstack=np.vstack((arr1, arr2))
print(arrvstack)

#dstack - to stack along height(depth)
arrdstack=np.dstack((arr1, arr2))
print(arrdstack)